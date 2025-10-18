name = input("Enter your name---> ")
print("\nODD NUMBER SUMMATION, press 0 to stop")
unak = True
ts = 0
ihan = ""  
while unak == True:
	num = eval(input("\nInput random number --> "))
	
	if num %2 == 1:
		print("ODD NUMBER DETECTED,code continues ")
		ts += num
		ihan += str(num) + " " 
	elif num == 0:
		print("Program stops!!!")
		break
	else :
		if num % 2 == 0:
			print("EVEN NUMBER DECTECTED, code continues")
		else:
			print("invalid input")
			continue
print(f"HI {name}, the sum  of all ODD number {ts}")
print(f"ODD numbers detected included the {ihan}")