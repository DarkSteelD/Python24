#!C:\Users\DarkStell\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import sqlite3
print("Content-type: text/html\n")
print()
print("<html><head><title>Database Results</title></head><body>")
try:
    conn = sqlite3.connect('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP6\\db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Developers")  
    rows = cursor.fetchall()
    print("<h1>Results from database:</h1>")
    print("<ul>")
    for row in rows:
        print("<li>{}</li>".format(row))
    print("</ul>")
    cursor.execute("SELECT * FROM Software")  
    rows = cursor.fetchall()
    print("<h1>Results from database:</h1>")
    print("<ul>")
    for row in rows:
        print("<li>{}</li>".format(row))
    print("</ul>")
    cursor.execute("SELECT * FROM Licenses")  
    rows = cursor.fetchall()
    print("<h1>Results from database:</h1>")
    print("<ul>")
    for row in rows:
        print("<li>{}</li>".format(row))
    print("</ul>")
    cursor.execute("SELECT * FROM Сompanies")  
    rows = cursor.fetchall()
    print("<h1>Results from database:</h1>")
    print("<ul>")
    for row in rows:
        print("<li>{}</li>".format(row))
    print("</ul>")
except Exception as e:
    print("<p>Error: {}</p>".format(e))
    
finally:
    print("</body></html>")
    conn.close()
