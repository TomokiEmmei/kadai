#command line argument
# 'a' = addition 'm' = multipulication
import sys
args = sys.argv[1]


# load numbers from command line
x=int(input('X: '))
y=int(input('Y: '))

# Display the multiplication table
if args == 'm':
	for i in range(1,x+1):
		for j in range(1,y+1):
			print(i*j, end=' ')
		print()

# Display the addition table
else:
	for i in range(1,x+1):
		for j in range(1,y+1):
			print(i+j, end=' ')
		print()
