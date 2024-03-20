import sqlite3
from sqlite3 import Error

class Recipe:
    def __init__(self, id=None, title=None, instructions=None, category_id=None, cuisine_type=None, meal_type=None, dietary_preferences=None, special_diets=None, allergens=None, user_id=None):
        self.id = id
        self.title = title
        self.instructions = instructions
        self.category_id = category_id
        self.cuisine_type = cuisine_type
        self.meal_type = meal_type
        self.dietary_preferences = dietary_preferences
        self.special_diets = special_diets
        self.allergens = allergens
        self.user_id = user_id

class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Ingredient:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class RecipeIngredient:
    def __init__(self, recipe_id: int, ingredient_id: int, quantity: float, unit: str):
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity
        self.unit = unit

class User:
    def __init__(self, id: int, username: str, role: str, created_at: str, age: int, gender: str):
        self.id = id
        self.username = username
        self.role = role
        self.created_at = created_at
        self.age = age
        self.gender = gender

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_tables(conn):
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
        cur = conn.cursor()
        for query in sql_queries:
            cur.execute(query)
        conn.commit()
    except Error as e:
        print(e)

def seed_database(conn):
    # Seed categories
    categories = [
        Category(id=1, name="Breakfast"),
        Category(id=2, name="Lunch"),
        Category(id=3, name="Dinner"),
        Category(id=4, name="Dessert")
    ]
    cur = conn.cursor()
    for category in categories:
        cur.execute("INSERT INTO category (id, name) VALUES (?, ?)", (category.id, category.name))
    conn.commit()

    # Seed ingredients
    ingredients = [
        Ingredient(id=1, name="Eggs"),
        Ingredient(id=2, name="Bread"),
        Ingredient(id=3, name="Tomatoes"),
        Ingredient(id=4, name="Chicken"),
        Ingredient(id=5, name="Chocolate"),
        Ingredient(id=6, name="Sugar")
    ]
    for ingredient in ingredients:
        cur.execute("INSERT INTO ingredient (id, name) VALUES (?, ?)", (ingredient.id, ingredient.name))
    conn.commit()

    # Seed users
    users = [
        User(id=1, username="Sam wanyua", role="user", created_at="2024-03-19", age=30, gender="Male"),
        User(id=2, username="Charity Okoth", role="user", created_at="2024-03-20", age=25, gender="Female")
    ]
    for user in users:
        cur.execute("INSERT INTO user (id, username, role, created_at, age, gender) VALUES (?, ?, ?, ?, ?, ?)",
                    (user.id, user.username, user.role, user.created_at, user.age, user.gender))
    conn.commit()

if __name__ == "__main__":
    db_file = 'recipe.db'
    conn = create_connection(db_file)
    if conn is not None:
        create_tables(conn)
        seed_database(conn)
        conn.close()
    else:
        print("Error: Unable to establish database connection.")
