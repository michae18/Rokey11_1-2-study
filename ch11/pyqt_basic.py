# pyqt_basic.py

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
import sys
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout

app = QApplication(sys.argv)
# 1. 생성
win = QWidget()     # 부모 윈도우 객체

# x = 100, y = 100 위치에 너비 = 400, 높이 = 300 크기로 창 설정
win.setGeometry(100, 100, 400, 300)

# 1. 크기 조절 (가로 800px , 세로 600px)
win.resize(800,600)

# 2. 위치 이동(모니터 화면의)
# win.move(100, 200)

button = QPushButton("클릭", parent=win)  # 자식 위젯 객체

# # 2. 배치
layout = QVBoxLayout()
layout.addWidget(button)
win.setLayout(layout)

win.show()
sys.exit(app.exec())

print('---------------------------')
# # 1. 생성
# win = QWidget()     # 부모 윈도우 객체
# button = QPushButton("클릭", parent=win)

# # 2. 배치
# layout = QVBoxLayout()
# layout.addWidget(button)
# win.setLayout(layout)     # 수직 배치


# # 3. 이벤트 처리
# def on_click_event(self):
#     print('버튼 클릭!')
# button.clicked.connect(on_click_event)

on_click