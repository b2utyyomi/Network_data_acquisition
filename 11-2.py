friend_file = open('/media/hadoop/TAEKWOON/PYTHON/data/friend.txt', 'w+')
for friend_count in range(1, 7+1):
	friend = input('Please input friend name: ')
	friend += '\n'
	friend_file.write(friend)
	friend_count += 1
friend_file.seek(0)
for friend in friend_file:
	print(friend, end='')
friend_file.close()
print(friend_file.closed)
