
class Player:

    def __init__(self):
        self.hand = [] 
    
    def hand_total(self):
        values = []
        for card in self.hand:
            values.append(card.value)
        total = sum(values)
        if total > 21 and 11 in values:
            i = values.index(11)
            values[i] = 1
            return sum(values)
        return total
