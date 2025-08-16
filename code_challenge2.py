n1 = 1000
n2 = 800
n3 = 600
n4 = 400
n5 = 200
n6 = 100
n7 = 50
n8 = 10
n9 = 5
n10 = 1

denum = eval(input("Enter the amount to deposit --->  "))
print ("here is the breakdown of the deposit amount : ")
# b1 = demun // n1   

b1 = denum // n1
denum = denum % n1
b2 = denum  // n2
denum = denum % n2
b3 = denum // n3
denum = denum % n3
b4 = denum // n4
denum = denum % n4
b5 = denum // n5
denum = denum % n5
b6 = denum // n6
denum = denum % n6
b7 = denum // n7
denum = denum % n7
b8 = denum // n8
denum = denum % n8
b9 = denum // n9
denum = denum % n9
b10 = denum // n10
denum = % n10


print(b1, "-", n1)
print(b2, "-", n2)
print(b3, "-", n3)
print(b4, "-", n4)
print(b5, "-", n5)
print(b6, "-", n6)
print(b7, "-", n7)
print(b8, "-", n8)
print(b9, "-", n9)
print(b10,"-",n10)
