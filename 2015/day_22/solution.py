from collections import deque

from utils_anviks import stopwatch

spells = {
    #              (cost, damage, +hp, +armor, +mana, turns)
    'Magic Missile': (53,      4,   0,      0,     0,     1),
    'Drain':         (73,      2,   2,      0,     0,     1),
    'Shield':       (113,      0,   0,      7,     0,     6),
    'Poison':       (173,      3,   0,      0,     0,     6),
    'Recharge':     (229,      0,   0,      0,   101,     5),
}


@stopwatch
def solve(part: int):
    best_cost = float('inf')
    possible_outcomes = deque([({}, (50, 0, 500, 0), (71, 10), True)])

    while possible_outcomes:
        active_spells, (hp, armour, mana, running_cost), (boss_hp, boss_damage), player_turn = possible_outcomes.popleft()

        if part == 2 and player_turn:
            hp -= 1

        if running_cost >= best_cost or hp <= 0:
            continue

        for spell, remaining_turns in list(active_spells.items()):
            _, spell_damage, bonus_hp, bonus_armour, bonus_mana, _ = spells[spell]
            boss_hp -= spell_damage
            mana += bonus_mana
            active_spells[spell] -= 1
            if active_spells[spell] == 0:
                hp -= bonus_hp
                armour -= bonus_armour
                del active_spells[spell]

        if boss_hp <= 0:
            best_cost = min(best_cost, running_cost)

        if player_turn:
            for spell in spells:
                spell_cost, _, bonus_hp, bonus_armour, _, spell_duration = spells[spell]

                if spell in active_spells or spell_cost > mana:
                    continue

                new_active_spells = active_spells | {spell: spell_duration}
                new_player_state = (hp + bonus_hp, armour + bonus_armour, mana - spell_cost, running_cost + spell_cost)
                possible_outcomes.append((new_active_spells, new_player_state, (boss_hp, boss_damage), False))
        else:
            new_player_state = (hp - max(1, boss_damage - armour), armour, mana, running_cost)
            possible_outcomes.append((active_spells, new_player_state, (boss_hp, boss_damage), True))

    return best_cost


if __name__ == '__main__':
    print(solve(1))  # 1824 | 1.44 seconds
    print(solve(2))  # 1937 | 0.17 seconds
