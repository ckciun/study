list1 = [37, 23, 10, 33, 29, 40]
print(list1)

## 리스트에 값 추가하기
## append 활용
print("리스트 맨 뒤에 값 추가하기")
list1.append(16)
print(list1)

## list를 list에 담아서 추가하기
list2 = list1 + [18]
print(list2)

## list 안에 값 확인하기
n = 12
list_check = n in list2
print(list_check)

## if 문 활용하기
n = 18
if n in list2:
    print('{}은(는) list에 있는 값입니다.'.format(n))
    
else:
    print('{}은(는) list에 없는 값입니다.'.format(n))
    
## 리스트에 값 삭제하기

## index를 이용해서 삭제
print("Index를 기준으로 값 삭제")
del(list2[-1])
## del list2[-1] 괄호를 생략해도 동일하게 동작
print(list2)

## list안에 특정 값을 삭제
## 동일한 값이 여러 개일 경우, 가장 앞에 있는 값만 삭제
print("list안에 특정 값을 기준으로 삭제")
list2.remove(33)
print(list2)