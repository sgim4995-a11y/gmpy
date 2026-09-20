# a = 100
# #숫자형 - 정수타입 int
# b = 1.1
# #숫자형 - 실수타입 float
# c = "안녕"
# #문자형,문자열 str
# d = True
# #불타입(bool)

# a = 100
# type(a)
# print(type(a))
# a=10
# # a+= 5
# a= a+5
# print(a)

# money = 1234050
# #500원 동전 몇개가 필요할까요?
# num = money//500
# print("500원 동전 개수 : %d"% num)
# num2 = money%500
# print("나머지 : %d"% num2)
# print("나머지 : {}".format(num2))

money = 12982
# 500원 동전 몇개가 필요할까요?
# 100원 동전 몇개가 필요할까요?
num = money//500
# print("500원 동전 개수 : {}".format(num))
# num2 = money//100
# print("100원 동전 개수 : {}".format(num2))
#500원 동전으로 몇개, 나머지 100원으로 몇개?
num2 = (money%500)//100
print(" 500원 동전 :{}, 100원 동전 : {}".format(num,num2))


# 나머지 50원으로 몇개 필요?
num3 = ((money%500)%100)//50
print(" 500원 : {}, 100원 : {}, 50원 : {}".format(num,num2,num3))
#10원 동전 몇개 필요?
#1원 동전 몇개 필요?
num4 = (((money%500)%100)%50)//10
num5 = ((((money%500)%100)%50)%10)//1
print(" 500원 : {}, 100원 : {}, 50원 : {}, 10원 : {}, 1원 : {}".format(num,num2,num3,num4,num5))





