# lineedit.py

# label.py

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget     # 부모 윈도우 클래스
from PyQt6.QtWidgets import QVBoxLayout # 수직 레이아웃 클래스
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit   # 입력 위젯

# 1. 생성
app = QApplication(sys.argv)
win = QWidget()         # 부모 윈도우 객체
win.resize(300,400)
layout = QVBoxLayout()  # 수직 레이아웃 생성

# 1. 생성
entry = QLineEdit()
label = QLabel()

entry.textChanged.connect(label.setText)
# 2. 배치
layout = QVBoxLayout()
layout.addWidget(entry)    # 레이아웃에 레이블 추가
layout.addWidget(label)
win.setLayout(layout)       # 윈도우에 레이아웃 설정

win.show()
sys.exit(app.exec())
