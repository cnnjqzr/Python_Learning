from initdata import lebron,dwyane
import  shelve
db = shelve.open('people-shelve')
db['lebron'] = lebron
