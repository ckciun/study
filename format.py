num = 20
greeting = '안녕하세요'
place = 'Python'
welcome = '환영합니다'

## Format 사용X
print("Format 사용X")
print(num,'번 손님', greeting,'.', place,'에 오신것을', welcome,'!')

## Format 사용O
## Format(1)
print("Format 1번 유형")
a = "{}번 손님, {}. {}에 오신것을 {}!"
b = a.format(num, greeting, place, welcome)
print(b)

## Format(2)
print("Format 2번 유형")
print("{}번 손님, {}. {}에 오신것을 {}!".format(num, greeting, place, welcome))

## {}가 format 인자보다 많으면 오류
## format 인자가 {}보다 많으면 오류 발생X
## format 인자가 {}에 순차적으로 대입되기 때문