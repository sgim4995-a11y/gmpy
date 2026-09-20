#첫번째 값, 두번째 값을 입력받아 +,-,*,/ 값을 출력하시오.

# a = input("첫번째 값을 입력하시오 >>")
# b = input("두번째 값을 입력하시오 >>")

# print(a+b)

# print("{}+{}".format(a,b))
# print("{}-{}".format(a,b))
# print("{}*{}".format(a,b))
# print("{}/{}".format(a,b))
#타입변환방법 : int,float,str 앞에 붙이기 
a = int(input("값입력 : "))
 #input의 타입 무조건 str타입
b = int(input("값입력2 : "))
# a,b더하기값:15
# a,b빼기값 :5
# a,b곱하기값 :50
# a,b나누기값 :2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print("a,b더하기값 : %d+%d"% (a,b))
# print("a,b빼기값 : %d-%d"% (a,b))
# print("a,b곱하기값 : %d*%d"% (a,b))
# print("a,b나누기값 : %d/%d"% (a,b))

# print("a,b더하기값 : {}+{}".format(a,b))
# print("a,b빼기값 : {}-{}".format(a,b))
# print("a,b곱하기값 : {}*{}".format(a,b))
# print("a,b나누기값 : {}/{}".format(a,b))

print("a값:%d,b값:%d, 더하기값: %d"%(a,b,a+b))
print("a값:{},b값:{}, 더하기값: {}".format(a,b,a+b))
print("a값:%d,b값:%d, 나누기값: %.2f"%(a,b,a/b))
print("a값:{},b값:{}, 나누기값: {:.2f}".format(a,b,a/b))
print("a값:%d,b값:%d, 빼기값: %d"%(a,b,a-b))
print("a값:{},b값:{}, 빼기값: {}".format(a,b,a-b))
print("a값:%d,b값:%d, 곱하기값: %d"%(a,b,a*b))
print("a값:{},b값:{}, 곱하기값: {}".format(a,b,a*b))
#나누기는 무조건 실수타입
#print 문자열타입



