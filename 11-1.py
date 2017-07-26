import os
str1 = os.getcwd()
os.chdir('data')
str = os.listdir()
print(str1, str)
oppas_file = open('oppa.txt', 'r')
for my_oppa in oppas_file:
	print(my_oppa, end='')

oppas_file.close()
#######################################
oppas_file = open('oppa.txt', 'r+')
while(1):
	temp = input()
	if(temp == 'q'):break
	oppas_file.write(' '+temp+'\n')

tmp = oppas_file.read() # here, the parameter must be 'r', or it will only read a enter.

print(type(tmp), tmp, sep='\n')
oppas_file.close()
print(oppas_file.closed)
