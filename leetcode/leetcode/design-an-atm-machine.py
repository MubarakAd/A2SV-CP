class ATM:
    def __init__(self):
        self.banknotes_count = [0, 0, 0, 0, 0]  
    def deposit(self, banknotes_count):
        for i in range(5):
            self.banknotes_count[i] += banknotes_count[i]

    def withdraw(self, amount):
        withdraw_count = [0, 0, 0, 0, 0]  
        remaining_amount = amount

        for i in range(4, -1, -1):
            num_banknotes = min(remaining_amount // [20, 50, 100, 200, 500][i], self.banknotes_count[i])
            withdraw_count[i] = num_banknotes
            remaining_amount -= num_banknotes * [20, 50, 100, 200, 500][i]

        if remaining_amount == 0:
            for i in range(5):
                self.banknotes_count[i] -= withdraw_count[i]
            return withdraw_count
        else:
            return [-1]