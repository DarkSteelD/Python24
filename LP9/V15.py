import pandas
import re
df = pandas.read_csv('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP9\\15 - 1.csv')
counter = 0
Atime = input("Введите требуемое время в формате ХХ мин. УУ сек.")
def time_sec(str):
    if pandas.isnull(str):
        return 0
    else:
        match = re.match(r'(\d+) мин. (\d+) сек.', str)
        if match:
            minutes, seconds = match.groups()
            return int(minutes) * 60 + int(seconds)
    return 0
needed_t = time_sec(Atime)
for i in range(len(df)):
    themes = [(10, 11), (12, 13), (14, 15), (16, 17), (18, 19)]
    failed_on = all((df.iloc[i, j].split(',')[0] == '0' and df.iloc[i, k].split(',')[0] == '0') for j, k in themes)
    passed = int(df.iloc[i]["Оценка/10,00"].split(',')[0])>= 6
    if passed and failed_on and time_sec(df.iloc[i][8])<needed_t:
        counter +=1
print(counter)