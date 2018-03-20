# file in python
import codecs

file_name = 'test.txt'

def read_file():
	try:
		f = open(file_name, mode='r')
		data = f.read()
		print(data)
	except FileNotFoundError:
		print("File not found: %s"%file_name)
	finally:
		f.close()


def create_file():
	f = codecs.open(file_name, mode='w', encoding = 'utf_8')

	f.write("Tôi thích lập trình")
	f.close()

if __name__ == '__main__':
	create_file()
	read_file()