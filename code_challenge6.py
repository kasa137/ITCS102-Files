print("Enter 10 numbers to sum all the odd numbers ")
all = 0 
for o in range(10):
	num = float(input("Enter any number---> "))
	if num % 2 != 0:
		all += num
print("The sum of all odd numbers is ",num)
		