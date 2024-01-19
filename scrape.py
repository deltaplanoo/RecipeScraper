import sys
from recipe_scrapers import scrape_me

def scrape_n_save(url):
    scraper = scrape_me(url)

    ingredients = scraper.ingredients()
    preparazione = scraper.instructions()

    ingredients_list = "- " + "\n- ".join(ingredients.split("\n"))
    preparazione_list = "- " + "\n- ".join(preparazione.split("\n"))

    with open(f"{scraper.title()}.md", 'w') as file:
        file.write(f"# {scraper.title()}\n\n## Ingredienti\n{ingredients_list}\n\n## Preparazione\n{preparazione_list}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the link to the recipe as an argument")
    else:
        recipe_url = sys.argv[1]
        scrape_n_save(recipe_url)