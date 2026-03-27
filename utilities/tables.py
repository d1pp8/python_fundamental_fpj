
def draw_table_with_ten_movie(films, counter: int, page_number):

    width = 45
    print("\n" + "🎬 Your result 🎬".center(width, "="))

    for film in films:
        print(f"{counter}. {film["title"]} ({film["release_year"]})")
        counter += 1
    print(f" Page: {page_number} ".center(width, "="))




""" A simple function for clearly displaying genres """
def draw_table_with_all_genres(films_genres):

    width = 45
    print("\n" + " List of films genres ".center(width, "="))
    print(f"{"ID":<5} {"Genre":<20} {"Earliest":<10} {"Latest":<10}")
    print("=" * width)

    for genre in films_genres:
        print(f"{genre["category_id"]:<5} {genre["name"]:<20} {genre["min_year"]:<10} {genre["max_year"]:<10}")

    print("=" * width)


def format_params(param):
    if "keyword" in param:
        return f"keyword = '{param['keyword']}'"
    if "genre" in param:
        return f"{param['genre']} ({param['year_range'][0]}-{param['year_range'][1]})"
    return str(param)
