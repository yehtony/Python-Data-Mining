import msvcrt

customers = {}


def customerExist(name):
    while not name in customers.keys():
        print(
            'Customer not exist! Please type customer\'s name again or \'Esc\' to exit.\nCustomer\'s name: ', end='')
        msvcrt.kbhit()
        key_stroke = msvcrt.getche()
        if key_stroke == chr(27).encode():
            print('\\', end="")
            return False
        else:
            name = str(key_stroke).split("'")[1]+input()
    return name


def checkMoney(money):
    try:
        val = int(money)
        if val >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def depositWithdrawMoney(name, act, money):
    if act == 'D':
        customers[name] += money
        print('Deposit successfully!')
    elif act == 'W':
        if customers[name] - money < 0:
            money = input(
                'Balance is insufficient! Please type money again:\nHow much money: ')
            while checkMoney(money) == False:
                money = input(
                    "Input error! Please type money again:\nHow much money: ")
            money = int(money)
            customers[name] -= money
        else:
            customers[name] -= money
        print('Withdraw successfully!')
    return money


def createCustomers():
    while True:
        print('Customer\'s name: ', end='')
        msvcrt.kbhit()
        key_stroke = msvcrt.getche()
        if key_stroke == chr(27).encode():
            print('\\')
            return
        else:
            name = str(key_stroke).split("'")[1]+input()
            if name not in customers.keys():
                money = input('Customer\'s money: ')
                while checkMoney(money) == False:
                    money = input(
                        "Input error! Please type customer's money again:\nMoney: ")
                money = int(money)
                customer = {name: money}
                customers.update(customer)
            else:
                print(
                    'Customer has already exist! Please type customer\'s name again or \'Esc\' to exit.')


def dealCustomerMoney():
    while True:
        print('Customer\'s name: ', end='')
        msvcrt.kbhit()
        key_stroke = msvcrt.getche()
        if key_stroke == chr(27).encode():
            print('\\')
            return
        else:
            nametemp = str(key_stroke).split("'")[1]+input()
            name = customerExist(nametemp)
            if name == False:
                return
            act = input(
                'Press (D) to deposit money or (W) to withdraw money: ')
            while act != "D" and act != "W":
                act = input(
                    "Input error! Please type again:\nPress (D) to deposit money or (W) to withdraw money: ")
            money = input('How much money: ')
            while checkMoney(money) == False:
                money = input(
                    "Input error! Please type money again:\nHow much money: ")
            money = int(money)
            depositWithdrawMoney(name, act, money)
            print(name, ":", customers[name])


def transferCustomersMoney():
    while True:
        print('Customer transfer: ', end='')
        msvcrt.kbhit()
        key_stroke = msvcrt.getche()
        if key_stroke == chr(27).encode():
            print('\\')
            return
        else:
            nametemp1 = str(key_stroke).split("'")[1]+input()
            name1 = customerExist(nametemp1)
            if name1 == False:
                return
            name2 = input('Customer be transfered: ')
            while not name2 in customers.keys() or name2 == name1:
                if name2 == name1:
                    print(
                        'Same customer! Please type customer\'s name again or \'Esc\' to exit:\nCustomer be tranfered: ', end='')
                else:
                    print(
                        'Customer not exist! Please type customer\'s name again or \'Esc\' to exit:\nCustomer be tranfered: ', end='')
                msvcrt.kbhit()
                key_stroke = msvcrt.getche()
                if key_stroke == chr(27).encode():
                    print('\\', end="")
                    return
                else:
                    name2 = str(key_stroke).split("'")[1]+input()
            money = input('How much money to transfer: ')
            while checkMoney(money) == False:
                money = input(
                    "Input error! Please type money again:\nHow much money: ")
            money = int(money)
            money = depositWithdrawMoney(name1, 'W', money)
            depositWithdrawMoney(name2, 'D', money)
            print(name1, ':', customers[name1],
                  ',', name2, ':', customers[name2])


def removeCustomer():
    while True:
        print('Customer\'s name: ', end='')
        msvcrt.kbhit()
        key_stroke = msvcrt.getche()
        if key_stroke == chr(27).encode():
            print('\\')
            return
        else:
            name = str(key_stroke).split("'")[1]+input()
            if name in customers.keys():
                del customers[name]
            else:
                print(
                    'Customer has not exist! Please type customer\'s name again or \'Esc\' to exit.')


def main():
    print('Hello, welcome back to customer\'s manage system!')
    while True:
        key = input('Press corresponding key to use the function: \n(1) Create customers and corresponding money. \n(2) Check all customers\' account balance. \n(3) Choose the customer to deposit or withdraw money.\n(4) Choose the customers to transfer money.\n(5) Remove the customers\n')
        match key:
            case '1':
                print(
                    'Create customers and corresponding money. Press \'Esc\' to exit.')
                createCustomers()
                print(customers)
            case '2':
                print('All customers\' account balance:\n' + str(customers))
            case '3':
                print(
                    'Choose a customer to deposit or withdraw money. Press \'Esc\' to exit.')
                print(customers)
                dealCustomerMoney()
            case '4':
                print('Choose two customers to transfer money. Press \'Esc\' to exit.')
                print(customers)
                transferCustomersMoney()
            case '5':
                print(
                    'Choose a customer to remove. Press \'Esc\' to exit.')
                print(customers)
                removeCustomer()
                print(customers)

            case _:
                print('key incorrect! Please try again.')
        print('--------------------------------------------------------')


main()