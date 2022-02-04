################### Scope ####################

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# Global Scope
# player_health = 10
#
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# There is no Block Scope

# game_level = 3
# enemies = ["Sceleton", "Zombie", "Alien"]
#
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy)

# Modify Global Scope

# enemies = 1
#
#
# def increase_enemies():
#     global enemies
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Global Constants

PI = 3.14159
