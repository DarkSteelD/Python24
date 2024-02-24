#!C:\Users\DarkStell\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import cgitb
import sqlite3
cgitb.enable() 
print("Content-type: text/html\n")
print()
form = cgi.FieldStorage()
name = form.getvalue('name')
version = form.getvalue('version')
developerId = form.getvalue('developerId')
try:
    conn = sqlite3.connect('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP6\\db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Software (Name, Version, DeveloperID) 
                      VALUES (?, ?, ?)''', (name, version, developerId ))
    
    conn.commit()  
    print("<html>")
    print("<head>")
    print("<title>Developer Added</title>")
    print("</head>")
    print("<body>")
    print("<h1>Software successfully added!</h1>")
    print("</body>")
    print("</html>")
except sqlite3.Error as e:
    print("<p>Error: {}</p>".format(e))
finally:
    if conn:
        conn.close()
