import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Developers (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Country TEXT NOT NULL,
                    Birth DATE NOT NULL,
                    Salary INTEGER,
                    LastCompany TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Software (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Version TEXT NOT NULL,
                    DeveloperID INTEGER,
                    FOREIGN KEY (DeveloperID) REFERENCES Developers(ID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Licenses (
                    ID INTEGER PRIMARY KEY,
                    LicenseType TEXT NOT NULL,
                    SoftwareID INTEGER,
                    ExpiryDate DATE,
                    CHECK(ExpiryDate >= '2024-02-23'),
                    FOREIGN KEY (SoftwareID) REFERENCES Software(ID))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Сompanies (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Licenses INTEGER,
                    Employees INTEGER,
                    Projects INTEGER,
                    FOREIGN KEY (Licenses) REFERENCES Licenses(ID),
                    FOREIGN KEY (Employees) REFERENCES Developers(ID),
                    FOREIGN KEY (Projects) REFERENCES Software(ID))''')

conn.commit()