my_dict = {'key':'value', 'key2':'value2'}
print(my_dict)
print(my_dict['key'])
d = {'k1':123,'k2':['a','b','c'],'k3':{'insidekey':100}}
print(d)
print(d['k1'])
print(d['k2'][1])
print(d['k3']['insidekey'])
d['k2'][0]= 'new VALUE'
print(d['k2'][0])
print(d.values())
print(d.items())

