print("COUNTDOWN TIMER SIMULATOR")
start = eval(input("Enter when to start the countdown--> "))
for unagi in range(start,0 , -1):
	if unagi <=20 and unagi >=16:
		print(unagi,"- please wait")
	elif unagi <=15 and unagi >=10 :
		print(unagi,"- waiting")
	elif unagi <=9 and unagi >=5:
		print(unagi,"- almost there")
	elif unagi <=4 and unagi >=2:
		print(unagi,"- you ready?")
	elif unagi == 1 :
		print("- ready for ...")
print("Liftoff!!")