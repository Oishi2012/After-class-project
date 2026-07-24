print('Power Series')

n = int(input("Enter the number of terms: "))

print('The power series is')

for i in range(1,n+1):
    print(i,'^',i,'=',i**i)