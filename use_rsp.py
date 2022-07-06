#      가위 바위 보 모듈 사용하기
#--------------------------------
import makes_rsp

selected = makes_rsp.rsp()
print(selected)
print("가위?", makes_rsp.scissor == selected)