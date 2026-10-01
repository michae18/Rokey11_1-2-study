# layout_qhbox.py

import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout

app = QApplication(sys.argv)
win = QWidget()     # 부모 윈도우 객체
win.resize(300, 200)

button1 = QPushButton("PUSH1", parent=win)  # 자식 위젯 객체
button2 = QPushButton("PUSH2", parent=win)  # 자식 위젯 객체
button3 = QPushButton("PUSH3", parent=win)  # 자식 위젯 객체

# 2. 배치
layout = QGridLayout()
layout.addWidget(button1,0,1)
layout.addWidget(button2,1,0)
layout.addWidget(button3,1,2)
win.setLayout(layout)

win.show()
sys.exit(app.exec())