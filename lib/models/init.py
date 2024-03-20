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
        
    def get_recipe_by_title(self, title: str) -> Recipe:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM recipe WHERE title=?", (title,))
            row = cur.fetchone()
            if row:
                return Recipe(*row)
            else:
                return None
        else:
            return None
        
    def get_recipe_by_id(self, recipe_id: int) -> Recipe:
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT * FROM recipe WHERE id=?", (recipe_id,))
            row = cur.fetchone()
            if row:
                return Recipe(*row)
            else:
                return None
        else:
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
        else:
            print("Error: Unable to establish database connection.")
        
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

    def delete_recipe(self, recipe_id: int):
        conn = self.create_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute("DELETE FROM recipe WHERE id=?", (recipe_id,))
            conn.commit()
            conn.close()
            print("Recipe deleted successfully!")
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

INSERT INTO recipe (title, instructions, category_id, cuisine_type, meal_type, dietary_preferences, special_diets, allergens, user_id)
VALUES ('Scrambled Eggs', 'Cook beaten eggs in a skillet until desired consistency, seasoning with salt and pepper.', 1, 'American', 'Breakfast', '', '', '', 1),
    ('Chicken Stir Fry', 'Brown diced chicken in a pan, stir-fry with vegetables and soy sauce, then serve over rice.', 2, 'Asian', 'Dinner', '', '', '', 2),
    ('Spaghetti Carbonara', 'Toss cooked spaghetti with crispy bacon, eggs, Parmesan cheese, and black pepper until creamy.', 3, 'Italian', 'Dinner', '', '', '', 3),
    ('Vegetable Soup', ' Simmer diced vegetables in broth until tender, seasoning with salt, pepper, and herbs.', 4, 'International', 'Lunch', '', '', '', 4),
    ('Chocolate Brownies', 'Mix melted chocolate with sugar, eggs, vanilla, flour, and cocoa powder, then bake until set.', 5, 'Dessert', 'Dessert', '', '', '', 5),
    ('Caesar Salad', 'Toss romaine lettuce with croutons, Parmesan cheese, and Caesar dressing.', 6, 'American', 'Lunch', '', '', '', 6),
    ('Sushi Rolls', 'Roll sushi rice and fillings in nori sheets, slice, and serve with soy sauce and wasabi.', 7, 'Asian', 'Dinner', '', '', '', 7),
    ('Tacos', ' Fill tortillas with seasoned beef, lettuce, tomatoes, cheese, and salsa.', 8, 'Mexican', 'Dinner', '', '', '', 8),
    ('Grilled Cheese Sandwich', 'Cook buttered bread slices with cheese until golden and melted.', 9, 'American', 'Lunch', '', '', '', 9),
    ('Mushroom Risotto', 'Sauté onions and garlic, cook Arborio rice in broth, stir in mushrooms until creamy.', 10, 'Italian', 'Dinner', '', '', '', 10),
    ('Fruit Smoothie', 'Blend mixed fruits with yogurt or juice until smooth.', 11, 'International', 'Breakfast', '', '', '', 11),
    ('BBQ Ribs', 'Grill seasoned ribs until cooked, basting with BBQ sauce.', 12, 'American', 'Dinner', '', '', '', 12),
    ('Caprese Salad', 'Layer tomato and mozzarella slices, drizzle with olive oil and balsamic glaze, then garnish with basil.', 'Lunch', '', '', '', 13);
