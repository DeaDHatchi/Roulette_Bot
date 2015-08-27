__author__ = 'Travis'
import random


class RouletteTable:
    def __init__(self):

        # Statistics
        self.max_cash = 0
        self.max_cash_list = []
        self.max_bet_count = 0
        self.max_bet_count_list = []

        # Initialized Variables
        self.initial_cash = 1000
        self.cycles = 1
        self.min_bet = 10
        self.selection = "black"

        # Table Config
        self.table = {
            0: "green",
            1: "red",
            2: "black",
            3: "red",
            4: "black",
            5: "red",
            6: "black",
            7: "red",
            8: "black",
            9: "red",
            10: "black",
            11: "black",
            12: "red",
            13: "black",
            14: "red",
            15: "black",
            16: "red",
            17: "black",
            18: "red",
            19: "red",
            20: "black",
            21: "red",
            22: "black",
            23: "red",
            24: "black",
            25: "red",
            26: "black",
            27: "red",
            28: "black",
            29: "black",
            30: "red",
            31: "black",
            32: "red",
            33: "black",
            34: "red",
            35: "black",
            36: "red",
            37: "green"
        }

    def cycle_through(self):
        cycle = self.cycles
        while cycle > 0:
            cycle -= 1
            self.run()
        self.stats()

    def run(self):
        cash = self.initial_cash
        max_cash = 0
        bet_count = 0
        bet = self.min_bet
        while cash > 0:
            x = self.bet()
            if x == "win":
                cash += bet
                bet_count += 1
                bet = self.min_bet
                if cash > max_cash:
                    max_cash = cash
            else:
                cash -= bet
                bet_count += 1
                bet = 2 * bet
            if bet > cash:
                self.max_cash_list.append(max_cash)
                self.max_bet_count_list.append(bet_count)
                if cash > self.max_cash:
                    self.max_cash = cash
                if bet_count > self.max_bet_count:
                    self.max_bet_count = bet_count

    def bet(self):
        x = self.spin()
        if self.selection == x:
            return "win"
        else:
            return "lose"

    def spin(self):
        x = random.randint(0, 37)
        y = self.table[x]
        return y

    def stats(self):
        print("")
        print("-=-=-=- STATISTICS -=-=-=-")
        print("Cycle Count: " + str(self.cycles))
        print("Starting Cash: " + str(self.initial_cash))
        print("Max Cash: " + str(self.max_cash))
        x = 0
        for item in self.max_cash_list:
            x += item
        print("Average Cash: " + str(x/len(self.max_cash_list)))
        print("Max Bet Count: " + str(self.max_bet_count))
        y = 0
        for item in self.max_bet_count_list:
            y += item
        print("Average Bet Count: " + str(y/len(self.max_bet_count_list)))

x = RouletteTable()
x.cycle_through()

