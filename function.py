#           근의 공식
#--------------------------------
##함수 사용X
'''
a = 1
b = 2
c = - 8

r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print("해는 {} 또는 {}.".format(r1, r2))
'''

##함수 사용O
##매개 변수X
'''
def print_root():
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print("해는 {} 또는 {}.".format(r1, r2))
    
a = 2
b = 4
c = -9

print_root()

a = 5
b = 6
c = -6

print_root()
'''

##함수 사용O
##매개 변수O
'''
def print_root(a, b, c):    #매개변수
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print("해는 {} 또는 {}.".format(r1, r2))
    
x = 2
y = 4
z = -9

print_root(x, y, z)         #실행인자

x = 5
y = 6
z = -6

print_root(x, y, z)
'''

##매개 변수와 실행인자 이해하기
'''
def print_round(num):
    rounded = round(num)
    print(rounded)

#실행인자에 변수 사용O    
a = 2.4
print_round(a)

#실행인자에 변수 사용X
print_round(4.6)
'''


##함수의 값 반환 받기 (Return)
##Return으로 값을 반환받게 되면 그 즉시 함수를 종료
##Return 아래 코드는 실행되지 않는다.
'''
def add_10(value):
    """value에 10을 더한 값을 반환받는 함수"""
    result = value + 10
    return result

n = add_10(42)
print(n)
'''

#     근의 공식에 return 활용하기
#--------------------------------
def root(a, b, c):    ##매개변수
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return  r1, r2
    ##반환 받을 값이 여러 개일 경우 ,로 구분한다.

r1, r2 = root(1, 2, -8)
##반환 받은 값과 그 값을 담을 변수의 갯수는 동일해야 한다.
print("방정식의 결과는 {}와 {}입니다.".format(r1, r2))