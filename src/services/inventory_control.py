from csv import DictReader
from typing import Dict

from models.dish import Recipe
from models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        for ingredient, amount in recipe.items():
            if ingredient not in self.inventory:
                return False
            if amount > self.inventory[ingredient]:
                return False
        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if not self.check_recipe_availability(recipe):
            raise ValueError()
        for ingredient, amount in recipe.items():
            self.inventory[ingredient] -= amount


if __name__ == "__main__":
    invetory = InventoryMapping()
    mussarela = Ingredient("queijo mussarela")
    print(invetory.inventory[mussarela])
    recipe: Recipe = {mussarela: 200}
    invetory.consume_recipe(recipe)
    print(invetory.inventory[mussarela])
    invetory.consume_recipe(recipe)
