bob = ['Bob Smith',42,30000,'software']
sue = ['Sue Jones',45,40000,'hardware']
'''
print(bob[0],sue[2])
print(bob[0].split()[-1])
sue[2] *= 1.25
print(sue)
'''
people = [bob,sue]
for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20
for person in people:
    print(person[2])
NAME,AGE,PAY,JOB = range(4)
qzr = ['Qu Zhanruo',22,0,'student']
print(qzr[NAME])
print(PAY,qzr[PAY])

bob = {'name':'Bob Smith','age':42,'pay':30000,'job':'dev'}
print(bob['name'])
sue = dict(name = 'Sue Jones', age = 45, pay = 40000, job = 'hdw')
print(sue)