import pandas
df = pandas.read_csv('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP9\\15 - 1.csv')
counter = 0
for i in range(len(df)):
    themes = [(10, 11), (12, 13), (14, 15), (16, 17), (18, 19)]
    failed_on = all((df.iloc[i, j].split(',')[0] == '0' and df.iloc[i, k].split(',')[0] == '0') for j, k in themes)
    passed = int(df.iloc[i]["Оценка/10,00"].split(',')[0])>= 6
  


    if passed and failed_on:
        counter +=1
print(counter)