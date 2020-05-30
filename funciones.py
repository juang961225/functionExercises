#Diseñe un algoritmo que permita leer N cantidad de números y saque el numero mayor y el numero menor del array

#variable declaration...
arrayNumbers = []
#end of variable declaration

#function declarations....
def askNumber():
    number = input('Porfavor digite un numero: ')
    return number

def upperNumber():
    auxNumber = arrayNumbers[0]
    for number in arrayNumbers:
        if auxNumber <= number:
            auxNumber = number
        else:
            continue
    return auxNumber

def lessNumber():
    auxNumber = arrayNumbers[0]
    for number in arrayNumbers:
        if number <= auxNumber:
            auxNumber = number
        else:
            continue
    return auxNumber

def validationNumber(number):
    try:
        validate = float(number)
        return validate
    except ValueError:
        print(number, " Eso no es un numero. vuelva a intentar")
        return True

def whileAllowNumber(validation):
    while validation:
        number = askNumber()
        validation = validationNumber(number)
        if validation == True:
            continue
        else: 
            number = validation
        validation = askToContinue()
        arrayNumbers.append(number)
    #end of the while

        
def askToContinue():
    ask = input('Desea seguir digitando numeritos?... Y/N: ')
    if ask == 'Y':
        return True
    elif ask == 'y':
        return True
    elif ask == 'yes':
        return True
    elif ask == 'Yes':
        return True
    else:
        return False

#end of functions declaration.

#code of this class start here...
whileAllowNumber(True)
upperNumber = upperNumber()
lessNumber = lessNumber()

print('El algoritmo ha finalizado...')
print('la lista de numeros que ingresaste es: ', arrayNumbers)
print('el numero mayor es: ', upperNumber, ' y el numero menor es: ', lessNumber)
#end of the code class here.