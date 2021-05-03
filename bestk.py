import pyupbit
import numpy as np


def get_ror(k=0.5):
    # 변동성 돌파전략 백테스팅 코드를 이용해서 누적 수익률 'ror'을 구함
    df = pyupbit.get_ohlcv("KRW-BTC", count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    # 수수료 fee는 일단 없는 것으로 생각
    # fee = 0.0032
    # df['ror'] = np.where(df['high'] > df['target'],
    #                      df['close'] / df['target'] - fee,
    #                      1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


# k 값을 0.1부터 1까지 0.1 단위로 증가시켜 ror을 구함
for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    # k값과 누적 수익률 출력
    print("%.1f %f" % (k, ror))
