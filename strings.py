mystring = "hello world"
print('hello \nworld')
print('hello \tworld')
print(len(mystring))
print(mystring[1])
print(mystring[-1])
print(mystring[1:])
print(mystring[:3])
print(mystring[1:3])
print(mystring[::2])
print(mystring[::-1])
changestring = mystring[6:]
print(changestring)
changestring = 'bye ' + changestring
print(changestring * 10)
x = 'hello world'
print(x.upper())
print(x.split())
print('this is a string {}'.format('inserted'))
print('the {0} {2} {1}' .format('quick', 'fox', 'brown'))
print('the {f} {b} {f}' .format(q='quick', f='fox', b='brown'))
result = 100/777
print('the result was{r}' .format(r=result))
print('the result was{r:6.3}' .format(r=result))
name = 'jose'
print(f'his name is {name}')