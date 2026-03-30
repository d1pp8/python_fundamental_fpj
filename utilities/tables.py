from utilities import input_manager

def draw_table_with_ten_movie(films, counter: int, page_number):

    """ Draws a table with 10 films """

    width = 45
    print("\n" + "🎬 Your result 🎬".center(width, "="))

    for film in films:
        print(f"{counter}. {film["title"]} ({film["release_year"]})")
        counter += 1
    print(f" Page: {page_number} ".center(width, "="))





def draw_table_with_all_genres(films_genres):

    """ A simple function for clearly displaying genres """

    width = 45
    print("\n" + " List of films genres ".center(width, "="))
    print(f"{"ID":<5} {"Genre":<20} {"Earliest":<10} {"Latest":<10}")
    print("=" * width)

    for genre in films_genres:
        print(f"{genre["category_id"]:<5} {genre["name"]:<20} {genre["min_year"]:<10} {genre["max_year"]:<10}")

    print("=" * width)


def print_top_searches(stats):

    print("\n🔥 TOP 5 QUERIES:")
    for i, item in enumerate(stats, start=1):
        search_type = item["_id"]["search_type"]
        param = input_manager.format_params(item["_id"]["param"])
        count = item["count"]
        print(f"{i}. {search_type}: {param} → {count} times")

def print_last_searches(stats):
    print("\n🌙 LAST 5 QUERIES:")
    for i, item in enumerate(stats, start=1):
        search_type = item["search_type"]
        param = input_manager.format_params(item["param"])
        print(f"{i}. {search_type}: {param}")

