"""
2018.Jan
@author: Tomoki Emmei
description: program to show multiplication and addition table
"""
import sys #read command line argument

# Display the multiplication table
def kakezan(a,b):
    Seki_tab=[[0 for i in range(a)] for j in range(b)]# array for the test
    for i in range(1,b+1):
        for j in range(1,a+1):
            print(i*j, end=' ')
            Seki_tab[i-1][j-1]=i*j #store the value
        print() #new line
    return Seki_tab

# Display the addition table
def tashizan(a,b):
    Wa_tab=[[0 for i in range(a)] for j in range(b)]# array for the test
    for i in range(1,b+1):
        for j in range(1,a+1):
            print(i+j, end=' ')
            Wa_tab[i-1][j-1]=i+j #store the value
        print() #new line
    return Wa_tab

def main():
    #command line argument 'a' -> addition table 'm' -> multipulication table
    args = sys.argv[1] 
    if args == 'm':
        #load numbers from command line
        x=int(input('x: '))
        y=int(input('y: '))
        kakezan(x,y)
    elif args == "a":
        x=int(input('x: '))
        y=int(input('y: '))
        tashizan(x,y)
    else:
        print('Caution: argument is a or m') # exception handling

if __name__ == '__main__':
    main()
