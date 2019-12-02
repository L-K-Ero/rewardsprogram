import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class ItemsDB:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
    
    def get_Members(self):
        self.cursor.execute("SELECT rowid,* FROM members")
        result = self.cursor.fetchall()
        return result

    def get_one_Member(self, member_id):
        data = [member_id]
        self.cursor.execute("SELECT rowid,* FROM members WHERE rowid = ?", data)
        result = self.cursor.fetchone()
        return result

    def insert_Member(self, name, email, phone, birthday, zipcode, level):
        data = [name, email, phone, birthday, zipcode, level]
        self.cursor.execute("INSERT INTO members (name, email, phone, birthday, zipcode, level) VALUES (?, ?, ?, ?, ?, ?)", data)
        self.connection.commit()

    def delete_Member(self, member_id):
        data = [member_id]
        self.cursor.execute("DELETE FROM members WHERE rowid = ?", data)
        self.connection.commit()
       
    def edit_Member(self, member_id, name, email, phone, birthday, zipcode, level):
        data = [name, email, phone, birthday, zipcode, level, member_id]
        self.cursor.execute("UPDATE members SET name = ?, email = ?, phone = ?, birthday = ?, zipcode = ?, level = ? WHERE rowid = ?;", data)
        self.connection.commit()

### row_factory , sqlite3 and python3 tuples to dictionaries stuff...
