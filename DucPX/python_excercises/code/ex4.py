# tôi thích lập trình
file_name = 'test.txt'

f = open(file_name, mode='r')
data = f.read()

li = data.split("\t")
print(li)

for i in data:
	print(i, end = '')