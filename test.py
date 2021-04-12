import pyupbit

# 로그인
access = "access"          # 본인 값으로 변경
secret = "secret"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# 잔고조회
print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회(리플)
print(upbit.get_balance("KRW"))         # 보유 현금 조회(원화)
