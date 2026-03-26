""" Utility for displaying the main menu """
def show_main_menu():
    print("\n" + "=" * 32)
    print("         🎬 MAIN MENU")
    print("=" * 32)
    print("  1. 🔍 Search by keyword")
    print("  2. 🎭 Search by genre & year")
    print("  3. 📈 Popular & recent queries")
    print("  0. 🚪 Exit")
    print("=" * 32)


def show_menu_for_range_years(name):
    print("\n" + "-" * 32)
    print(f"   📅 Year range search: '{name}'")
    print("-" * 32)
    print("  1. ✏️  Enter year range")
    print("  0. 🚪 Exit")
    print("-" * 32)