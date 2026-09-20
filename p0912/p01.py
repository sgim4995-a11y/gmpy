# 리스트: 데이터 여러개를 한곳에 담아 놓은 것
# 방법: 대괄호 []로 묶고 그 안에 필요한 것들을 한꺼번에 넣음

# import datetime

# now = datetime.datetime.now()
# formatted_date = now.strftime("%Y-%m-%d")
# formatted_time = now.strftime("%H:%M:%S")

# print("포맷팅된 날짜:",formatted_date)
# print("포맷팅된 시간:",formatted_time)

# now = datetime.datetime.now()
# one_day = datetime.timedelta(days=1)
# yesterday = now - one_day
# tomorrow = now + one_day

# print("어제:", yesterday)
# print("오늘:", now)
# print("내일:", tomorrow)

import datetime

now = datetime.datetime.now()
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))
