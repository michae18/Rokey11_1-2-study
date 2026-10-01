# checkbox.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QCheckBox
from PyQt6.QtWidgets import QVBoxLayout


def order():
    select_items = []
    if chk1.isChecked():
        select_items.append('아메리카노')
    if chk2.isChecked():
        select_items.append('라떼')
    if chk3.isChecked():
        select_items.append('카푸치노')
    if chk3.isChecked():
        select_items.append('에스프레소')

    if select_items:
        print('주문 내역:',select_items)
    else:
        print('주문한 것이 없습니다')
# 1. 생성
app = QApplication(sys.argv)
win = QWidget()

chk1 = QCheckBox('아메리카노')
chk2 = QCheckBox('라떼')
chk3 = QCheckBox('카푸치노')
chk4 = QCheckBox('에스프레소')
btn1 = QPushButton('주문')

# 2. 배치
layout = QVBoxLayout()
layout.addWidget(chk1)
layout.addWidget(chk2)
layout.addWidget(chk3)
layout.addWidget(chk4)
layout.addWidget(btn1)
win.setLayout(layout)

btn1.clicked.connect(order)

# 3. 출력
win.show()
sys.exit(app.exec())
