import pandas
df = pandas.read_csv('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP9\\15 - 1.csv')
counter = 0
for i in range(len(df)):
    failed_on = any(df.iloc[i,j] == 0 for j in range(10, 20))
    passed = int(df.iloc[i]["Оценка/10,00"].split(',')[0])>= 6
    if passed:
        print(df.iloc[i]["Оценка/10,00"])
    if failed_on:
        print(any(df.iloc[i,j] == 0 for j in range(10, 20)))
    if passed and failed_on:
        counter +=1
print(counter)