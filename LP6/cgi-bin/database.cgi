#!C:\Users\DarkStell\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi
import sqlite3
print("Content-type: text/html\n")
print("<html><head><title>Database Results</title></head><body>")
conn = sqlite3.connect('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP6\\db.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Developers LIMIT 10")  
rows = cursor.fetchall()
print("<h1>Results from database:</h1>")
print("<ul>")
for row in rows:
    print("<li>{}</li>".format(row))
print("</ul>")
print("</body></html>")
conn.close()
