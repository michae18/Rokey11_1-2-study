# file_open.py
import os
print('현재 디렉토리 위치:',os.getcwd())

# 파일 객체 = open(경로, 모드)
# 절대경로
# \n = newline
# 읽기 모드:  r
# f = open('C:\rokey\py_work\ch12\file_open.py', 'r')
# # 추가 모드 : a => 파일 마지막에 새로운 내용 추가
# f = open('ch12\file_open.py', 'a')

# 파일 열기 , 쓰기 모드 : w => 새로운 파일 생성, 이미 있는 경우 덮어 씀
f = open('ch12/file1.txt', 'r')
# 파일 닫기
f.close()