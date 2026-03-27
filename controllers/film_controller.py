from utilities import input_manager, tables , menu, pagination
from services.search_logger import log_search
from services.statistic import get_top_searches


""" Created a controller to move logic from main to a separate layer """

# Constant for limit content on "page"
PAGE_SIZE = 10


""" Controller for finding films by keyword """
""" 1. From main menu """
def search_by_keyword(films):
    keyword = input("\n🔍 Enter your \'keyword\': ")

    def query_create_func(page):

        result = films.find_by_keyword(keyword=keyword.lower(),limit=PAGE_SIZE,page=page)

        log_search(search_type="keyword", param={"keyword": keyword}, result_count=len(result))

        return result

    pagination.get_ten_films(query_create_func)



""" Controller for finding films by genres and years release """
""" 2. From main menu """
def search_by_genres_and_year(films):

    films_genres = films.get_all_genres_with_dates()

    while True:

        """ draw all genres and get one from user """
        tables.draw_table_with_all_genres(films_genres)
        selected_genre = input_manager.get_user_gener(films_genres)

        if selected_genre is None:
            print("⛔Information about film genres has stopped.")
            return None

        gener_id = selected_genre["category_id"]
        gener_name = selected_genre["name"]


        while True:

            menu.show_menu_for_range_years(gener_name)
            choice = input_manager.check_choice("\nSelect the number: ", ["1","0"])

            if choice == "1":
                start_year, end_year = input_manager.get_valid_input(f"\n🗓️Enter year or range for {gener_name}" "\nIn format (yyyy-yyyy): ", input_manager.validate_year_input)

                if start_year < selected_genre["min_year"] or end_year > selected_genre["max_year"]:
                    print(f"\n❌No results for \'{gener_name}\' in range \'{start_year}\'-\'{end_year}\'")
                    print(f"➡️We have movies in the \'{gener_name}\' only from {selected_genre["min_year"]}-{selected_genre["max_year"]} years.")

                elif start_year is None:
                    return None

                else:
                    def query_create_func(page):
                        result = films.search_films_by_year_range_by_genre(gener_id=gener_id, start_year=start_year, end_year=end_year,limit=PAGE_SIZE, page=page)

                        log_search(search_type="genre_year", param = {"genre": gener_name, "year_range": [start_year, end_year]}, result_count=len(result))

                        return result

                    pagination.get_ten_films(query_create_func)


            elif choice == "0":
                return None




def show_statistics():
    stats = get_top_searches()

    print("\n🔥 TOP 5 SEARCHES:\n")

    for i, item in enumerate(stats, start=1):
        search_type = item["_id"]["search_type"]
        param = tables.format_params(item["_id"]["param"])
        count = item["count"]

        print(f"{i}. {search_type}: {param} → {count} times")