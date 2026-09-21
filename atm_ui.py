import tkinter as tk
from tkinter import messagebox

# =========================
# ข้อมูลบัญชี
# =========================
account = {
    173895: {'name': 'กร', 'money': 3500},
    493857: {'name': 'บาส', 'money': 879},
    895345: {'name': 'ปอนด์', 'money': 1500},
    852517: {'name': 'กุน', 'money': 89},
    345879: {'name': 'ตอง', 'money': 750}
}

account_pass_check = None


# =========================
# ฟังก์ชัน
# =========================

def login():
    global account_pass_check

    password = entry.get()

    if not password.isdigit():
        messagebox.showerror("แจ้งเตือน", "กรุณากรอกรหัสเป็นตัวเลข")
        return

    password = int(password)

    if password in account:
        account_pass_check = password

        screen.config(
            text=f"ยินดีต้อนรับ คุณ{account[password]['name']}\n"
                 f"กรุณาเลือกทำรายการ"
        )

        entry.delete(0, tk.END)

        login_btn.pack_forget()
        transaction_frame.pack(pady=10)

    else:
        messagebox.showerror(
            "รหัสไม่ถูกต้อง",
            "รหัสผ่านไม่ถูกต้อง กรุณาลองใหม่"
        )

        entry.delete(0, tk.END)


def check_money():
    money = account[account_pass_check]['money']

    screen.config(
        text=f"ยอดเงินคงเหลือ\n\n{money:,} บาท"
    )


def deposit():
    amount = entry.get()

    if not amount.isdigit():
        messagebox.showerror(
            "แจ้งเตือน",
            "กรุณาระบุจำนวนเงิน"
        )
        return

    amount = int(amount)

    if amount <= 0:
        screen.config(
            text=f"ไม่สามารถฝากจำนวน {amount} บาทได้"
        )

    elif amount % 100 != 0:
        screen.config(
            text="ตู้สามารถรับธนบัตร\n"
                 "1000, 500 และ 100 บาทเท่านั้น"
        )

    else:
        account[account_pass_check]['money'] += amount

        screen.config(
            text=f"ฝากเงินสำเร็จ\n\n"
                 f"ฝากเงิน = {amount:,} บาท\n"
                 f"ยอดเงินสุทธิ = "
                 f"{account[account_pass_check]['money']:,} บาท"
        )

    entry.delete(0, tk.END)


def withdraw():
    amount = entry.get()

    if not amount.isdigit():
        messagebox.showerror(
            "แจ้งเตือน",
            "กรุณาระบุจำนวนเงิน"
        )
        return

    amount = int(amount)

    if amount <= 0:
        screen.config(
            text=f"ไม่สามารถถอนจำนวน {amount} บาทได้"
        )

    elif amount % 100 != 0:
        screen.config(
            text="ไม่สามารถถอนเป็นเศษได้\n"
                 "กรุณาระบุจำนวนที่หารด้วย 100 ลงตัว"
        )

    elif amount > account[account_pass_check]['money']:
        screen.config(
            text="ยอดเงินในบัญชีไม่เพียงพอ\n"
                 "กรุณาทำรายการใหม่"
        )

    else:
        account[account_pass_check]['money'] -= amount

        notes = banknote(amount)

        screen.config(
            text=f"ถอนเงินสำเร็จ\n\n"
                 f"ถอนเงิน = {amount:,} บาท\n"
                 f"ยอดเงินสุทธิ = "
                 f"{account[account_pass_check]['money']:,} บาท\n\n"
                 f"{notes}"
        )

    entry.delete(0, tk.END)


def banknote(amount):
    notes = [1000, 500, 100]

    result = "ธนบัตรที่ได้รับ\n"

    for note in notes:
        count = amount // note

        if count > 0:
            result += f"แบงก์ {note:,} บาท = {count} ใบ\n"
            amount %= note

    return result


def logout():
    global account_pass_check

    account_pass_check = None

    transaction_frame.pack_forget()
    login_btn.pack(pady=10)

    entry.delete(0, tk.END)

    screen.config(
        text="ATM\n\nกรุณาป้อนรหัสผ่าน"
    )


def clear_entry():
    entry.delete(0, tk.END)


def add_number(number):
    entry.insert(tk.END, number)


# =========================
# สร้างหน้าต่าง
# =========================

root = tk.Tk()

root.title("ATM")
root.geometry("500x650")
root.resizable(False, False)

# =========================
# หัวข้อ
# =========================

title = tk.Label(
    root,
    text="ATM",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)


# =========================
# หน้าจอ ATM
# =========================

screen = tk.Label(
    root,
    text="ATM\n\nกรุณาป้อนรหัสผ่าน",
    font=("Arial", 16),
    width=35,
    height=8,
    bg="black",
    fg="lime",
    relief="sunken"
)
screen.pack(pady=10)


# =========================
# ช่องกรอกข้อมูล
# =========================

entry = tk.Entry(
    root,
    font=("Arial", 20),
    justify="center",
    width=20
)
entry.pack(pady=10)


# =========================
# ปุ่มตัวเลข
# =========================

number_frame = tk.Frame(root)
number_frame.pack()

buttons = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["C", "0", "←"]
]

for row in buttons:

    row_frame = tk.Frame(number_frame)
    row_frame.pack()

    for text in row:

        if text == "C":
            command = clear_entry

        elif text == "←":
            command = lambda: entry.delete(
                len(entry.get()) - 1,
                tk.END
            )

        else:
            command = lambda n=text: add_number(n)

        btn = tk.Button(
            row_frame,
            text=text,
            width=7,
            height=2,
            font=("Arial", 14),
            command=command
        )

        btn.pack(side="left", padx=3, pady=3)


# =========================
# ปุ่ม Login
# =========================

login_btn = tk.Button(
    root,
    text="เข้าสู่ระบบ",
    width=20,
    height=2,
    font=("Arial", 14),
    command=login
)

login_btn.pack(pady=10)


# =========================
# เมนู ATM
# =========================

transaction_frame = tk.Frame(root)

check_btn = tk.Button(
    transaction_frame,
    text="ดูยอดเงิน",
    width=12,
    height=2,
    command=check_money
)
check_btn.grid(row=0, column=0, padx=5, pady=5)


deposit_btn = tk.Button(
    transaction_frame,
    text="ฝากเงิน",
    width=12,
    height=2,
    command=deposit
)
deposit_btn.grid(row=0, column=1, padx=5, pady=5)


withdraw_btn = tk.Button(
    transaction_frame,
    text="ถอนเงิน",
    width=12,
    height=2,
    command=withdraw
)
withdraw_btn.grid(row=1, column=0, padx=5, pady=5)


logout_btn = tk.Button(
    transaction_frame,
    text="ออกจากระบบ",
    width=12,
    height=2,
    command=logout
)
logout_btn.grid(row=1, column=1, padx=5, pady=5)


# =========================
# เริ่มโปรแกรม
# =========================

root.mainloop()