from art import logo, vs
from game_data import data as game_data
import random


def get_random_account() -> dict:
    return random.choice(game_data)


def format_data(account) -> None:
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    print(f"{account_name}, a {account_desc}, from {account_country}")


def print_compare_statement(person1: dict, person2: dict) -> None:
    print(f"Compare A: {person1['name']}, {person1['description']}, from {person1['country']}")
    print(vs)
    print(f"Compare B: {person2['name']}, {person2['description']}, from {person2['country']}")


def main():
    user_score = 0
    is_game_over = False

    print(logo)
    print("#" * 80)

    while not is_game_over:
        person1 = get_random_account()
        person2 = get_random_account()
        print_compare_statement(person1, person2)
        user_tip = input("Who has more followers?: Type 'A' or 'B': ").lower()

        if user_tip == "a" and person1["follower_count"] > person2["follower_count"]:
            user_score += 1
            print(f"You are right! Current score: {user_score}")
        elif user_tip == "b" and person2["follower_count"] > person1["follower_count"]:
            user_score += 1
            print(f"You are right! Current score: {user_score}")
        else:
            print(f"Wrong, your score: {user_score}")
            is_game_over = True


main()
