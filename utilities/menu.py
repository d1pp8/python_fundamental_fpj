
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


# don't use, for latter maybe
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
    """ Utility for displaying a short menu of item selections """
    main_string = "🎥Select a genre or exit:".center(45)

    length = int(len(main_string)/2)
    print(main_string)
    print("[🔍ID or Name]".center(length), end = "")
    print("[🚪Exit]".center(length), end="")
    print("\n\n️⚙️Your option: ",end="")


def select_release_years(name, min, max):
    """ Utility for displaying a short menu of selections when specifying years """

    width = 59
    print()
    print("=" * width)
    main_string = f"🔍 Enter year or range for '{name}' (e.g. 1999 or {min}-{max})"

    print(f"{main_string}")

    length = int(len(main_string) / 2)

    print("[🔙Back]".center(length), end="")
    print("[🚪Exit]".center(length))
    print("=" * width)
    print("\n⚙️Your option: ", end="")


def menu_for_statistic():
    """ Utility for displaying the Statistic menu """
    width = 32
    print("\n" + "=" * width)
    print("📊 Statistics".center(width))
    print("=" * width)
    print("  1. 🔥 Top 5 popular queries")
    print("  2. 🌙 Last 5 queries")
    print("  0. 🚪 Exit")
    print("=" * width)


def menu_navigate_for_statistic():
    """ Utility for navigating the statistics menu """
    width = 22
    print("Enter the next action:")
    print("=" * width)
    print("[🔙 Back]" + "\t" + "  " +"[🚪Exit]")
    print("=" * width)
