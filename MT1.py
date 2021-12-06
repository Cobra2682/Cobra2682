import os, json, time, urllib, requests, threading
global Choice, Invalid
def Menu():
	os.system("clear")
	global Choice
	Choice = int(input("""- - - - Multi-Tool!
- - - By Cobra
- - Choose an option:
1. Calculator
2. Website Checker
3. Fastping
4. IP Geolocation
5. Exit
- Choice: """))
	Check()
def Check():
	global Invalid
	Invalid = 0
	Check = str(input("Are you sure? (True/False): "))
	if Check == "True":
		print("Option", Choice, "selected and confirmed.")
		time.sleep(1)
		os.system("clear")
	elif Check == "False":
		Menu()
	else:
		print("Invalid response received.")
		time.sleep(1)
		Invalid = 1
Menu()
while Invalid == 1:
	Menu()
Invalid = 0
def Calculator():#																Script Functions
	Invalid = 1
	while Invalid == 1:
		os.system("clear")
		Operator = str(input("""- Calculator!
Enter + for addition
Enter - for subtraction
Enter * for multiplication
Enter / for division
- Operator: """))
		if Operator == "+":
			N1 = int(input("Enter first number: "))
			N2 = int(input("Enter second number: "))
			Ans = N1 + N2
			Invalid = 0
		elif Operator == "-":
			N1 = int(input("Enter first number: "))
			N2 = int(input("Enter second number: "))
			Ans = N1 - N2
			Invalid = 0
		elif Operator == "*":
			N1 = int(input("Enter first number: "))
			N2 = int(input("Enter second number: "))
			Ans = N1 * N2
			Invalid = 0
		elif Operator == "/":
			N1 = int(input("Enter first number: "))
			N2 = int(input("Enter second number: "))
			Ans = N1 / N2
			Invalid = 0
		else:
			print("Invalid response received.")
			time.sleep(1)
	print("Your answer for", N1, Operator, N2 , "=", str(Ans)+"!")
def WebChecker():
	Invalid = 1
	while Invalid == 1:
		os.system("clear")
		print("Website Checker!")
		URL = str(input("Enter any URL: "))
		WebStatus = urllib.request.urlopen(URL).getcode()
		WebsiteUp = WebStatus == 200
		print(WebsiteUp)
		if WebsiteUp == True:
			print("The website is up and running! (Code = 200)")
		else:
			print("The website seems to be down... (Code =", str(WebStatus)+")")
		Invalid = 0
def Fastping():
	Invalid = 1
	while Invalid == 1:
		os.system("clear")
		print("- Fastping!")
		print("To stop this program, press CTRL-C, and type True/False to determine if the process gets repeated.")
		global Host
		Host = str(input("Enter IP or hostname to start TCP conversation: "))
		Layers = int(input("Enter how many ping instances you would like to perform: "))
		Invalid = 0
		def Fastpinger():
			global Host
			os.system("ping " + Host)		
		ThreadsList = []
		for Layer in range(Layers):
			Threader = threading.Thread(target=Fastpinger)
			ThreadsList.append(Threader)
			Threader.start()
def IPGeolocation():
	Invalid = 1
	while Invalid == 1:
		os.system("clear")
		print("IP Geolocation!\nInfo - if an IP address that you have requested to track is not found, the json\ndata will show your public IP info instead.")
		IPInput = str(input("Enter IPv4 address to gelocate (IPv6 Untested): "))
		DataStep1 = requests.get("https://geolocation-db.com/jsonp/" + IPInput)
		DataStep2 = DataStep1.content.decode()
		DataStep3 = DataStep2.split("(") [1].strip(")")
		DataStep4 = json.loads(DataStep3)
		DataResult = DataStep4
		print("We searched the API and found this...\n", DataResult)
		Invalid = 0
def Exit():
	os.system("clear")
	print("Thanks for using Multi-Tool!")
	time.sleep(1)
	os.system("clear")
	print("- InsaneCobra2682")
	exit()
while Choice < 1:#																Choice Validator
	print("Invalid choice!")
	time.sleep(1)
	Menu()
while Choice > 5:
	print("Invalid choice!")
	time.sleep(1)
	Menu()
while Choice == 1:
	Calculator()
	Invalid = 1
	while Invalid == 1:
		Again = str(input("Run this program again? (True/False): "))
		if Again == "True":
			Invalid = 0
			Calculator()
			Invalid = 1
		elif Again == "False":
			Invalid = 0
			Menu()
		else:
			print("Invalid response received.")
			time.sleep(1)
while Choice == 2:
	WebChecker()
	Invalid = 1
	while Invalid == 1:
		Again = str(input("Run this program again? (True/False): "))
		if Again == "True":
			Invalid = 0
			WebChecker()
			Invalid = 1
		elif Again == "False":
			Invalid = 0
			Menu()
		else:
			print("Invalid response received.")
			time.sleep(1)
while Choice == 3:
	Fastping()
	Invalid = 1
	while Invalid == 1:
		Again = str(input("Run this program again? (True/False): "))
		if Again == "True":
			Invalid = 0
			Fastping()
			Invalid = 1
		elif Again == "False":
			Invalid = 0
			Menu()
		else:
			print("Invalid response received.")
			time.sleep(1)
while Choice == 4:
	IPGeolocation()
	Invalid = 1
	while Invalid == 1:
		Again = str(input("Run this program again? (True/False): "))
		if Again == "True":
			Invalid = 0
			IPGeolocation()
			Invalid = 1
		elif Again == "False":
			Invalid = 0
			Menu()
		else:
			print("Invalid response received.")
			time.sleep(1)
while Choice == 5:
	Invalid = 1
	while Invalid == 1:
		Confirm = str(input("Are you sure you would like to exit? (True/False): "))
		if Confirm == "True":
			Invalid = 0
			Exit()
		elif Confirm == "False":
			Invalid = 0
			Menu()
		else:
			print("Invalid response received.")
			time.sleep(1)
	
	
