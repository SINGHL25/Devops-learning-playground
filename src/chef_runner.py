
def run_recipe(recipe_file):
    """Simulate running a Chef recipe"""
    print(f"Executing Chef recipe: {recipe_file}")
    return {"status": "success", "recipe": recipe_file}
