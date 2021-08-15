my_list = [1,2,3]
my_list = ['string', 100. ,11.22]
print(len(my_list))
print(my_list[0])
print(my_list[0:2])
new_list = ['one','two','three','four']
print(new_list)
new_list[0] = 'ONE'
print(new_list)
new_list.append('six')
print(new_list)
new_list.pop()
print(new_list)
popped_item = new_list.pop(1)
print(popped_item)
print(new_list)
new_list2 = ['s','a','s','f']
new_list2.sort()
print(new_list2)
num_list = [1,12,5,7,3,67,4,2]
num_list.sort()
print(num_list)
newnum_list = num_list
newnum_list.reverse()
print(newnum_list)