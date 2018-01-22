import sys #read command line argument

def kakezan(a,b):
# Display the multiplication table
    Seki_tab=[[0 for i in range(a)] for j in range(b)]
    for i in range(1,b+1):
        for j in range(1,a+1):
            print(i*j, end=' ')
            Seki_tab[i-1][j-1]=i*j
        print()
    return Seki_tab
    
def tashizan(a,b):
# Display the addition table
    Wa_tab=[[0 for i in range(a)] for j in range(b)]
    for i in range(1,b+1):
        for j in range(1,a+1):
            print(i+j, end=' ')
            Wa_tab[i-1][j-1]=i+j
        print()
    return Wa_tab

def main():
#command line argument
# 'a' = addition 'm' = multipulication
    args = sys.argv[1]
    #load numbers from command line
    x=int(input('x: '))
    y=int(input('y: '))
    if args == 'm':
        kakezan(x,y)
    else:
        tashizan(x,y)
        
if __name__ == '__main__':
    main()