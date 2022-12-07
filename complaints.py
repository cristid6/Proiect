"""Un client are nevoie de un soft pentru a gestiona mai usor reclamatiile clientilor.
Va trebuie sa implementezi un caiet de reclamatii digital.

Acest caiet are urmatoarele functionalitati:

- adaugare reclamatie
- vezi toate reclamatiile ne-rezolvate
- marcheaza o reclamatie ca "rezolvata"

NOTE:
1. fiecare reclamatie, pe langa reclamatia in sine, trebuie sa retina data la care a fost
creata si numele reclamatului.
2. fiecare reclamatie va primi un ID unic pentru a fi identificata."""

import sqlite3


class Database:
    """Connection with complaints database and some methods for adding, selecting and updating info."""

    def __init__(self):
        self.connection = sqlite3.connect("complaints_database.db")
        self.cur = self.connection.cursor()
        self.create_table = self.cur.execute(
            """CREATE TABLE IF NOT EXISTS complaints (
            id_reg INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            complaint_title TEXT NOT NULL,
            complaint_description TEXT NOT NULL,
            register_datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
            status INTEGER DEFAULT 0
            );
            """)

    def add_complaint(self, first_name, last_name, complaint_title, complaint_description):
        """Add complaint (requires first name, last_name, complaint title, complaint description)"""
        self.cur.execute("""INSERT INTO complaints(first_name, last_name, complaint_title, complaint_description) VALUES (?, ?, ?, ?);""",
                         (first_name, last_name, complaint_title, complaint_description))
        self.connection.commit()

    def select_complaint(self, id_reg):
        """Select complaint by id_reg (requires id_reg)"""
        select = self.cur.execute("""SELECT * FROM complaints WHERE id_reg=?;""", (id_reg,))
        print(select.fetchall())

    def select_all(self):
        """Select all complaints"""
        select = self.cur.execute("""SELECT * FROM complaints;""")
        print(select.fetchall())

    def select_0(self):
        """Select all complaints where id_reg is unresolved"""
        select = self.cur.execute("""SELECT * FROM complaints WHERE status=0;""")
        print(select.fetchall())

    def select_1(self):
        """Select all complaints where id_reg is resolved"""
        select = self.cur.execute("""SELECT * FROM complaints WHERE status=1;""")
        print(select.fetchall())

    def modify_status(self, id_reg, status):
        """Update complaint status by id_reg (requires id)"""
        self.cur.execute("""UPDATE complaints SET status=? WHERE id_reg=?;""", (status, id_reg))
        self.connection.commit()
        print(f"Complaint with id {id_reg} updated with status {status}.")

    def get_max_id(self):
        """Get max id_reg from complaints"""
        max_id = self.cur.execute("""SELECT max(id_reg) FROM complaints""")
        return max_id.fetchall()[0][0]
