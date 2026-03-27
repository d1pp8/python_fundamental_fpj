from databases.mysql.client import MysqlClient
from services.film_operation import FilmsOperations

from utilities import input_manager, menu
from controllers import film_controller



db = MysqlClient()
films = FilmsOperations(db)

while True:

    menu.show_main_menu()
    choice = input_manager.check_choice("\nSelect the number: ", ["1","2","3","0"])

    if choice == "1":
        film_controller.search_by_keyword(films)

    elif choice == "2":
        film_controller.search_by_genres_and_year(films)

    elif choice == "3":
        film_controller.show_statistics()


    elif choice == "0":
        print("\n🖐️Work is completed, bye🖐️")
        break