sum_money = 100

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
        print(f"\nยอดเงินสุทธิ = {sum_money} บาท")
    elif choice == 2:
        deposit = int(input("\nระบุยอดเงินที่ต้องการฝาก : "))
        sum_money += deposit
        print(
            f"ฝากเงิน = {deposit} บาท "
            f"\nยอดเงินสุทธิ = {sum_money} บาท"
        )
    elif choice == 3:
        withdraw = int(input("\nระบุยอดเงินที่ต้องการถอน : "))

        if withdraw > sum_money:
            print("ยอดเงินในบัญชีไม่เพียงพอ กรุณาทำรายการใหม่")
        else:
            sum_money -= withdraw
            print(
                f"ถอนเงิน = {withdraw} บาท "
                f"\nยอดเงินสุทธิ = {sum_money} บาท"
            )
    elif choice == 4:
        print("\nขอบคุณที่ใช้บริการ")
        break
    else:
        print("\nเลือกตัวเลือกผิด! กรุณาเลือกใหม่")