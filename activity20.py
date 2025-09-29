for unak in range(1,10, 1):
	for x in range(10,unak,-1):
		print("~",end=" ")
	for y in range(1, unak, 1):
		print("x",end=" ")
	for ih in range(1,unak,1):
		print("x",end=" ")
	print()
	
for ts in range(1,11,1):
	for t in range(1,ts, 1):
		print("~",end=" ")
	for san in range(10, ts, -1):
		print("x", end=" ")
	for s in range(10,ts,-1):
		print("x",end=" ")
	print()
	
	