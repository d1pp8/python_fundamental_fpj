
def show_main_menu():

    """ Utility for displaying the main menu """

    width = 32
    print("\n" + "=" * width)
    print("         🎬 MAIN MENU")
    print("=" * width)
    print("  1. 🔍 Search by keyword")
    print("  2. 🎭 Search by genre & year")
    print("  3. 📈 Popular & recent queries")
    print("  0. 🚪 Exit")
    print("=" * width)


def show_menu_for_range_years(name):

    """ Utility for displaying the menu for specifying a range of years or going back or to the main menu """

    width = 40
    print("\n" + "-" * width)
    print(f"   📅 Search by year for: '{name}'")
    print("-" * width)
    print("  1. ✏️  Enter year range")
    print("  9. 🔙  Select another gener")
    print("  0. 🚪 Exit")
    print("-" * width)


def genre_selection():

    """ Function for displaying a short menu of item selections """


    main_string = "".center(45)

    length = int(len(main_string)/2)

    print("[🔍ID or Name]".center(length), end = "")
    print("[🚪Exit]".center(length), end="")
    print("\n\n️⚙️Your option: ",end="")


def select_release_years(name):
    main_string = f"🔍 Enter year or range for '{name}' (e.g. 1999 or 1990-2000)"

    print(f"\n{main_string}")

    length = int(len(main_string) / 2)

    print("[🔙Back]".center(length), end="")
    print("[🚪Exit]".center(length), end="")
    print("\n\n⚙️Your option: ", end="")
