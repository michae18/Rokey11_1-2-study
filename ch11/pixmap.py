# pixmap.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QLabel
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtGui import QPixmap

# 1. 생성
app = QApplication(sys.argv)
win = QWidget()
win.resize(200,300)

# 이미지 불러오기
pixmap = QPixmap(r'ch11\apples.jpg')
label = QLabel(win)
label.setPixmap(pixmap)
label.move(-40, -40)
button1 = QPushButton('Push1',win)
button2 = QPushButton('Push2',win)
button3 = QPushButton('Push3',win)

# 2. 배치
button1.move(10,60)
button2.move(140,60)
button3.move(80,10)


win.show()
sys.exit(app.exec())