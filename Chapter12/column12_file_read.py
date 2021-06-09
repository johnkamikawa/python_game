file = open("test.txt", 'r')
rl = file.readlines()
file.close()
for i in rl:
	print(i.rstrip("\n"))