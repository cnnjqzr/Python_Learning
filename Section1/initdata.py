#record

lebron = { 'name' : 'Lebron James', 'age' : 31, 'team':'Cle', 'role' : 'sf'}
dwyane = { 'name' : 'Dwyane Wade', 'age' : 34, 'team':'Mia', 'role' : 'sg'}

#database

db = {}
db['lebron'] = lebron
db['dwyane'] = dwyane

#this period of codes is aimed to detect if the file runs
if __name__ == '__main__':
    for key in db:
        print(key,'=>\n',db[key])

