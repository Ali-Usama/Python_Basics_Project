class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, d_amount, description=None):
        self.balance += d_amount
        ledger_dict = {}
        if description:
            ledger_dict['amount'] = d_amount
            ledger_dict['description'] = description

        else:
            ledger_dict['amount'] = d_amount
            ledger_dict['description'] = ''

        self.ledger.append(ledger_dict)

    def withdraw(self, w_amount, description=None):
        self.balance -= w_amount
        ledger_dict2 = {}

        if self.balance > w_amount:

            if description is not None:
                ledger_dict2['amount'] = -w_amount
                ledger_dict2['description'] = description


            else:
                ledger_dict2['amount'] = -w_amount
                ledger_dict2['description'] = ''


            self.ledger.append(ledger_dict2)

        else:
            return False

    def get_balance(self):
        return self.balance


    def transfer(self, t_amount, category):

        if self.balance > t_amount:
            self.balance -= t_amount
            category.balance += t_amount

            self.ledger.append(
            {'amount' : -t_amount,
            'description' : f'Transfer to {category.name}'}
            )

            category.ledger.append(
            {'amount': t_amount,
            'description' : f'Transfer from {self.name}'}
            )

        else:
            return False

        def check_funds(self, c_amount):
            if self.balance > c_amount:
                return True

            else:
                return False

        def __str__(self):
            name = self.name.center(30, '*')
            ledger_list = []

            for item in self.ledger:
                amount = format(item['amount'], "7.2f")
                #amount = item['amount'].format('7.2f')
                desc = item['description'][:23]

                ledger_list.append(desc + amount)

            print_lines = '\n'.join(ledger_list)

            total = f'Total : {format(self.balance, "1.2f")}'

            display = name + '\n'+  print_lines + '\n' + total

            return display



def create_spend_chart(cat_list):
    title = 'Percentage spent by category'
    categories = []
    chart = ''
    withdraws = []
    withdraw_percentage = []
    vetical_cats = ''

    #iterating through cat_list:
    for category in cat_list:
        categories.append(category.name)

        withdrawn_amount = 0

        for action in category.ledger:
            if action['amount'] < 0:
                withdrawn_amount -= action['amount']

        withdraws.append(withdrawn_amount)


    # calculating the percentage for each number:
    for i in range(len(withdraws)):
        withdraw_percentage.append(withdraws[i]/sum(withdraws) * 100)


    # Building the y -axis:
    for i in range(100, -10, -10):
        chart += str(i).rjust(3, ' ') + '|'

        for num in withdraw_percentage:
            if num >= i:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'

    # Building the x-axis:

    chart += '    ' + '-' * len(categories) * 3 + '-' + '\n'

    #longest category name is:
    longest = max(len(name.name) for name in cat_list)

    for level in range(longest):

        vetical_cats += '    '

        for name in cat_list:
            if level < len(name.name):
                vetical_cats += ' ' + name.name[level] + ' '
            else:
                vetical_cats += '   '

        vetical_cats += ' \n'


    chart += vetical_cats.rstrip() + '  '

    display = title + '\n' + chart
    return display
















food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
print(food.get_balance())
print(food)

clothing = Category('Clothing')
food.transfer(50, clothing)
print('food balance after transfer: ', food.get_balance())
print('clothing balance after transfer: ', clothing.get_balance())

print(create_spend_chart([food,clothing]))
