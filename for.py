#          for in 반복문
#--------------------------------
# patterns = ['가위', '보', '보', '바위', '바위', '가위', '보']
# for pattern in patterns:
# pattern 변수는 명시되어 있지 않지만, for문에 의해 생성되어진 변수이다
    # """
    # for 반복문을 사용하지 않고 위 list의 값을 하나씩 전부 출력하려면
    # pattern = patterns[0]
    # print(pattern)
    # pattern = patterns[1]
    # print(pattern)
    # pattern = patterns[2]
    # print(pattern)
    # pattern = patterns[3]
    # print(pattern)
    # ...
    # 이런 작업을 해야한다.
    # """
    # print(pattern)
    
#           for range
#--------------------------------
## for in 반복문으로 [0, 1, 2, 3, 4] 출력하기
# print("for in 반복문으로 0~4 출력")
# count = [0, 1, 2, 3, 4]
# for i in count:
#     print(i)
    
## # for range 반복문으로 같은 결과 출력하기
# print("for range로 위와 같은 결과 출력하기")
# for i in range(5):
#     print(i)

## 이름에 번호 붙이기
# names = ['재석', '명수', '준하', '형돈','홍철','하하']

# for i in range(6):
#     name = names[i]
#     print('{}번: {}'.format(i + 1, name))
    
## 이름이 늘어날 때마다 range의 숫자를 늘리기 번거로우니 len 함수 이용
names = ['재석', '명수', '준하', '형돈','홍철','하하', '세호']
print("range 활용")
for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i + 1, name))
    
## 순서와 list 안의 값을 동시에 반환해주는 enumerate 활용
print("enumerate 활용")
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))