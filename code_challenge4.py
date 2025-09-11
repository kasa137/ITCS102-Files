print("Welcome to manga reader recommendation")
print("Please answer the following question to find out the right manga recommendation for you")
genre = input("What genre do you like? (Romance, Adventure, Sports): ")
duration = input("How long should the manga be? (short, medium, Long): ")
decade = input("Which decade? (2000s, 2010s): ") 
i = ("I would like to recommend you ")
a = ("Invalid input")
b = ("Please try again")

if genre == 'romance' or genre == 'Romance' :
    if duration == 'short' or duration == 'Short' :
        if decade == '2000s' or decade == '2000' :
        	print(i,"Bara no Tame, Millennuim Show, Absolute Boyfriend")
        elif decade == '2010s' or decade == '2010':
        	print(i,"My Love Story, The girl with sanpaku eye")
    elif duration == "Medium" or duration == "medium":
        if decade == '2000s' or decade == '2000':
            print(i, "lagyan mo 'to, nalumutan mo ata") 
        elif decade == '2010s' or decade == '2010' :
            print(i,"Ao haru ride, Horimiya")
    elif duration == 'long' or duration == 'Long':
        if decade == '2000s' or decade =='2000' :
            print(i,"Fruit Basket, Ouran Highschool Host Club and Maid-sama")
        elif decade == '2010s' or decade == '2010' :
            print(i,"Kamisama Kiss")
        else: 
            print(a)
            print(b)
  
            
if genre == 'Adventure' or genre == 'adventure' :
	if duration == 'short' or duration == 'Short' :
		if decade == '2000s' or decade == '2000' :
			print(i,"All You Need Is Kill, Gyo , The Summit of the Gods")
		elif decade == '2010s' or decade == '2010s' :
			print(i,"Obata")
	elif duration == 'Medium' or duration == 'medium' :
		if decade == '2000s' or decade ==  '2000' :
			print(i,"Fullmetal Alchemist, Claymore")
		elif decade == '2010s' or decade == '2010':
			print(i,"The Promised Neverland")
	elif duration == 'long' or duration == 'Long' :
		if decade == '2000s' or decade == '2000' :
			print(i, "Bleach , Naruto")
		elif decade == '2010s' or decade == '2010' :
			print(i,"Attack on Titan, My Hero Academia, Black Clover")
            
    
if genre == 'Sports' or genre == 'sports' : 
    if duration == 'short' or duration == 'Short' :
        if decade == '2000s' or decade == '2000' :
        	print(i,"Real , Cross   ")
        elif decade == '2010s' or decade == '2010':
        	print(i," Priceless, Ginga e Kickoff!! ")
    elif duration == "Medium" or duration == "medium":
        if decade == '2000s' or decade == '2000':
            print(i,"Whistle!, Eyeshield21, The Prince of Tennis  ")
        elif decade == '2010s' or decade == '2010' :
            print(i," Haikyuu!! ")
    elif duration == 'long' or duration == 'Long':
        if decade == '2000s' or decade =='2000' :
            print(i,"sorry can't recommend a manga'  ")
        elif decade == '2010s' or decade == '2010' :
            print(i," Baby Steps, Diamond no Ace ")
        else: 
            print(a)
            print(b)