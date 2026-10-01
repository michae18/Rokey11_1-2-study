# combobox.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout,QLabel, QPushButton

# 1.생성
app = QApplication(sys.argv)
win = QWidget()
win.resize(300,200)

# option_list1 = ['Option1', 'Otion2', 'Option3']
option_list = ['학생', '공무원', '전문직', '사무직']

# 2. 배치
combo = QComboBox()
label = QLabel('현재 직업을 선택하시오')
btn = QPushButton('선택')
combo.addItems(option_list)

def job_changed():
    selected = combo.currentText()
    print(selected)    

combo.currentTextChanged.connect(job_changed)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(combo)
layout.addWidget(btn)

win.setLayout(layout)
win.show()
sys.exit(app.exec())