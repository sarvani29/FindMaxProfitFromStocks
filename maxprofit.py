class MaxProfit:

    def maxProfit(self):
        if len(self) == 0:
            return 0

        profit = 0
        cheapest = self[0]
        message = ""

        for i in range(1, len(self)):
            cheapest = min(cheapest, self[i])
            profit = max(profit, self[i] - cheapest)
            buy = self[i]
            sell = cheapest
            message = f'with a Buying price of {buy} and Selling price of {sell}'
        return profit, message


