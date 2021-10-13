try:
    num1= int(input("Число 1"))
    num2= int(input("Число2"))
    if num2 == 0:
        raise Exception ("Равное нулю")
    print("Результат делениея", num1/num2)
except ValueError:
    print("Некорректные данные")
except Exception as e:
    print(e)
print ("Завершино")
       
