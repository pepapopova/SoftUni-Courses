from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.common.validator import Validator


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if any(f.name == name for f in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = self.__create_food_by_type(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if any(d.name == name for d in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = self.__create_drink_by_type(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({drink_type}) to the drink menu"

    def add_table (self, table_type: str, table_number: int, capacity: int):
        if any(t.table_number == table_number for t in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = self.__create_table_by_type(table_type, table_number, capacity)
        #TODO: add if table is None
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        result = f'Table {table_number} ordered:\n'
        for food_name in food_names:
            if self.__find_food_by_name(food_name):
                result += str(self.__find_food_by_name(food_name)) + '\n'
                self.food_menu.append(self.__find_food_by_name(food_name))
                table.order_food(self.__find_food_by_name(food_name))
        result += f'{self.name} does not have in the menu:\n'
        for food_name in food_names:
            if not self.__find_food_by_name(food_name):
                result += food_name + '\n'
        return result.strip()

    def order_drink (self, table_number: int, *drinks_names):
        table = self.__find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        on_the_menu_drinks = f'Table {table_number} ordered:\n'
        not_in_the_menu_drinks = f'{self.name} does not have in the menu:\n'
        for drink_name in drinks_names:
            drink = self.__find_drink_by_name(drink_name)
            if drink:
                on_the_menu_drinks += str(drink) + '\n'
                self.drinks_menu.append(drink)
                table.order_drink(drink)
            else:
                not_in_the_menu_drinks += drink_name + '\n'
        return on_the_menu_drinks + not_in_the_menu_drinks.strip()

    def leave_table (self, table_number: int):
        table = self.__find_table_by_number(table_number)
        if not table:
            return
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table.table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'

    @staticmethod
    def __create_food_by_type(food_type, name, price):
        if food_type == "Cake": #could be == Cake.__name__
            return Cake(name, price)
        if food_type == "Bread":
            return Bread(name, price)

    @staticmethod
    def __create_drink_by_type(drink_type, name, portion, brand):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        if drink_type == "Water":
            return Water(name, portion, brand)

    @staticmethod
    def __create_table_by_type(table_type, table_number, capacity):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        if table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)

    def __find_table_by_number(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return table
            return None

    def __find_food_by_name(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def __find_drink_by_name(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

