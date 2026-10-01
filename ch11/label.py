# label.py

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget     # 부모 윈도우 클래스
from PyQt6.QtWidgets import QPushButton # 자식 위젯 클래스
from PyQt6.QtWidgets import QVBoxLayout # 수직 레이아웃 클래스
from PyQt6.QtWidgets import QLabel  # 레이블 위젯

# 1. 생성
app = QApplication(sys.argv)
win = QWidget()         # 부모 윈도우 객체
win.resize(300,400)
layout = QVBoxLayout()  # 수직 레이아웃 생성

# 1. 생성
label1  = QLabel('적')  # 레이블 위젯 생성
# setStyleSheet() : Qt 위젯의 모양을 css 유사 문법으로 지정하는 메서드
label1.setStyleSheet('background-color:red; color: white')  # 배경 및 글자 색 설정
label2  = QLabel('녹')  # 자식 위젯 객체
label2.setStyleSheet('background-color:green; color: white')  # 배경색
label3  = QLabel('파')  # 자식 위젯 객체
label3.setStyleSheet('background-color:blue; color: white')  # 배경색

# 2. 배치
layout = QVBoxLayout()
layout.addWidget(label1)    # 레이아웃에 레이블 추가
layout.addWidget(label2)
layout.addWidget(label3)
win.setLayout(layout)       # 윈도우에 레이아웃 설정

win.show()
sys.exit(app.exec())
