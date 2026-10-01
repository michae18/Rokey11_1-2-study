import tkinter as tk
from tkinter import messagebox


# -------------------------
# 주문 처리 함수
# -------------------------
def order_pizza():
    total_price = 10
    order_list = []

    try:
        pepperoni_count = int(pepperoni_entry.get())
        cheese_count = int(cheese_entry.get())
        bulgogi_count = int(bulgogi_entry.get())

        if pepperoni_count < 0 or cheese_count < 0 or bulgogi_count < 0:
            messagebox.showwarning("입력 오류", "수량은 0 이상이어야 합니다.")
            return

    except ValueError:
        messagebox.showwarning("입력 오류", "수량은 숫자로 입력해주세요.")
        return

    # 페퍼로니 피자
    if pepperoni_count > 0:
        price = pepperoni_count * 3500
        total_price += price
        order_list.append(
            f"페퍼로니 피자 {pepperoni_count}조각 : {price:,}원"
        )

    # 치즈 피자
    if cheese_count > 0:
        price = cheese_count * 3000
        total_price += price
        order_list.append(
            f"치즈 피자 {cheese_count}조각 : {price:,}원"
        )

    # 불고기 피자
    if bulgogi_count > 0:
        price = bulgogi_count * 4000
        total_price += price
        order_list.append(
            f"불고기 피자 {bulgogi_count}조각 : {price:,}원"
        )

    if total_price == 0:
        messagebox.showinfo("주문 확인", "피자를 1조각 이상 선택해주세요.")
        return

    result = "\n".join(order_list)
    result += f"\n\n총 금액 : {total_price:,}원"

    result_label.config(text=result)


# -------------------------
# 초기화 함수
# -------------------------
def reset_order():
    pepperoni_entry.delete(0, tk.END)
    pepperoni_entry.insert(0, "0")

    cheese_entry.delete(0, tk.END)
    cheese_entry.insert(0, "0")

    bulgogi_entry.delete(0, tk.END)
    bulgogi_entry.insert(0, "0")

    result_label.config(text="주문 내역이 여기에 표시됩니다.")


# -------------------------
# 메인 창
# -------------------------
window = tk.Tk()

window.title("조각 피자 주문 프로그램")
window.geometry("450x500")


# 제목
title_label = tk.Label(
    window,
    text="🍕 조각 피자 주문",
    font=("맑은 고딕", 20, "bold")
)

title_label.pack(pady=20)


# -------------------------
# 피자 메뉴
# -------------------------
menu_frame = tk.Frame(window)
menu_frame.pack(pady=10)


# 페퍼로니
pepperoni_label = tk.Label(
    menu_frame,
    text="페퍼로니 피자 (3,500원)",
    font=("맑은 고딕", 12)
)
pepperoni_label.grid(row=0, column=0, padx=10, pady=10)

pepperoni_entry = tk.Entry(
    menu_frame,
    width=5,
    justify="center"
)
pepperoni_entry.insert(0, "0")
pepperoni_entry.grid(row=0, column=1)


# 치즈
cheese_label = tk.Label(
    menu_frame,
    text="치즈 피자 (3,000원)",
    font=("맑은 고딕", 12)
)
cheese_label.grid(row=1, column=0, padx=10, pady=10)

cheese_entry = tk.Entry(
    menu_frame,
    width=5,
    justify="center"
)
cheese_entry.insert(0, "0")
cheese_entry.grid(row=1, column=1)


# 불고기
bulgogi_label = tk.Label(
    menu_frame,
    text="불고기 피자 (4,000원)",
    font=("맑은 고딕", 12)
)
bulgogi_label.grid(row=2, column=0, padx=10, pady=10)

bulgogi_entry = tk.Entry(
    menu_frame,
    width=5,
    justify="center"
)
bulgogi_entry.insert(0, "0")
bulgogi_entry.grid(row=2, column=1)


# -------------------------
# 버튼
# -------------------------
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

order_button = tk.Button(
    button_frame,
    text="주문하기",
    width=12,
    command=order_pizza
)
order_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(
    button_frame,
    text="초기화",
    width=12,
    command=reset_order
)
reset_button.grid(row=0, column=1, padx=10)


# -------------------------
# 주문 결과
# -------------------------
result_label = tk.Label(
    window,
    text="주문 내역이 여기에 표시됩니다.",
    font=("맑은 고딕", 11),
    justify="left"
)

result_label.pack(pady=20)


# 프로그램 실행
window.mainloop()