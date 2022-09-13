for i in range(10):
	print("very", end=" ")
	a1="tall"	
print("{0} lalal".format(a1))
for i in range(10):
	a1 = print("very", end=" ")
a1= str(a1)+"tall"	
print("{0} lalal".format(a1))

import datetime
def ask_yes_no(prompt): #prompt-cái sẽ in ra màn hình: "Are you male (yes/no): "
	answers_yes_list = ["yes", "y", "YES"]
	answers_no_list =["no", "n", "NO"]
	while True: #lặp các câu lệnh ở dưới liên tục, cho đến khi break đúng.
		answer=input(prompt) #"Are you male (yes/no): " = prompt
		if answer in answers_yes_list:
			return True
		elif answer in answers_no_list:
			return False
		else:
			continue #Tiếp tục quay lại câu hỏi, để user điền lại answer trong list
def cal_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = (meter) * METER_TO_FEET 
	feet = round(feet,1)
	return feet
def cal_age(THIS_YEAR, yearborn):
	return THIS_YEAR - (yearborn)
def print_height_info(is_male, height_feet, lastname): #3 TH xảy ra: nam nữ.
	if is_male ==True:
		if height_feet>=6.5:
			print("You are", end=" ")
			i=0
			while i<10: #in "very" 10 lần
				i+=1
				print("very", end=" ")
			print("tall as a man")
		elif height_feet>=6.0:
			print(lastname + " "+"is tall")
		else:
			print(lastname + " "+"is short")
	elif is_male ==False: 
		if height_feet>=6.0:
			print("You are", end=" ")
			for i in range(10):
				print("very", end=" ")
			print("tall as a woman")
		elif height_feet>=5.7:
			print(lastname + " "+"is tall")
		else:
			print(lastname + " "+"is short")
def print_person_info(firstname, lastname, age, THIS_YEAR, height_feet, is_vietnamese, is_male):#In kết quả lên màn hình
	print("\n----\n")
	print("Your name is"+" "+firstname+" "+lastname)
	print("{0}'s {1} years old in {2}".format(lastname,age,THIS_YEAR)) #Bắt đầu từ số 0
	print(lastname+"'s"+" "+str(height_feet)+" "+"feet tall")
	if is_vietnamese:
		print("You're from Vietnam")
	else:
		print("You aren't from Vietnam")
	print_height_info(is_male, height_feet, lastname)
def ask_person_info():#asking for detail from users
	firstname = input("Your first name: ")
	lastname = input("Your last name: ")
	yearborn = int(input("When you were born: "))
	height_m = float(input("Your height (m): "))
	is_male = ask_yes_no("Are you male (yes/no): ") #tương tự như hàm input, nhập số cho hàm yes_no chạy ra kq
	is_vietnamese = ask_yes_no("Are you Vietnamese (yes/no): ")
	return firstname, lastname, yearborn, height_m, is_male, is_vietnamese
def main():
	now = datetime.datetime.now()
	THIS_YEAR = now.year #constant variable (unchanged variable), written in all capital letter, this is the naming convention of constant variable
	firstname, lastname, yearborn, height_m, is_male, is_vietnamese = ask_person_info()
	age = cal_age(THIS_YEAR, yearborn)
	height_feet = cal_to_feet(height_m)
	print_person_info(firstname, lastname, age, THIS_YEAR, height_feet, is_vietnamese, is_male)
main()

def ted():
	print("hdhdh")

