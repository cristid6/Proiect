import sqlite3


class Database:
    """Connection with complaints database and some methods for adding, selecting and updating info."""

    def __init__(self):
        self.connection = sqlite3.connect("complaints_database.db")
        self.cur = self.connection.cursor()
        self.create_table = self.cur.execute(
            """CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            complaint_title TEXT NOT NULL,
            complaint_description TEXT NOT NULL,
            register_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
            status INTEGER DEFAULT 0
            );
            """)

    """Add complaint (requires first name, last_name, complaint title, complaint description)"""
    def add_complaint(self, first_name, last_name, complaint_title, complaint_description):
        self.cur.execute("""INSERT INTO complaints(first_name, last_name, complaint_title, complaint_description) 
        VALUES (?, ?, ?, ?);""", (first_name, last_name, complaint_title, complaint_description))
        self.connection.commit()

    """Select complaint by id (requires id)"""
    def select_complaint(self, id):
        select = self.cur.execute("""SELECT * FROM complaints WHERE id=?;""", (id,))
        print(select.fetchall())

    """Select all complaints"""
    def select_all(self):
        select = self.cur.execute("""SELECT * FROM complaints;""")
        print(select.fetchall())

    """Select all complaints where id is unresolved"""
    def select_0(self):
        select = self.cur.execute("""SELECT * FROM complaints WHERE status=0;""")
        print(select.fetchall())

    """Select all complaints where id is resolved"""
    def select_1(self):
        select = self.cur.execute("""SELECT * FROM complaints WHERE status=1;""")
        print(select.fetchall())

    """Update complaint status by id (requires id)"""
    def modify_status(self, id, status):
        self.cur.execute("""UPDATE complaints SET status=? WHERE id=?;""", (status, id))
        self.connection.commit()
        print(f"Complaint with id {id} updated with status {status}.")

    """Get max id from complaints"""
    def get_max_id(self):
        max_id = self.cur.execute("""SELECT max(id) FROM complaints""")
        return max_id.fetchall()[0][0]
