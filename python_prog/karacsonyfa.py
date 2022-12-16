#feladat: Karácsonyfát rajzolni * karakterekből
# def triangleShape(n):
#     for i in range(n):
#         for j in range(n-i):
#             print(' ', end=' ')
#         for k in range(2*i+1):
#             print('*',end=' ')
#         print()

# # Generating Pole Shape
# def poleShape(n):
#     for i in range(n):
#         for j in range(n-1):
#             print(' ', end=' ')
#         print('* * *')

# # Input and Function Call
# row = int(input('Enter number of rows: '))

# triangleShape(row)
# triangleShape(row)
# poleShape(row)


for a in range(10):
    for b in range(10-a):
        print(' ',end=' ')
    for c in range(2*a+1):
        print('*',end=' ')  
    print()
for a in range(10):
    for b in range(10-a):
        print(' ',end=' ')
    for c in range(2*a+1):
        print('*',end=' ')  
    print()


for i in range(10):
    for j in range(10-1):
        print(' ',end=' ')
    print('* * *')

for i in range(magassag):
    for j in range(magassag-1):
        print(' ',end=' ')
    print("***********")
    
