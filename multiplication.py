import sys #read command line argument
import unittest

def kakezan(a,b):
# Display the multiplication table
	for i in range(1,b+1):
		for j in range(1,a+1):
			print(i*j, end=' ')
		print()

def tashizan(a,b):
# Display the addition table
	for i in range(1,b+1):
		for j in range(1,a+1):
			print(i+j, end=' ')
		print()

def main():
#command line argument
# 'a' = addition 'm' = multipulication
    args = sys.argv[1]
    #load numbers from command line
    x=int(input('x: '))
    y=int(input('y: '))
    print(2)
    if args == 'm':
        kakezan(x,y)
    else:
        tashizan(x,y)
        
if __name__ == '__main__':
    main()