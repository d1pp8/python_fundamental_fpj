from utilities import menu

def check_choice(question: str, valid_choices: list):

    """ FOR MENU Checking the validity of the answer to the question """

    valid_choices = {valid.lower() for valid in valid_choices}
    while True:
        value = input(question).strip().lower()
        if value in valid_choices:
            return value
        print(f"\n⭕ Please enter one of: {', '.join(sorted(valid_choices))}")




def get_valid_input(validator, gener):

    """ Validator function to check the presence of data """

    while True:
        menu.select_release_years(gener["name"], gener["min_year"], gener["max_year"])
        value = input().strip().lower()

        if value == "back":
            return "back", "back"

        if value == "exit":
            return None, None

        result = validator(value, gener)

        if result:
            return  result

        if result is None:
            print("\n❌ Invalid input")




def validate_year_input(value:str, gener):

    """ Is the year entered by the user valid? """

    if "-" in value:

        # Parsing by "-", to get two values
        parts = value.split("-")
        if len(parts) != 2:
            return None

        start, end = parts
        if not(start.isdigit() and end.isdigit()):
            return None

        # The first year of the range cannot be greater than the second
        start, end = int(start), int(end)
        if start > end:
            return None

        # If the entered range is not entered correctly, then information is displayed about the range in which we have films.
        elif  gener["max_year"] < start < gener["min_year"] or gener["max_year"] < end < gener["min_year"]:
            print_range_checker(gener, start, end)
            return False


        # If the dates are entered correctly and two different dates are received, we return the values
        return start, end

    # If one date is entered, I return it.
    if value.isdigit():
        value = int(value)
        if value < gener["min_year"] or value > gener["max_year"]:
            print_range_checker(gener, value)
            return False

        year = int(value)
        return year, year

    # Default return
    return None


def print_range_checker(gener, start, end=None):

        """ Function to display an error if the user entered an incorrect year """
        if end is not None:
            print(f"\n❌No results for \'{gener['name']}\' in range \'{start}\'-\'{end}\'")
            print(f"➡️We have movies in the \'{gener['name']}\' only from {gener["min_year"]}-{gener["max_year"]} years.")
        else:
            print(f"\n❌No results for \'{gener['name']}\' in year \'{start}\'")
            print(f"➡️We have movies in the \'{gener['name']}\' only from {gener["min_year"]}-{gener["max_year"]} years.")






def get_user_gener(genres):

    """ Get selected gener from user input """

    #Create dictionaries for searching by id and name
    genres_by_id = {genre["category_id"]: genre for genre in genres}
    genres_by_name = {genre_id["name"].lower(): genre_id for genre_id in genres}

    while True:
        menu.genre_selection()
        value = input().strip().lower()

        # For exit from func to main menu
        if value == "exit":
            return None

        # Check if the value was a number
        if value.isdigit():
            value = int(value)
            if value in genres_by_id:
                return genres_by_id[value]

            print("\n❌Invalid number\n")
            continue


        # Check if the value was a word
        if value in genres_by_name:
            return genres_by_name[value]

        print("\n❌Invalid name\n")


def format_params(param):
    if "keyword" in param:
        return f"keyword = '{param['keyword']}'"
    if "genre" in param:
        return f"{param['genre']} ({param['year_range'][0]}-{param['year_range'][1]})"
    return str(param)
