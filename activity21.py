cake = True
sum = 0
while cake == True:
	coco = input("Do you want some cake? ")
	sum += 1
	if coco == "yes":
		print("here your cake~~")
		print(f"The numbers of offering cake :",{sum} )
		break
	else :
		print("Not until you accecpt my cake >~< ")
		continue