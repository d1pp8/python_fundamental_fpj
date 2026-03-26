
    # FOR MENU Checking the validity of the answer to the question
def check_choice(question: str, valid_choices: list):

    valid_choices = {valid.lower() for valid in valid_choices}
    while True:
        value = input(question).strip().lower()
        if value in valid_choices:
            return value
        print(f"\n⭕ Please enter one of: {', '.join(sorted(valid_choices))}")


def get_valid_input(question: str, validator):
    while True:
        value = input(question).strip()
        result = validator(value)

        if result is not None:
            return  result
        print("\n❌ Invalid input")

def validate_year_input(value:str):

    if "-" in value:
        parts = value.split("-")
        if len(parts) != 2:
            return None

        start, end = parts
        if not(start.isdigit() and end.isdigit()):
            return None

        start, end = int(start), int(end)
        if start > end:
            return None
        return start, end

    if value.isdigit():
        year = int(value)
        return year, year

    return None


   # Get selected gener from user input
def get_user_gener(genres):

    #Create dictionaries for searching by id and name
    genres_by_id = {genre["category_id"]: genre for genre in genres}
    genres_by_name = {genre_id["name"].lower(): genre_id for genre_id in genres}

    while True:
        value = input(
                    "- Select the genre (\'ID\'/ or \'name\')"
                    "\n- Write \'0\' for Exit"
                    "\n\n🎈Your option: "
                    ).strip().lower()

        # For exit from func
        if value == "0":
            return None

        # Check if the value was a number
        if value.isdigit():
            value = int(value)
            if value in genres_by_id:
                return genres_by_id[value]

            print("\n❌Invalid number")
            continue


        # Check if the value was a word
        if value in genres_by_name:
            return genres_by_name[value]

        print("\n❌Invalid name")