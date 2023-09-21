# Christmas Spirit

ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLAND_PRICE = 3
TREE_LIGHTS_PRICE = 15

quantity_of_decorations = int(input())
days_left = int(input())

total_cost = 0
total_spirit = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        total_cost += quantity_of_decorations * ORNAMENT_SET_PRICE
        total_spirit += 5  # spirit points

    if day % 3 == 0:
        total_cost += quantity_of_decorations * TREE_SKIRT_PRICE
        total_cost += quantity_of_decorations * TREE_GARLAND_PRICE
        total_spirit += 13  # Sum of spirit points

    if day % 5 == 0:
        total_cost += quantity_of_decorations * TREE_LIGHTS_PRICE
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += TREE_SKIRT_PRICE + TREE_GARLAND_PRICE + TREE_LIGHTS_PRICE


if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
