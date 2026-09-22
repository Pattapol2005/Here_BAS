account = {
    "123456": {'name': 'กร', 
               'account_num' : "173895" ,
               'money': 3500},

    "654321": {'name': 'บาส', 
               'account_num' : "493857" ,
               'money': 879},

    "001222": {'name': 'ปอนด์', 
               'account_num' : "895345" ,
               'money': 1500},

    "333440": {'name': 'กุน', 
               'account_num' : "852517" ,
               'money': 89},
               
    "755666": {'name': 'ตอง', 
               'account_num' : "345879" ,
               'money': 750}
}

# สำหรับทดสอบ
'''
for data in account.values():
    print("data = " , data )
    print("data['account_num']" , data['account_num'])
'''

account_pass_check = ""


def checkMoney():
    print(f"\nยอดเงินสุทธิ = {account[account_pass_check]['money']} บาท")


def deposit(money):
    if money <= 0:
        print(f"ไม่สามารถฝากจำนวน {money} บาทได้")
    elif money % 100 != 0:
        print("ตู้สามารถรับเงินแบงค์ 1000, 500, 100 ได้เท่านั้น")
    else:
        account[account_pass_check]['money'] += money

        print(f"ฝากเงิน = {money} บาท")
        print(f"ยอดเงินสุทธิ = {account[account_pass_check]['money']} บาท")


def withDraw(money):
    if money <= 0:
        print(f"ไม่สามารถถอนจำนวน {money} บาทได้")
    elif money % 100 != 0:
        print("ไม่สามารถถอนเป็นเศษได้")
    elif money > account[account_pass_check]['money']:
        print("ยอดเงินในบัญชีไม่เพียงพอ กรุณาทำรายการใหม่")
    else:
        account[account_pass_check]['money'] -= money

        print(f"ถอนเงิน = {money} บาท")
        print(f"ยอดเงินสุทธิ = {account[account_pass_check]['money']} บาท")

        banknote(money)

def tranfer(amount , to_acc):
    account_number = []
    for data in account.values():
        
        account_number.append(data['account_num'])
    # 2 ตัวนี้คือตัวเดียวกันแต่จะเขียนแบบย่อกว่า แต่สำหรับเบสิคแนะนำ ตัวที่ 2 เพราะเห็นภาพมากกว่า
    '''
    ( 1 )
    account_number = [data['account_num'] for data in account.values()]

    ( 2 )
    account_number = []
    for data in account.values():
        account_number.append(data['account_num'])
    '''
    to_key = None

    for key, data in account.items():
        if data['account_num'] == to_acc:
            to_key = key

    if to_acc in account_number :
        if (to_acc != account[account_pass_check]['account_num']):
            if amount > 0 :
                if amount <= account[account_pass_check]['money']:
                    print("ยืนยันการโอน")
                    print(f"จาก คุณ{account[account_pass_check]['name']}")
                    print(f"ไปยัง คุณ{account[to_key]['name']}")
                    print(f"จำนวน {amount} บาท")
                    if int(input("ยืนยันกด 1 | ยกเลิกกด 0")) :
                        account[account_pass_check]['money'] -= amount
                        account[to_key]['money'] += amount
                        print("โอนเงินสำเร็จ")
                    else :
                        print("ยกเลิกการโอน")
                else :
                    print(f"ยอดเงินไม่เพียงพอ บัญชีมี {account[account_pass_check]['money']} บาท")
                    print(f"ยอดโอน {amount} บาท ขาดเงิน {amount - account[account_pass_check]['money']} บาท")
            else :
                print("ยอดโอนขั่นต่ำ 0.01 บาท")
        else :
            print("ไม่สามารถโอนเงินเข้าบัญชีของตัวเองได้")
    else :
        print(f"ไม่พบบัญชีปลายทางหมายเลข {to_acc}")

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
        account_pass_check = str(input("\nป้อนรหัสผ่านของคุณ : "))

        if account_pass_check in account:
            print("ยินดีต้อนรับ คุณ" + account[account_pass_check]['name'])
            break

        else:
            print("รหัสผ่านไม่ถูกต้อง กรุณาลองใหม่")

    while True:
        choice = int(input(
            "\n======ATM======"
            "\n1.ดูยอดเงิน"
            "\n2.ฝากเงิน"
            "\n3.ถอนเงิน"
            "\n4.โอนเงิน"
            "\n5.ออกจากระบบ"
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
            acc = str(input("\nป้อนเลขบัญชีที่ต้องการโอน : "))
            if acc != "" :
                amount = int(input("จำนวนเงินที่ต้องการโอน : "))
                tranfer(amount , acc)
            else :
                print("กรุณากรอกเลขบัญชี")


        elif choice == 5:
            print("\nออกจากระบบเรียบร้อย")
            break

        else:
            print("\nเลือกตัวเลือกผิด! กรุณาเลือกใหม่")