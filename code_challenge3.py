name = input("What is your name?--> ")
fare = eval(input("your farefee?--->  "))
person = input("are you a student?(yes/no)--> ")
if person ==  'yes' :
	discount = fare * 0.20
	nfare = fare - discount
	print("Hi",name)
	print("your discount is",discount)
	print("your new fare is ",nfare)
else :
	print("sorry",name,"you are not eligible for a srudent discount ")