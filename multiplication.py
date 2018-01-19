# load numbers from command line
x=int(input('X: '))
y=int(input('Y: '))

# Display the multiplication table
for i in range(1,x+1):
	for j in range(1,y+1):
		print(i*j, end=' ')
	print()