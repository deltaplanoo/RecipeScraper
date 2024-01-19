import sys
import os
from recipe_scrapers import scrape_me

def scrape_n_save(url):
    scraper = scrape_me(url)

    ingredienti = scraper.ingredients()
    preparazione = scraper.instructions()

    ingredienti_list = "- " + "\n- ".join(" ".join(ingredienti).split("\n"))
    preparazione_list = "- " + "\n- ".join(preparazione.split("\n"))

    with open(os.path.join("/home/delta/Documents/Uni/Altro/ObsidianVault/Lists/Cucina", f"{scraper.title()}.md"), 'w') as file:
    # with open(os.path.join("recipes", f"{scraper.title()}.md"), 'w') as file:
        file.write(f"#cucina\n\nLink ricetta: [{scraper.host()}]({url})\n\nTempo: {scraper.total_time()}\n\nDosi: {scraper.yields()}\n\n---\n## Ingredienti\n{ingredienti_list}\n\n## Preparazione\n{preparazione_list}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the link to the recipe as an argument")
    else:
        recipe_url = sys.argv[1]
        scrape_n_save(recipe_url)