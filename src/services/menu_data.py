import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.__data = []
        self.__menu_csv_to_data(source_path)
        self.dishes = self.__get_dishes_from_data()
        self.__add_ingredients_in_each_dish()

    # metódos privados pra organizar melhor cada passo para fazer o menu_data
    def __menu_csv_to_data(self, source_path: str):
        with open(source_path, encoding="utf8") as file:
            menu_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            self.__data.extend(menu_reader)

    def __get_dishes_from_data(self):
        return set(
            Dish(item["dish"], float(item["price"])) for item in self.__data
        )

    def __add_ingredients_in_each_dish(self):
        for dish in self.dishes:
            for item in self.__data:
                if dish.name == item["dish"]:
                    ingredient = Ingredient(item["ingredient"])
                    price = int(item["recipe_amount"])
                    dish.add_ingredient_dependency(ingredient, price)


if __name__ == "__main__":
    menu = MenuData("tests/mocks/menu_base_data.csv")
    print(menu.dishes)
