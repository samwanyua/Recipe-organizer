from models.init import RecipeDB
from models import Category, Ingredient, Recipe, User

def seed_database(db):
    # Seed categories
    categories = [
        Category(id=1, name="Breakfast"),
        Category(id=2, name="Lunch"),
        Category(id=3, name="Dinner"),
        Category(id=4, name="Dessert")
    ]
    for category in categories:
        db.add_category(category)

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
        db.add_ingredient(ingredient)

    # Seed recipes
    recipes = [
        Recipe(id=1, title="Scrambled Eggs", instructions="...", category_id=1, cuisine_type="American",
               meal_type="Breakfast", dietary_preferences="", special_diets="", allergens="", user_id=1),
        Recipe(id=2, title="Grilled Chicken Sandwich", instructions="...", category_id=2, cuisine_type="American",
               meal_type="Lunch", dietary_preferences="", special_diets="", allergens="", user_id=1),
        Recipe(id=3, title="Chocolate Cake", instructions="...", category_id=4, cuisine_type="Dessert",
               meal_type="Dessert", dietary_preferences="", special_diets="", allergens="", user_id=2)
    ]
    for recipe in recipes:
        db.add_recipe(recipe)

    # Seed users
    users = [
        User(id=1, username="Sam wanyua", role="user", created_at="2024-03-19", age=30, gender="Male"),
        User(id=2, username="Charity Okoth", role="user", created_at="2024-03-20", age=25, gender="Female")
    ]
    for user in users:
        db.add_user(user)

if __name__ == "__main__":
    db = RecipeDB('recipe.db')
    seed_database(db)
