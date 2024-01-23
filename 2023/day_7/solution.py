from collections import Counter
from dataclasses import dataclass

from utils_anviks.decorators import read_data, stopwatch


@dataclass
class CardHand:
    cards: str
    bid: int
    strength: int = -1


@read_data(sep2=" ")
@stopwatch
def solution(data: list[list[str]], part: int):
    winnings = 0

    hands: list[CardHand] = [CardHand(cards, int(bid)) for cards, bid in data]
    hand_types = ((1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,))
    card_values = "23456789TJQKA" if part == 1 else "J23456789TQKA"

    for hand in hands:
        if part == 1 or 'J' not in hand.cards:
            h_type = sorted(Counter(hand.cards).values())
            hand.strength = hand_types.index(tuple(h_type))
        else:
            potential_hand_values = []
            for cv in card_values[1:]:
                temp_hand = hand.cards.replace("J", cv)
                h_type = sorted(Counter(temp_hand).values())
                potential_hand_values.append(hand_types.index(tuple(h_type)))
            hand.strength = max(potential_hand_values)

    hands.sort(key=lambda _hand: (_hand.strength, tuple(card_values.index(card) for card in _hand.cards)))

    for i in range(len(hands)):
        winnings += (i + 1) * hands[i].bid

    return winnings


if __name__ == '__main__':
    print(solution(1))  # 251121738
    print(solution(2))  # 251421071
