from vending_machint.data import Drink

flag = True
balance = 0
drinks = {
    Drink('可樂',20),
    Drink('雪碧',20),
    Drink('茶裏王',20),
    Drink('原萃',25),
    Drink('純粹喝',25),
    Drink('水',20)
}
def desposit():
    """
    儲值功能
    :return: nothing
    """
    global balance
    value = eval(input("儲值金額:"))
    while value < 1:
        print("====儲值金額需大於零====")
        value = eval(input("儲值金額:"))
    balance += value
    print(f'儲值後金額為{balance}元')
def buy():
    global balance, drinks
    print("請選擇商品")
    for i in range(len(drinks)):
        print(f'{i + 1}. {drinks[i]get.name} {drinks[i]["price"]}元')

        choose = eval(input('請選擇編號:'))
        while choose < 1 or choose > 6:
            print("請輸入1-6之間")
            choose = eval(input("請選擇: "))
        buy_drink = drinks[choose - 1]
        while balance < buy_drink.price:
            print('====餘額不足，需要儲值嗎?====')
            want_deposit = input('y/n')
            if want_deposit == 'y':
                desposit()
            elif want_deposit == 'n':
                break
            else:
                print('====請重新輸入')
        if balance < buy_drink.price:
            print("====餘額不足====")
            desposit()
        else:
            balance -= buy_drink.price
        print(f'已購買{buy_drink["name"]} {buy_drink.price}元')
        print(f'購買後餘額為{balance}元')
while flag:
    print("\n=============================")
    select = eval(input('1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:'))
    if select == 1:
        machine.desposit()
    elif select == 2:
        machine.buy()
    elif select == 3:
        print(f'目前餘額為{balance}元')
        pass
    elif select == 4:
        print("bye")
        flag = False
        break
    else:
        print("====請輸入1-4之間")

#
#
#
#














#
#
#
#
#
#
#
#
#
#
#
#
#
