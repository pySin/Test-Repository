snowballs_count = int(input())
max_snowball_value = 0
best_snowball = {
    "snowball_weight": 0,
    "snowball_time": 0,
    "snowball_quality": 0
}

for ball in range(snowballs_count):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        best_snowball['snowball_weight'] = snowball_weight
        best_snowball['snowball_time'] = snowball_time
        best_snowball['snowball_quality'] = snowball_quality


print(f"{best_snowball['snowball_weight']} : {best_snowball['snowball_time']} = "
      f"{max_snowball_value} ({best_snowball['snowball_quality']})")
