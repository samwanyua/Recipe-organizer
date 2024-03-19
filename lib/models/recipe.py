import sqlite3
from sqlite3 import Error
from typing import List, Tuple

class Recipe:
    def __init__(self, id: int, title: str, instructions: str, category_id: int, cuisine_type: str,
                 meal_type: str, dietary_preferences: str, special_diets: str, allergens: str, user_id: int):
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
