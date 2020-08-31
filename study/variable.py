# assinalar várias variáveis em uma mesma linha
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# É possível realizar operações no print
x = 5
y = 10
print(x + y)

a = "Hello World"	#str	
b = 20	#int	
c = 20.5	#float	
d = 1j	#complex	
e = ["apple", "banana", "cherry"]	#list	
f = ("apple", "banana", "cherry")	#tuple	
g = range(6)	#range	
h = {"name" : "John", "age" : 36}	#dict	
i = {"apple", "banana", "cherry"}	#set	
j = frozenset({"apple", "banana", "cherry"})	#frozenset	
k = True	#bool	
l = b"Hello"	#bytes	
m = bytearray(5)	#bytearray	
n = memoryview(bytes(5))	#memoryview

print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f,'\n',g,'\n',h,'\n',i,'\n',j,'\n',k,'\n',l,'\n',m,'\n',n)
# https://www.w3schools.com/python/python_variables.asp