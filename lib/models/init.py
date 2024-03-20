import sqlite3
from sqlite3 import Error
from models.recipe import Recipe
from models.recipe import Category
from models.recipe import Ingredient
from models.recipe import RecipeIngredient
from models.recipe import User
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
    def add_recipe(self, recipe):
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO recipe (title, instructions, category_id, cuisine_type, meal_type, dietary_preferences, special_diets, allergens, user_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (recipe.title, recipe.instructions, recipe.category_id, recipe.cuisine_type, recipe.meal_type, recipe.dietary_preferences, recipe.special_diets, recipe.allergens, recipe.user_id))
            conn.commit()
            conn.close()
        else:
            print("Error: Unable to establish database connection.")

    def add_category(self, category):
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("INSERT INTO category (id, name) VALUES (?, ?)", (category.id, category.name))
            conn.commit()
            conn.close()
        else:
            print("Error: Unable to establish database connection.")


if __name__ == "__main__":
    db = RecipeDB('recipe.db')
    recipes = db.get_recipes()
    for recipe in recipes:
        print(recipe.title)
