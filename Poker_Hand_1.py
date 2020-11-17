import itertools
from collections import Counter

# define a class PokerHand


class PokerHand(object):
    def __init__(
            self,
            hand: str) -> None:
        super().__init__()

        # Storage the player's five cards
        self.hand = hand

    # Compare the result
    def compare_with(self, hand1):
        card_list = [self.hand, hand1.hand]
        result = []

        for i in card_list:
            result.append((self._get_result(i)))

        # State the result
        if result.index(max(result)) == 0:
            return ("Win")
        else:
            return ("Loss")

    # This function get result from cards on the hand.
    def _get_result(self, cards):
        # Card value dictionary.
        card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                       "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

        # Values on the hand
        values = [card_values[cards[0]], card_values[cards[3]],
                  card_values[cards[6]], card_values[cards[9]], card_values[cards[12]]]

        # Suits on the hand
        suits = [cards[1], cards[4], cards[7], cards[10], cards[13]]

        # Sorting card values
        values = sorted(values, reverse=True)

        # Check if there is a straight
        straight = (values == list(
            range(values[0], values[0]-5, -1)) or values == [14, 5, 4, 3, 2])

        # Check if there is a flush
        flush = all(s == suits[0] for s in suits)

        # Check if there is a Royal Straight Flush
        if straight and flush and values[0] == 14:
            return 10

        # Check if there is a Straight Flush
        if straight and flush and values[0] != 14:
            return 9

        # Check if there is a Flush
        if flush:
            return 6

        # Check if there is a Straight
        if straight:
            return 5

        dict_group = {}

        # Check how many cards there are.
        for v, group in itertools.groupby(values):
            count = sum(1 for _ in group)
            dict_group[v] = count
        # Check if there is Full House
        if (3 in dict_group.values()) and (2 in dict_group.values()):
            return 7
        # Check if there is Three of a kind
        if (3 in dict_group.values()):
            return 4

        res = Counter(dict_group.values())

        # Check if there is Four of a kind
        if 4 in res.keys():
            return 8

        # Check if there are two pairs
        if 2 in res.keys() and 2 in res.values():
            return 3
        # Check if there is a pair
        if 2 in res.keys() and 1 in res.values():
            return 2
        return 1
