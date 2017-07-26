student={'400A2':'KIKI', '300A4':'Jungkuk'}
student['123fg'] = 'OJimin'
key_list=student.keys()
print(key_list)
print(type(key_list))
for the_key in key_list:
	print(the_key, end=' ')
	print(student[the_key])
value_list=student.values()
print(type(value_list))
print(value_list)
value_list = sorted(value_list)
print(value_list)
