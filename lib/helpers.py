import sqlite3
from sqlite3 import Error
from typing import List  # Add this line to import List type
from models import Recipe, Category, Ingredient, User

class RecipeDB:
    def __init__(self, db_file='recipe.db'): 
        self.db_file = db_file
        self.create_tables()  # Call create_tables method during initialization

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return None

    def create_tables(self):
        sql_queries = [
            """
            CREATE TABLE IF NOT EXISTS recipe (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                instructions TEXT NOT NULL,
                category_id INTEGER,
                cuisine_type TEXT,
                meal_type TEXT,
                dietary_preferences TEXT,
                special_diets TEXT,
                allergens TEXT,
                user_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES category(id),
                FOREIGN KEY (user_id) REFERENCES user(id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS category (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS ingredient (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS recipe_ingredient (
                recipe_id INTEGER,
                ingredient_id INTEGER,
                quantity REAL,
                unit TEXT,
                FOREIGN KEY (recipe_id) REFERENCES recipe(id),
                FOREIGN KEY (ingredient_id) REFERENCES ingredient(id),
                PRIMARY KEY (recipe_id, ingredient_id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                role TEXT NOT NULL,
                created_at TEXT NOT NULL,
                age INTEGER,
                gender TEXT
            );
            """
        ]
        try:
            conn = self.create_connection()
            cur = conn.cursor()
            for query in sql_queries:
                cur.execute(query)
            conn.commit()
            conn.close()
        except Error as e:
            print(e)

    def get_recipes(self) -> List[Recipe]:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM recipe")
            rows = cur.fetchall()
            recipes = [Recipe(*row) for row in rows]
            conn.close()
            return recipes
        return []

    def get_recipe_by_title(self, title: str) -> Recipe:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM recipe WHERE title=?", (title,))
            row = cur.fetchone()
            if row:
                return Recipe(*row)
        return None

    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM recipe WHERE id=?", (recipe_id,))
            row = cur.fetchone()
            if row:
                return Recipe(*row)
        return None

    def update_recipe(self, recipe: Recipe):
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("""
                UPDATE recipe
                SET title=?, instructions=?, category_id=?, cuisine_type=?, meal_type=?, 
                    dietary_preferences=?, special_diets=?, allergens=?, user_id=?
                WHERE id=?
            """, (recipe.title, recipe.instructions, recipe.category_id, recipe.cuisine_type,
                  recipe.meal_type, recipe.dietary_preferences, recipe.special_diets,
                  recipe.allergens, recipe.user_id, recipe.id))
            conn.commit()
            conn.close()

    def add_recipe(self, recipe: Recipe):
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO recipe (title, instructions, category_id, cuisine_type, meal_type, dietary_preferences, special_diets, allergens, user_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (recipe.title, recipe.instructions, recipe.category_id, recipe.cuisine_type, recipe.meal_type, recipe.dietary_preferences, recipe.special_diets, recipe.allergens, recipe.user_id))
            conn.commit()
            conn.close()

    def delete_recipe(self, recipe_id: int):
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("DELETE FROM recipe WHERE id=?", (recipe_id,))
            conn.commit()
            conn.close()

    def add_category(self, category: Category):
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("INSERT INTO category (id, name) VALUES (?, ?)", (category.id, category.name))
            conn.commit()
            conn.close()

    def get_users(self) -> List[User]:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM user")
            rows = cur.fetchall()
            users = [User(*row) for row in rows]
            conn.close()
            return users
        return []

    def get_categories(self) -> List[Category]:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            categories = [Category(*row) for row in rows]
            conn.close()
            return categories
        return []

    def get_meal_types(self) -> List[str]:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT DISTINCT meal_type FROM recipe")
            rows = cur.fetchall()
            meal_types = [row[0] for row in rows]
            conn.close()
            return meal_types
        return []

    def get_cuisine_types(self) -> List[str]:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT DISTINCT cuisine_type FROM recipe")
            rows = cur.fetchall()
            cuisine_types = [row[0] for row in rows]
            conn.close()
            return cuisine_types
        return []

    def get_ingredients(self) -> List[Ingredient]:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM ingredient")
            rows = cur.fetchall()
            ingredients = [Ingredient(*row) for row in rows]
            conn.close()
            return ingredients
        return []
