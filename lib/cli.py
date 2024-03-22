import sys # provides access to system-specific parameters and functions, such as command-line arguments
from models.init import RecipeDB, Recipe

# Various options available for my recipe organizer
def main():
    db = RecipeDB('recipe.db')
    while True:
        menu()
        choice = input(">>>>> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_recipes(db)
        elif choice == "2":
            find_recipe_by_title(db)
        elif choice == "3":
            find_recipe_by_id(db)
        elif choice == "4":
            create_recipe(db)
        elif choice == "5":
            update_recipe(db)
        elif choice == "6":
            delete_recipe(db)
        elif choice == "7":
            show_all_users(db)
        elif choice == "8":
            show_all_categories(db)
        elif choice == "9":
            show_all_meal_types(db)
        elif choice == "10":
            show_all_cuisine_types(db)
        elif choice == "11":
            show_all_ingredients(db)
        else:
            print("Invalid choice")


# CLI menu options for my Recipe organizer 
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all recipes")
    print("2. Find recipe by title")
    print("3. Find recipe by id")
    print("4. Create recipe")
    print("5. Update recipe")
    print("6. Delete recipe")
    print("7. Show all users")
    print("8. Show all categories")
    print("9. Show all meal types")
    print("10. Show all cuisine types")
    print("11. Show a list of ingredients")

# Exiting the program functionality
def exit_program():
    print("Exiting program...")
    sys.exit()

# Listing all the recipes
def list_recipes(db): # db is a parameter to access the database to retrieve information
    recipes = db.get_recipes()
    if recipes:
        for recipe in recipes:
            print(f"{recipe.id}: {recipe.title}")
    else:
        print("No recipes found.")

# FInding recipes by title
def find_recipe_by_title(db):
    title = input("Enter the title of the recipe: ")
    recipe = db.get_recipe_by_title(title)
    if recipe:
        print_recipe_details(recipe)
    else:
        print("Recipe not found.")

# Finding recipe by id
def find_recipe_by_id(db):
    recipe_id = input("Enter the ID of the recipe: ")
    recipe = db.get_recipe_by_id(recipe_id)
    if recipe:
        print_recipe_details(recipe)
    else:
        print("Recipe not found.")

# Getting all the recipe details
def print_recipe_details(recipe):
    print(f"ID: {recipe.id}")
    print(f"Title: {recipe.title}")
    print(f"Instructions: {recipe.instructions}")
    print(f"Category ID: {recipe.category_id}")
    print(f"Cuisine Type: {recipe.cuisine_type}")
    print(f"Meal Type: {recipe.meal_type}")
    print(f"Dietary Preferences: {recipe.dietary_preferences}")
    print(f"Special Diets: {recipe.special_diets}")
    print(f"Allergens: {recipe.allergens}")
    print(f"User ID: {recipe.user_id}")

# creating a new recipe
def create_recipe(db):
    print("Creating a new recipe:")
    title = input("Enter the title of the recipe: ")
    instructions = input("Enter the instructions for the recipe: ")
    category_id = int(input("Enter the category ID for the recipe: "))
    cuisine_type = input("Enter the cuisine type for the recipe: ")
    meal_type = input("Enter the meal type for the recipe: ")
    dietary_preferences = input("Enter the dietary preferences for the recipe: ")
    special_diets = input("Enter any special diets for the recipe: ")
    allergens = input("Enter any allergens for the recipe: ")
    user_id = int(input("Enter the user ID for the recipe: "))

    new_recipe = Recipe(title=title, instructions=instructions, category_id=category_id,
                        cuisine_type=cuisine_type, meal_type=meal_type, dietary_preferences=dietary_preferences,
                        special_diets=special_diets, allergens=allergens, user_id=user_id)
    db.add_recipe(new_recipe)
    print("Recipe created successfully!")


# updating a recipe
def update_recipe(db):
    print("Updating an existing recipe:")
    recipe_id = int(input("Enter the ID of the recipe to update: "))
    recipe = db.get_recipe_by_id(recipe_id)
    if recipe:
        # Prompt user for the areas he/she wants to update
        title = input("Enter the new title of the recipe: ")
        if title:
            recipe.title = title
        instructions = input("Enter the new instructions for the recipe: ")
        if instructions:
            recipe.instructions = instructions
        category_id = input("Enter the new category ID for the recipe: ")
        if category_id:
            recipe.category_id = int(category_id)
        cuisine_type = input("Enter the new cuisine type for the recipe: ")
        if cuisine_type:
            recipe.cuisine_type = cuisine_type
        meal_type = input("Enter the new meal type for the recipe: ")
        if meal_type:
            recipe.meal_type = meal_type
        dietary_preferences = input("Enter the new dietary preferences for the recipe: ")
        if dietary_preferences:
            recipe.dietary_preferences = dietary_preferences
        special_diets = input("Enter the new special diets for the recipe: ")
        if special_diets:
            recipe.special_diets = special_diets
        allergens = input("Enter the new allergens for the recipe: ")
        if allergens:
            recipe.allergens = allergens

        db.update_recipe(recipe)
        print("Recipe updated successfully!")
    else:
        print("Recipe not found.")

# Deleting a recipe 
def delete_recipe(db):
    print("Deleting an existing recipe:")
    recipe_id = int(input("Enter the ID of the recipe to delete: "))
    recipe = db.get_recipe_by_id(recipe_id)
    if recipe:
        confirm = input(f"Are you sure you want to delete the recipe '{recipe.title}'? (y/n): ").strip().lower()
        if confirm == 'y':
            db.delete_recipe(recipe_id)
            print("Recipe deleted successfully!")
    else:
        print("Recipe not found.")

# Show all users
def show_all_users(db):
    users = db.get_users()
    if users:
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Role: {user.role}, Created At: {user.created_at}, Age: {user.age}, Gender: {user.gender}")
    else:
        print("No users found.")

# Show all categories
def show_all_categories(db):
    categories = db.get_categories()
    if categories:
        for category in categories:
            print(f"ID: {category.id}, Name: {category.name}")
    else:
        print("No categories found.")

# Show all meal types
def show_all_meal_types(db):
    meal_types = db.get_meal_types()
    if meal_types:
        for meal_type in meal_types:
            print(meal_type)
    else:
        print("No meal types found.")

# Show all cuisine types
def show_all_cuisine_types(db):
    cuisine_types = db.get_cuisine_types()
    if cuisine_types:
        for cuisine_type in cuisine_types:
            print(cuisine_type)
    else:
        print("No cuisine types found.")

# Show a list of ingredients
def show_all_ingredients(db):
    ingredients = db.get_ingredients()
    if ingredients:
        for ingredient in ingredients:
            print(f"ID: {ingredient.id}, Name: {ingredient.name}")
    else:
        print("No ingredients found.")

if __name__ == "__main__":
    main()
