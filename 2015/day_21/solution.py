from itertools import chain, combinations, product

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
stats = parse_file_content(file, ('\n', ': '), str)

store = [
    [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0)
    ],
    [
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5)
    ],
    [
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3)
    ]
]


@stopwatch
def solve():
    only_weapon = product(store[0])
    weapon_ring = product(store[0], store[2])
    weapon_ring_ring = (
        (weapon, ring1, ring2)
        for weapon in store[0]
        for ring1, ring2 in combinations(store[2], 2)
    )
    weapon_armour = product(store[0], store[1])
    weapon_armour_ring = product(store[0], store[1], store[2])
    weapon_armour_ring_ring = (
        (weapon, armor, ring1, ring2)
        for weapon, armor in product(store[0], store[1])
        for ring1, ring2 in combinations(store[2], 2)
    )

    best_cost, worst_cost = float('inf'), 0

    for combo in chain(only_weapon, weapon_ring, weapon_ring_ring, weapon_armour, weapon_armour_ring, weapon_armour_ring_ring):
        boss_hp, boss_damage, boss_armour = (int(pair[1]) for pair in stats)
        hp, damage, armour, cost = 100, 0, 0, 0

        for cost_, damage_, armour_ in combo:
            cost += cost_
            damage += damage_
            armour += armour_

        while boss_hp > 0 and hp > 0:
            boss_hp -= max(1, damage - boss_armour)
            if boss_hp <= 0:
                break
            hp -= max(1, boss_damage - armour)

        if boss_hp <= 0:
            best_cost = min(best_cost, cost)
        else:
            worst_cost = max(worst_cost, cost)

    return best_cost, worst_cost


if __name__ == '__main__':
    print(*solve())  # 121 201 | 0.0025 seconds
