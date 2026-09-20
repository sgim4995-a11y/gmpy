# 타입 : int,float,str,bool
# 사칙연산 : +,-,*,/,//,%,**
# 다른타입 + 연산자를 사용할 수 없음
# 입력한 점수가 90점 이상 AQ, 80점 B,70-C,60-D,F
# 100~97 A+,A, 93~90:A-
# 89~87 B+,B,83~80:B-
# 79~77 C+,C, 73~70:C-
num = int(input("숫자 입력 >>"))
if num>=90:
    if num>97:
        print("A+")
    elif 93>=num>=90:
        print("A")
    else:
        print("A-")
elif 90>num>=80:
    print("B")
elif 80>num>=70:
    print("C")
elif 70>num>=60:
    print("D")
else:
    print("F")

# num = int(input("숫자를 입력 >> ")) #str타입
# ### 짝수인지,홀수인지 출력하시오.
# if num%2==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")
