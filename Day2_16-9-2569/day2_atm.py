sum_money = 1000


def checkMoney():
    global sum_money
    print(f"\nยอดเงินสุทธิ = {sum_money} บาท")


def deposit(money):
    global sum_money
    sum_money += money
    print(f"ฝากเงิน = {money} บาท \nยอดเงินสุทธิ = {sum_money} บาท")


def withDraw(money):
    global sum_money
    if money > sum_money:
        print("ยอดเงินในบัญชีไม่เพียงพอ กรุณาทำรายการใหม่")

    else:
        if money == 0:
            print(f"ไม่สามารถถอนจำนวน {money} บาทได้")
        elif (money % 100) != 0:
            print("ไม่สามารถถอนเป็นเศษได้")
        else:
            sum_money -= money
            print(f"ถอนเงิน = {money} บาท \nยอดเงินสุทธิ = {sum_money} บาท")
            banknote(money)


def banknote(amount):
    notes = [1000, 500, 100]
    print("\n[system] ธนบัตรที่ได้รับ")
    for note in notes:
        count = amount // note
        if count > 0:
            print(f"แบงก์ {note} บาท = {count} ใบ")
            amount %= note


while True:
    choice = int(input(
        "\n======ATM======\n"
        "1.ดูยอดเงิน\n"
        "2.ฝากเงิน\n"
        "3.ถอนเงิน\n"
        "4.ออกจากระบบ\n"
        "กรุณาเลือกการทำรายการ : "
    ))

    if choice == 1:
        checkMoney()
    elif choice == 2:
        deposit(int(input("\nระบุยอดเงินที่ต้องการฝาก : ")))
    elif choice == 3:
        withDraw(int(input("\nระบุยอดเงินที่ต้องการถอน : ")))
    elif choice == 4:
        print("\nขอบคุณที่ใช้บริการ")
        break
    else:
        print("\nเลือกตัวเลือกผิด! กรุณาเลือกใหม่")