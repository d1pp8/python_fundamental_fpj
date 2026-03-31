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
    """ A utility for displaying top search queries from MongoDB """
    print()
    print("=" * 52)
    print("🔥TOP 5 QUERIES🔥".center(52))
    print("=" * 52)
    for i, item in enumerate(stats, start=1):
        search_type = item["_id"]["search_type"]
        param = input_manager.format_params(item["_id"]["param"])
        count = item["count"]
        print(f"{i}. {search_type:<10} | {param:<25} | {count} times")
    print("=" * 52)

def print_last_searches(stats):
    """ A utility for displaying the last 5 search queries from MongoDB """
    print()
    print("=" * 40)
    print("🌙LAST 5 QUERIES🌙".center(40))
    print("=" * 40)
    for i, item in enumerate(stats, start=1):
        search_type = item["search_type"]
        param = input_manager.format_params(item["param"])
        print(f"{i}. {search_type:<10} | {param:<25}")
    print("=" * 40)
