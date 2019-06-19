# Try to find file and open it

try:
	data = open('sketch.txt')
	for each_line in data:
		# Try to iterate over file data
		try:
			(role, line_spoken) = each_line.split(':', 1) 
			print(role, end='')
			print(' said: ', end='')
			print(line_spoken, end='')
		# Except situation when line cannot be splitted correctly
		except ValueError:
			pass
	data.close()
# Except situation, when file not exists	
except IOError:
	print('File not found!')
	pass
