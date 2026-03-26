from databases.mysql.client import MysqlClient



class FilmsOperations:
    def __init__(self, db: MysqlClient):
        self.db = db


    """ The function generates a request to search for a movie by keyword and passes the result on """
    def find_by_keyword(self, keyword, limit=10, page=0):
        query = "SELECT title FROM film WHERE title LIKE %s LIMIT %s OFFSET %s"
        param = (f"%{keyword}%", limit, page *10)
        return self.db.fetch_all(query, param)


    """ Getting a list of all genres in the database """
    def get_all_genres_with_dates(self):
        query = """SELECT c.category_id, c.name, MIN(f.release_year) AS min_year, MAX(f.release_year) AS max_year
                FROM category AS c
                JOIN film_category AS f_c 
                    ON c.category_id = f_c.category_id
                JOIN film AS f 
                    ON f_c.film_id = f.film_id
                GROUP BY c.category_id, c.name;
                """
        return self.db.fetch_all(query)


    """ Search for a movie by year of release and genre """
    def search_films_by_year_range_by_genre(self, gener_id, start_year, end_year, limit=10, page=0):
        query = """
                    SELECT f.title, f.release_year
                    FROM film as f
                    JOIN film_category as f_c
                        ON f.film_id = f_c.film_id
                    WHERE f_c.category_id = %s AND f.release_year >= %s AND f.release_year <= %s
                    ORDER BY f.release_year
                    LIMIT %s OFFSET %s
                    """
        param = (gener_id,start_year, end_year, limit, page)
        return self.db.fetch_all(query, param)