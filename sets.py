from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients).intersection(ALCOHOLS):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"
