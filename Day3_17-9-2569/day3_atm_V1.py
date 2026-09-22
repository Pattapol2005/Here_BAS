sum_money =    {173895: 3500 , 493857: 879 , 895345:  1500 , 852517:   89 , 345879: 750}
account_pass = {173895: 'กร', 493857: 'บาส', 895345: 'ปอนด์', 852517: 'กุน', 345879: 'ตอง'}

account_pass_check = 0


def checkMoney():
    print(f"\nยอดเงินสุทธิ = {sum_money[account_pass_check]} บาท")


def deposit(money):
    if money <= 0:
        print(f"ไม่สามารถฝากจำนวน {money} บาทได้")

    elif money % 100 != 0:
        print("ตู้สามารถรับเงินแบงค์ 1000, 500, 100 ได้เท่านั้น")

    else:
        sum_money[account_pass_check] += money
        print(f"ฝากเงิน = {money} บาท")
        print(f"ยอดเงินสุทธิ = {sum_money[account_pass_check]} บาท")


def withDraw(money):
    if money <= 0:
        print(f"ไม่สามารถถอนจำนวน {money} บาทได้")

    elif money % 100 != 0:
        print("ไม่สามารถถอนเป็นเศษได้")

    elif money > sum_money[account_pass_check]:
        print("ยอดเงินในบัญชีไม่เพียงพอ กรุณาทำรายการใหม่")

    else:
        sum_money[account_pass_check] -= money
        print(f"ถอนเงิน = {money} บาท")
        print(f"ยอดเงินสุทธิ = {sum_money[account_pass_check]} บาท")

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
    print("\nธนาคารเหี้ยบาสยินดีต้อนรับ")

    while True:
        account_pass_check = int(input("\nป้อนรหัสผ่านของคุณ : "))
        if account_pass_check in account_pass:
            print("ยินดีต้อนรับ คุณ" + account_pass[account_pass_check])
            break
        else:
            print("รหัสผ่านไม่ถูกต้อง กรุณาลองใหม่")

    while True:
        choice = int(input(
            "\n======ATM======"
            "\n1.ดูยอดเงิน"
            "\n2.ฝากเงิน"
            "\n3.ถอนเงิน"
            "\n4.ออกจากระบบ"
            "\nกรุณาเลือกการทำรายการ : "
        ))

        if choice == 1:
            checkMoney()

        elif choice == 2:
            money = int(input("\nระบุยอดเงินที่ต้องการฝาก : "))
            deposit(money)

        elif choice == 3:
            money = int(input("\nระบุยอดเงินที่ต้องการถอน : "))
            withDraw(money)

        elif choice == 4:
            print("\nออกจากระบบเรียบร้อย")
            break

        else:
            print("\nเลือกตัวเลือกผิด! กรุณาเลือกใหม่")