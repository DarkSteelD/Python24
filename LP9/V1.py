import pandas
a = pandas.read_csv('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP9\\15 - 1.csv')
counter = 0
for i in range(len(a)):
    time_sec = (a.at["Оценка/10,00"]/100*60 + a.iloc[9]%100)
    failed_on = (bool(a.iloc[i] and a.iloc[i+1]) for i in range(11,20,2))
    passed = a.loc[i].at["Оценка/10,00"]
    if passed and time_sec < 15000 and failed_on:
        counter +=1
print(counter)