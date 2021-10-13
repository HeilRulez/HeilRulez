try :
	gender = int (input('Ваш пол:\n1 - Мужской.\n2 - Женский.\n'))
	if ((gender != 1) and (gender != 2)):
		raise ValueError()
	age = int (input ('Введите Ваш возраст: '))
	if ((age <= 0) or (age > 150)):
		raise ValueError()
	growth = int(input('Введите Ваш рост с сантиметрах: '))
	if ((growth < 40) or (growth > 300)):
		raise ValueError()
	if (gender == 1):
		  print ('Дла определения типа тела, измерьте запястье.\nАстенический < 17 см.\nНормостенический 17-20 см.\nГипепстенический > 20 см.\n')
	elif (gender == 2):
		print ('Дла определения типа тела, измерьте запястье.\nАстенический < 16 см.\nНормостенический 16-18 см.\nГипепстенический > 18 см.\n')
	typeBody = input ('Ваш тип тела:\n1 - Астенический.\n2 - Нормостенический.\n3 - Гиперстенический.\n')
	if ((typeBody != '1') and (typeBody != '2') and (typeBody != '3')):
		raise ValueError()
except ValueError:
	print ('Введены неверные данные.')
cof =0
if (growth <= 165):
	cof = 100
elif (growth > 165) and (growth <= 175):
	cof = 105
elif (growth > 175):
	cof = 110
out = (growth - cof)
cofAge = 0
if (age >= 20) and (age <= 30):
	cofAgeIndex = 1
	cofAge = 0.11
elif (age > 50):
	cofAge = 0.06
	cofAgeIndex = 2
elif (age < 20) or ((age > 30) and (age <= 50)):
	cofAgeIndex = 0
if (cofAgeIndex == 1) and (typeBody == '1'):
	weight = out - (out*cofAge) - (out*0.1)
elif (cofAgeIndex == 2) and (typeBody == '1'):
	weight = out + (out*cofAge) - (out*0.1)
elif (cofAgeIndex == 1) and (typeBody == '2'):
	weight = out - (out*cofAge)
elif (cofAgeIndex == 1) and (typeBody == '3'):
	weight = out - (out*cofAge) + (out*0.1)
elif (cofAgeIndex == 2) and (typeBody == '2'):
	weight = out + (out*cofAge)
elif (cofAgeIndex == 2) and (typeBody == '3'):
	weight = out + (out*cofAge) + (out*0.1)
elif (cofAgeIndex == 0) and (typeBody == '1'):
	weight = out - (out*0.1)
elif (cofAgeIndex == 0) and (typeBody == '2'):
	weight = out
elif (cofAgeIndex == 0) and (typeBody == '3'):
	weight = out + (out*0.1)
print('Согласно исследованиям Поля Брока, Ваш идеальный вес: ', weight, 'киллограм.')
