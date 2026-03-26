from utilities import input_manager, tables


def get_ten_films(func):

    page_counter = 0
    film_counter = 1

    while True:
        list_with_ten_films = func(page_counter)
        if not list_with_ten_films:
            print("\n❌No such result was found.")
            return

        page_counter += 1
        tables.draw_table_with_ten_movie(list_with_ten_films, film_counter, page_counter)
        film_counter += 10

        if len(list_with_ten_films) < 10:
            print("\n✅All found films")
            # value = input_manager.check_choice("-Write (\'0\'/\'exit\') for exit: ", ["0", "exit"])
            return

        choice_for_next_ten_films = input_manager.check_choice("\n-Show next 10 films? (y/n): ", ["y", "n"])
        if choice_for_next_ten_films == "n":
            print("☑️Information about the films is stopped.")
            return