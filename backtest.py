import pyupbit
import numpy as np

# ohlcv : opne, high, low, close, volume의 약자
# count = 7 : 7일 동안의 거래량을 가져온다는 의미
df = pyupbit.get_ohlcv("KRW-BTC", count=7)
# print(df)

# range = 변동폭, k = 0.5
df['range'] = (df['high'] - df['low']) * 0.5
# target = 매수가, range는 전날 값이므로 target을 구한 후 컬럼을 한 칸씩 밑으로 내림(shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# print(df)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# df['ror']에 대해 누적 곱 계산(cumprod)을 해서 누적 수익률을 구함
df['hpr'] = df['ror'].cumprod()

# dd = 'draw down(하락폭)'의 약자
# '누적 최댓값(cummax) - 현재 누적 수익률'을 누적 최댓값으로 나누면 하락폭을 구할 수 있음
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD은 'Draw Down(dd)' 중 최댓값
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")
