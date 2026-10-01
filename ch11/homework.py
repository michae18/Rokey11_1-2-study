# homework.py
# 5. PyQt6 모듈의 QApplication과 QWidget 클래스를 사용하여 
# 기본 윈도우 객체를 생성하고 실행하는 코드를 작성하시오
# import sys
# from PyQt6.QtWidgets import QApplication,QWidget

# app = QApplication(sys.argv)
# win = QWidget()

# win.show()
# sys.exit(app.exec())

# 6. 앞서 생성한 윈도우 객체의 크기를 400x300으로 설정하고, 
# 제목을 “조각 피자 주문 프로그램”으로 작성하시오.
# import sys
# from PyQt6.QtWidgets import QApplication,QWidget
# from PyQt6.QtWidgets import QLabel,QVBoxLayout
# # 1. 생성
# app = QApplication(sys.argv)
# win = QWidget()
# win.resize(400,300)

# # 2. 배치
# label1 = QLabel("조각 피자 주문 프로그램")

# layout = QVBoxLayout()
# layout.addWidget(label1)
# win.setLayout(layout)

# win.show()
# sys.exit(app.exec())

# 7. 앞서 생성한 윈도우 객체에 “피자” 레이블을 추가하시오.
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
# from PyQt6.QtWidgets import QVBoxLayout, QLabel

# app = QApplication(sys.argv)
# win = QWidget()
# win.resize(400,300)

# label1 = QLabel('조각 피자 주문 프로그램')
# label2 = QLabel('피자')

# layout = QVBoxLayout()
# layout.addWidget(label1)
# layout.addWidget(label2)

# win.setLayout(layout)
# win.show()
# sys.exit(app.exec())
print('8---------------------------------')
# 8. 앞서 생성한 윈도우 객체에 다음과 같이 피자 메뉴를 체크박스(QCheckBox)와 함께 추가하시오.
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
# from PyQt6.QtWidgets import QLabel,QCheckBox,QVBoxLayout

# # 1. 생성
# app = QApplication(sys.argv)
# win = QWidget()
# win.resize(400,300)

# label1 = QLabel('조각 피자 주문 프로그램')
# label2 = QLabel('피자')

# chk1 = QCheckBox('페페로니 피자')
# chk2 = QCheckBox('포테이토 피자')
# chk3 = QCheckBox('디럭스 피자')

# layout = QVBoxLayout()
# layout.addWidget(label1)
# layout.addWidget(label2)
# layout.addWidget(chk1)
# layout.addWidget(chk2)
# layout.addWidget(chk3)

# win.setLayout(layout)
# win.show()
# sys.exit(app.exec())

# # 9. 앞서 생성한 윈도우 객체에 주문 버튼(QPushButton)을 추가하시오.
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
# from PyQt6.QtWidgets import QLabel,QCheckBox,QPushButton,QVBoxLayout
    
# app = QApplication(sys.argv)
# win = QWidget()
# win.resize(400,300)

# label1 = QLabel('조각 피자 주문 프로그램')
# label2 = QLabel('피자')

# chk1 = QCheckBox('페페로니 피자')
# chk2 = QCheckBox('포테이토 피자')
# chk3 = QCheckBox('디럭스 피자')

# btn = QPushButton('주문 버튼')

# layout = QVBoxLayout()
# layout.addWidget(label1)
# layout.addWidget(label2)
# layout.addWidget(chk1)
# layout.addWidget(chk2)
# layout.addWidget(chk3)
# layout.addWidget(btn)

# win.setLayout(layout)
# win.show()
# sys.exit(app.exec())


print('10-----------------------------------------------')
# 10. 앞서 생성한 윈도우 객체에 주문 버튼 클릭 시 체크된 
# 피자의 내역과 총 가격을 표시하는 동작 사항을 추가하시오.
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel,QCheckBox,QPushButton,QVBoxLayout

def order():
    select_pizza = []
    total_price = 0
    if chk1.isChecked():
        select_pizza.append('페페로니 피자')
        total_price += 3000
    if chk2.isChecked():
        select_pizza.append('포테이토 피자')
        total_price += 3500
    if chk3.isChecked():
        select_pizza.append('디럭스 피자')
        total_price += 4000

    if select_pizza:
        print('주문내역',select_pizza, total_price,'원')
    else:
        print('주문 내역이 없습니다')
    
app = QApplication(sys.argv)
win = QWidget()
win.resize(400,300)

label1 = QLabel('조각 피자 주문 프로그램')
label2 = QLabel('피자')

chk1 = QCheckBox('페페로니 피자')
chk2 = QCheckBox('포테이토 피자')
chk3 = QCheckBox('디럭스 피자')

btn = QPushButton('주문 버튼')

layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(chk1)
layout.addWidget(chk2)
layout.addWidget(chk3)
layout.addWidget(btn)

btn.clicked.connect(order)

win.setLayout(layout)
win.show()
sys.exit(app.exec())
