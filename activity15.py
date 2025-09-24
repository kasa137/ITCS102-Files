print("STRING FORMATING")
print("string concatenation")
print("USING f{} method")
name = input("what is your first name --> ")
mname = input("what is your middle name --> ")
sname = input("what is your surname -->")


print(f"Your full name is {name} {mname} {sname}\n")
print("USING f{" ".upper} method")
print(f"My full name is {name.upper} {mname.upper} {sname.upper}\n")

all = 0
for yah in range(1 , 6):
	yeh = eval(input(f"{yah} - INPUT A NUMBER --> "))
	all += yeh
print(f"The total sum if {all}\n")
print("TOP 5 LIST OF YOUR FAVORITE MOVIE")
for kris in range(5, 1, -1):
	tin = input(f" TOP {kris} FAVORITE MOVIE ---> ")
print("THANK YOU FOR LISTING TOP 5 OF YOUR FAVORITE MOVIES")


