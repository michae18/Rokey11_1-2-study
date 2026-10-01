# radio.py

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QRadioButton
from PyQt6.QtWidgets import QVBoxLayout

def order():
    if r_btn1.isChecked():
        print('A 런치 주문')
    elif r_btn2.isChecked():
        print('B 런치 주문')
    elif r_btn3.isChecked():
        print('C 런치 주문')
# 1. 생성
app = QApplication(sys.argv)    # 위젯 관리자 생성
win = QWidget()                 # 배경 위젯 생성


btn1 = QPushButton('주문')      # 버튼 추가
r_btn1 = QRadioButton('A 런치') # 라디오 버튼 추가
r_btn2 = QRadioButton('B 런치')
r_btn3 = QRadioButton('C 런치')

r_btn1.setChecked(True)
# 2. 배치
layout = QVBoxLayout()          
layout.addWidget(r_btn1)        # 구현한 버튼 추가
layout.addWidget(r_btn2)
layout.addWidget(r_btn3)
layout.addWidget(btn1)
win.setLayout(layout)           # 추가한 버튼들 나열


# 3. 이벤트
btn1.clicked.connect(order)     # 버튼 클릭 시 order 함수 실행
win.show()
sys.exit(app.exec())