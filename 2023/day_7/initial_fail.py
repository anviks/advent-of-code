from utils_anviks.decorators import read_data
from functools import total_ordering


@total_ordering
class Card:
    card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, value: str):
        if value in Card.card_values:
            self.value = value
        else:
            raise ValueError(f"{value} isn't a valid card.")

    def __eq__(self, other):
        return type(other) is Card and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        return Card.card_values.index(self.value) > Card.card_values.index(other.value)


@total_ordering
class CardHand:
    def __init__(self, cards: list[Card], bid: int):
        self.cards = cards
        self.bid = bid

    @property
    def strength(self) -> int:
        card_counts = []
        for card in set(self.cards):
            card_counts.append(self.cards.count(card))

        if card_counts == [5]:
            return 6
        elif 4 in card_counts:
            return 5
        elif 3 in card_counts:
            return 4 if 2 in card_counts else 3
        elif card_counts.count(2) == 2:
            return 2
        elif 2 in card_counts:
            return 1
        else:
            return 0

    def __eq__(self, other):
        return type(other) is CardHand and self.strength == other.strength and self.cards == other.cards

    def __lt__(self, other):
        if self.strength < other.strength:
            return True
        if self.strength == other.strength:
            for card1, card2 in zip(self.cards, other.cards):
                if card1 == card2:
                    continue
                return card1 < card2

        return False


@read_data(sep2=" ")
def solution(data: list[list[str]], part: int):
    hands = []
    winnings = 0

    for cards_string, bid in data:
        cards = list(map(Card, cards_string))
        hands.append(CardHand(cards, int(bid)))

    hands.sort()

    for i in range(len(hands)):
        winnings += hands[i].bid * (i + 1)

    return winnings


if __name__ == '__main__':
    print(solution(1))  # 251121738
    print(solution(2))
    print(Card.card_values)
