##5. Crear un Algoritmo que solicite el nombre de una persona, su estatura en centímetros y su peso en kilogramos. Con estos datos calcular el índice de masa corporal (IMC), determinar el estado nutricional de la persona, de acuerdo a la tabla ESTADO NUTRICIONAL, y mostrar en pantalla el siguiente mensaje:

#“Hola “ + <<Nombre solicitado>> + “ su índice de masa corporal es ” + <<IMC Calculado>> + “Su estado Nutricional es “ + <<Estado nutricional>>
#NOTA1: La fórmula para calcular el IMC está dada por
#𝐼𝑀𝐶= 𝑃𝐸𝑆𝑂/𝐸𝑆𝑇𝐴𝑇𝑈𝑅𝐴^2

#variable declaration...

#end of variable declaration

#function declarations....
def askVariable(message):
    variableReturn = input(message)
    return variableReturn

def numbersValidation(variable):
    try:
        variableValue = float(variable)
        return (variableValue)
    except ValueError:
            print(variable, 'no son valores operables, por favor utilice solo números')
            return True

def imcCalculate(statureValue, weigthValue):
    IMC = (weigthValue/(statureValue**2))
    return IMC

def whileErrorNumbers(validation):
    while validation:
        heigth = askVariable('Porfavor digite su estatura en metro y utilice punto pra los decimales: ')
        weigth = askVariable('Porfavor digite su peso en kilogramos: ')
        
        value = numbersValidation(heigth)
        value2 = numbersValidation(weigth)
        IMC = imcCalculate(value, value2)
        print('señor/señora', name, ' su indice de masa muscular es de: ', IMC )
        if validation == value:
            continue
        else:
            validation = False
    #end of the while

#end of functions declaration.
    
#code of this class start here...

name = askVariable('Porfavor digite su nombre: ')
whileErrorNumbers(True)