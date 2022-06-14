mine = "가위"
yours = "바위"

if mine == yours:
    print("비김")
else:
    if mine == "가위":
        if yours == "보":
            print("이겼다")
        else:
            print("졌다")
    else:
        if mine == "바위":
            if yours == "가위":
                print("이겼다")
            else:
                print("졌다")
        else:
            if mine == "보":
                if yours == "바위":
                    print("이겼다")
                else:
                    print("졌다")

#if else 보기 좋게 만들기
a = "가위"
b = "바위"

if a == b:
    print("비겼다.")
elif (a == "가위" and b == "보") or (a == "바위" and b == "가위") or (a == "보" and b == "바위"):
    print("이겼다")
else:
    print("졌다")