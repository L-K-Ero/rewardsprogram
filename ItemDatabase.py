import os
import psycopg2
import psycopg2.extras
import urllib.parse

#def dict_factory(cursor, row):
#    d = {}
#    for idx, col in enumerate(cursor.description):
#        d[col[0]] = row[idx]
#    return d

class ItemsDB:
    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
        
        self.connection = psycopg2.connect(
            cursor_factory=psycopg2.extras.RealDictCursor,
            database=url.path[1:],
            port=url.port
        )
        self.cursor = self.connection.cursor()
        
        #self.connection = sqlite3.connect("database.db")
        #self.connection.row_factory = dict_factory
        #self.cursor = self.connection.cursor()
    
    def __del__(self):
        self.connection.close()
        
    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS members (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255), birthday VARCHAR(255), zipcode VARCHAR(255), level VARCHAR(255))")
        self.connection.commit()
        
    def get_Members(self):
        self.cursor.execute("SELECT * FROM members ORDER BY id")
        result = self.cursor.fetchall()
        return result

    def get_one_Member(self, member_id):
        data = [member_id]
        self.cursor.execute("SELECT * FROM members WHERE id = %s", data)
        result = self.cursor.fetchone()
        return result

    def insert_Member(self, name, email, phone, birthday, zipcode, level):
        data = [name, email, phone, birthday, zipcode, level]
        self.cursor.execute("INSERT INTO members (name, email, phone, birthday, zipcode, level) VALUES (%s, %s, %s, %s, %s, %s)", data)
        self.connection.commit()
        return None

    def delete_Member(self, member_id):
        data = [member_id]
        self.cursor.execute("DELETE FROM members WHERE rowid = %s", data)
        self.connection.commit()
        return None
    
    def edit_Member(self, member_id, name, email, phone, birthday, zipcode, level):
        data = [name, email, phone, birthday, zipcode, level, member_id]
        self.cursor.execute("UPDATE members SET name = %s, email = %s, phone = %s, birthday = %s, zipcode = %s, level = %s WHERE id = %s;", data)
        self.connection.commit()
        return None
### row_factory , sqlite3 and python3 tuples to dictionaries stuff...
