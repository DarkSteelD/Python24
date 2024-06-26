import sqlite3
try:
    conn = sqlite3.connect('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP6\\db.sqlite')
    cursor = conn.cursor()
    # cursor.execute('''CREATE TABLE IF NOT EXISTS Developers (
    #                     ID INTEGER PRIMARY KEY,
    #                     Name TEXT NOT NULL,
    #                     Country TEXT NOT NULL,
    #                     Birth DATE NOT NULL,
    #                     Salary INTEGER,
    #                     LastCompany TEXT)''')
    # cursor.execute('''CREATE TABLE IF NOT EXISTS Software (
    #                     ID INTEGER PRIMARY KEY,
    #                     Name TEXT NOT NULL,
    #                     Version TEXT NOT NULL,
    #                     DeveloperID INTEGER,
    #                     FOREIGN KEY (DeveloperID) REFERENCES Developers(ID))''')

    # cursor.execute('''CREATE TABLE IF NOT EXISTS Licenses (
    #                     ID INTEGER PRIMARY KEY,
    #                     LicenseType TEXT NOT NULL,
    #                     SoftwareID INTEGER,
    #                     ExpiryDate DATE,
    #                     CHECK(ExpiryDate >= '2024-02-23'),
    #                     FOREIGN KEY (SoftwareID) REFERENCES Software(ID))''')
    # cursor.execute('''CREATE TABLE IF NOT EXISTS Сompanies (
    #                     ID INTEGER PRIMARY KEY,
    #                     Name TEXT NOT NULL,
    #                     Licenses INTEGER,
    #                     Employees INTEGER,
    #                     Projects INTEGER,
    #                     FOREIGN KEY (Licenses) REFERENCES Licenses(ID),
    #                     FOREIGN KEY (Employees) REFERENCES Developers(ID),
    #                     FOREIGN KEY (Projects) REFERENCES Software(ID))''')
    # query = '''INSERT INTO Developers (Name, Country, Birth, Salary, LastCompany) 
    #         VALUES (?, ?, ?, ?, ?)'''
    # values = [ ('Василий', 'Россия', '1970-12-01', 120000, 'Google'),
    #     ('Кирилл', 'Россия', '1998-05-13', None, None),
    #     ('John', 'Россия', '2000-05-13', 170000, 'Yandex') ]
    # cursor.executemany(query, values)
    # cursor.execute('''INSERT INTO Software (Name, Version, DeveloperID) VALUES ('Docs', '3.4', 1)''')
    # cursor.execute('''INSERT INTO Software (Name, Version, DeveloperID) VALUES ('Алиса', '2.1', 3)''')
    # cursor.execute('''INSERT INTO Licenses (LicenseType, SoftwareID, ExpiryDate) VALUES ('GPL', 1, '2002-12-31')''')
    # cursor.execute('''INSERT INTO Licenses (LicenseType, SoftwareID, ExpiryDate) VALUES ('BSD', 2, '2000-06-30')''')
    conn.commit()
    # cursor.execute('''SELECT * FROM Developers LIMIT 10''')
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    # Найти все программные продукты, которые разработаны
    # российскими разработчиками и имеют лицензию, истекающую после
    # 2025 года, включая имя программного продукта,
    # имя разработчика и дату истечения лицензии.    
    # Решил поиграться
    # cursor.execute('''SELECT * FROM Developers 
    #                JOIN Software ON Software.DeveloperID = Developers.ID
    #                JOIN Licenses ON Software.ID =  Licenses.SoftwareID
    #                WHERE Country = 'Россия' and ExpiryDate >= '2025-12-30' ''')
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    # cursor.execute('''SELECT AVG(Salary) AS AverageSalary
    #                 FROM Developers; ''')
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    conn.close()
except sqlite3.Error as e:
    conn.rollback()
    print(f"An error occurred: {e}")