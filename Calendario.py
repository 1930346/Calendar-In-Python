import os 
from io import open

class Calendario(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
        pass

    #SETTERS -----------------
    def setDay(self,day):
        self.day = day
        pass
    def setMonth(self,month):
        self.month = month
        pass
    def setYear(self,year):
        self.year = year
        pass
    #SETTERS ----------------
    
    #GETTERS ----------------
    def getDay(self):
        return (self.day)
    def getMonth(self):
        return (self.month)
    def getYear(self):
        return (self.year)
    #GETTERS ------------------

    def isBisiesto(self, year):
        if(year%400 == 0 or (year%100!=0 and year%4 ==0)):
            #print("ES bisiesto")
            return 1
        return 0

    def getDiaSemana(self, day):
        nombreDia = ["Domingo","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        return nombreDia[day]
    
    def getCoeficienteMes(self,month):
        meses = {1:6, 2:2, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
        return meses[month]

    def getDaysOfMonth(self,month):
        numeroMeses = {1:31, 2: 29 if self.isBisiesto(self.getYear()) else 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        return numeroMeses[month]

    def getNombreMes(self,month):
        meses = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
        return meses[month]
    
    def crearNota(self,texto):
        nota = open("notas.txt","a")
        if(len(texto) > 1):
            nota.write(str(self.getDay()) + " de " + str(self.getNombreMes(self.getMonth())) + ": " + texto + "\n")
        nota.close()


    def printMonth(self):
        contador = 0
        nota = open("notas.txt","r")
        contenido = nota.readlines()

        while(1):
            #os.system('clear')
            if(self.getMonth() == 12 and contador == 1):
                contador = -11
                self.setYear(self.getYear()+1)
            elif(self.getMonth() == 1 and contador == -1):
                contador = 11
                self.setYear(self.getYear()-1)
            
            self.setMonth(self.getMonth()+contador)
            print("-------------------------------")
            print("\t   %.3s, %s" % (self.getNombreMes(self.getMonth()), self.getYear()))
            print("-------------------------------")
            print("   S   M   T   W   T   F   S")
            self.setDay(1) 
            inicio = self.getNombreDiaBaseFecha()
            print("    " * inicio, end="")
            for i in range(self.getDaysOfMonth(self.getMonth())):
                if((i+inicio)%7 == 0):
                    print()

                diaConNota = False
                for j in contenido:
                    ji = j.split()
                    if str(i+1) + " de " + self.getNombreMes(self.getMonth()) + ": " in j and ji[0] == str(i+1):
                        diaConNota = True
                    
                if diaConNota:
                    print("\033[;34m" + "  %2s" % str(i+1), end="")
                else:
                    print("\033[;37m"+"  %2s" % str(i+1), end="")

            print()
            eleccion = input("\033[;37m" + "Presione \"N\" para avanzar un mes y \"Q\" para retroceder. \"V\" Para ver las notas \"E\" para salir: ")
            if(eleccion == "n" or eleccion == "N"):
                contador = 1
            elif(eleccion == "q" or eleccion == "Q"):
                contador = -1
            elif(eleccion == "e" or eleccion == "E"):
                break
            elif(eleccion == "v" or eleccion == "V"):
                print("\nNotas:")
                hayNota = False
                for s in contenido:
                    if self.getNombreMes(self.getMonth()) in s:
                        hayNota = True
                        print(s, end="")
                if not hayNota:
                    print("No hay notas en este mes")
                input("Presiona enter para continuar")
                contador = 0
            else:
                contador = 0
                print("Opcion no existente")
                break
            

    def getNombreDiaBaseFecha(self):

        if (self.year >= 2000):
            coeficientes = (int(self.year/100) - 20 ) * (-2) 
        elif(self.year <= 1999):
            coeficientes = (20 - int(self.year/100)) * (2) - 1

        if(self.isBisiesto(self.year) == 1 and (self.month == 1 or self.month == 2)):
            coeficientes = coeficientes - 1

        coeficientes = coeficientes + int(str(self.year)[-2:]) +  int((int(str(self.year)[-2:])/4)) + self.getCoeficienteMes(self.month) + self.day
        
        
        if(coeficientes < 0):
            coeficientes = coeficientes * -1
        while coeficientes > 6:
            coeficientes %= 7
        
        return coeficientes




    def menu(self):
        
        while(1):
            
            print("1. Obtener el día de la semana en base a la fecha")
            print("2. Mostrar todos los días en base a un mes y año")
            print("3. Hacer una nota para un dia especial")
            print("4. Salir")
            opcion = int(input("Elija una opción: "))

            if(opcion == 1):
                #os.system('clear')
                try:
                    os.system('clear')
                    while(1):
                        
                        self.setDay(int(input("Ingrese el dia en DD: ")))
                        if(self.getDay() >= 1 and self.getDay() <= 31):
                            self.setMonth(int(input("Ingrese el mes en MM: ")))
                            if(self.getMonth() >= 1 and self.getMonth() <= 12):
                                self.setYear(int(input("Ingrese el año en YYYY: ")))
                                if(self.getYear() >= 1600):
                                    if(self.getDay() >= 1 and self.getDay() <= self.getDaysOfMonth(self.getMonth())):
                                        print("El dia de la semana es: ", self.getDiaSemana(self.getNombreDiaBaseFecha()))
                                        break
                                    else:
                                        print("Fecha inválida")
                                else:
                                    print("Fecha inválida")
                            else:
                                print("Fecha inválida")
                        else:
                            print("Fecha inválida")
                except:
                        print("Fecha inválida")
            elif (opcion == 2):
                #os.system('clear')
                try:
                    #os.system('clear')
                    while(1):
                        os.system('clear')
                        self.setMonth(int(input("Ingrese el mes en MM: ")))
                        if(self.getMonth() >= 1 and self.getMonth() <= 12):
                            self.setYear(int(input("Ingrese el año en YYYY: ")))
                            if(self.getYear() >= 1600):
                                print("El mes tiene: ", self.getDaysOfMonth(self.getMonth()) , " dias")
                                self.printMonth()
                                break
                            else:
                                print("Fecha inválida")
                        else:
                            print("Fecha inválida")
                except:
                    print("Fecha inválida")
            elif (opcion == 3):
                #os.system('clear')
                try:
                    os.system('clear')
                    while(1):
                        os.system('clear')
                        self.setDay(int(input("Ingrese el dia en DD: ")))
                        if(self.getDay() >= 1 and self.getDay() <= 31):
                            self.setMonth(int(input("Ingrese el mes en MM: ")))
                            if(self.getMonth() >= 1 and self.getMonth() <= 12):
                                self.crearNota(input("Descripción del evento: "))
                                break
                            else:
                                print("Fecha inválida")
                        else:
                            print("Fecha inválida")
                except:
                    print("Fecha inválida")
            elif (opcion == 4):
                exit()
                break
            else:
                print("Opcion no existente\n")