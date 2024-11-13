class TradingStrategy:
    def __init__(self):
        self.position = None  # None, 'LONG', 'SHORT'
        self.entry_price = 0.0
        self.reward = 0.0

    def buy(self, price):
        if self.position == 'SHORT':
            self.reward += price - self.entry_price  # закрытие SHORT
            self.position = None  # кроме позиции закрываем SHORT
        elif self.position is None:
            self.position = 'LONG'
            self.entry_price = price
            self.reward += 1  # поощрение за открытие LONG

    def sell(self, price):
        if self.position == 'LONG':
            self.reward += price - self.entry_price  # закрытие LONG
            self.position = None  # закрываем LONG
        elif self.position is None:
            self.position = 'SHORT'
            self.entry_price = price
            self.reward += 1  # поощрение за открытие SHORT

    def hold(self):
        self.reward += 0.5  # поощрение за HOLD

    def get_reward(self):
        return self.reward


# Пример использования
environment = TradingStrategy()
environment.buy(100)  # BUY на цене 100
environment.hold()  # HOLD
environment.sell(110)  # SELL на цене 110 (закрытие LONG)
print("Total Reward:", environment.get_reward())
