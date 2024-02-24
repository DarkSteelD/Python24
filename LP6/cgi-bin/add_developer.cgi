#!C:\Users\DarkStell\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import cgitb
import sqlite3
cgitb.enable() 
print("Content-type: text/html\n")
print()
form = cgi.FieldStorage()
name = form.getvalue('name')
country = form.getvalue('country')
birth = form.getvalue('birth')
salary = form.getvalue('salary') or 0  
last_company = form.getvalue('last_company')
try:
    conn = sqlite3.connect('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP6\\db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Developers (Name, Country, Birth, Salary, LastCompany) 
                      VALUES (?, ?, ?, ?, ?)''', (name, country, birth, salary, last_company))
    conn.commit() 
    print("<html>")
    print("<head>")
    print("<title>Developer Added</title>")
    print("</head>")
    print("<body>")
    print("<h1>Developer successfully added!</h1>")
    print("</body>")
    print("</html>")
except sqlite3.Error as e:
    print("<p>Error: {}</p>".format(e))
finally:
    if conn:
        conn.close()
