import sqlite3
from sqlite3 import Error
from recipe import Recipe, Category, Ingredient, RecipeIngredient, User
from typing import List, Tuple

class RecipeDB:
    def __init__(self, db_file: str):
        self.db_file = db_file

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return None

    def get_recipes(self) -> List[Recipe]:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM recipe")
            rows = cur.fetchall()
            recipes = [Recipe(*row) for row in rows]
            conn.close()
            return recipes


if __name__ == "__main__":
    db = RecipeDB('recipe.db')
    recipes = db.get_recipes()
    for recipe in recipes:
        print(recipe.title)
