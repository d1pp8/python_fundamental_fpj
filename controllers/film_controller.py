from utilities import input_manager, tables , menu, pagination
from services.search_logger import log_search
from services.statistic import get_top_searches


""" Created a controller to move logic from main to a separate layer """

# Constant for limit content on "page"
PAGE_SIZE = 10


def search_by_keyword(films):

    """
    Controller for finding films by keyword
    Point 1. From main menu
    """

    keyword = input("\n🔍 Enter your \'keyword\': ")


    def query_create_func(page):

        """ A function closure was created to avoid duplicating a large piece of code
        A closure function specifically for keyword searches """

        result = films.find_by_keyword(keyword=keyword.lower(), limit=PAGE_SIZE,page=page)

        # Logging a query to a MongoDB database
        log_search(search_type="keyword",param={"keyword": keyword}, result_count=len(result))

        return result

    # Function to display 10 movies received by a request
    pagination.get_ten_films(query_create_func)



def search_by_genres_and_year(films):

    """
    Controller for finding films by genres and years release
    Point 2. From main menu
    """

    films_genres = films.get_all_genres_with_dates()

    while True:

        # draw all genres and get one from user
        tables.draw_table_with_all_genres(films_genres)
        selected_genre = input_manager.get_user_gener(films_genres)

        # Returns to the main menu if the user does not want to select a genre
        # And show a message about info has stopped
        if selected_genre is None:
            print("⛔Information about film genres has stopped.")
            return None

        while True:

            # Display a menu with an option to enter a range of release years or exit.
            menu.show_menu_for_range_years(selected_genre["name"])
            choice = input_manager.check_choice("\nSelect the number: ", ["1", "9", "0"])

            # Here we add a search by year and a check of the validity of the entered data.
            if choice == "1":

                start_year, end_year = input_manager.get_valid_input(input_manager.validate_year_input, selected_genre)

                # For selected another gener
                if start_year == "back":
                    break

                # For exit to main menu
                if start_year is None:
                    return None

                def query_create_func(page):

                    """ A function closure was created to avoid duplicating a large piece of code
                     The closure function is specifically for searching by genre and year """

                    result = films.search_films_by_year_range_by_genre(gener_id=selected_genre["category_id"], start_year=start_year, end_year=end_year, limit=PAGE_SIZE, page=page)

                    # Logging a query to a MongoDB database
                    log_search(search_type="genre_year", param = {"genre": selected_genre["name"], "year_range": [start_year, end_year]}, result_count=len(result))

                    return result

                # Function to display 10 movies received by a request
                pagination.get_ten_films(query_create_func)

            # For back to select another gener
            if choice == "9":
                break

            return None



def show_statistics():

    """
    Controller for displaying statistics on popular and recent queries
    Point 3. From main menu
    """

    # I must add one more Statistic for last 5 searched
    pass

    stats = get_top_searches()
    print("\n🔥 TOP 5 SEARCHES:\n")

    for i, item in enumerate(stats, start=1):
        search_type = item["_id"]["search_type"]
        param = tables.format_params(item["_id"]["param"])
        count = item["count"]

        print(f"{i}. {search_type}: {param} → {count} times")