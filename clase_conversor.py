#clase conversor de temperatura

class Conversor:
    def __init__(self):
        self.__temperatura = 0
        self.__unidades = "centigrados"
        self.__registro = []
        
    def __str__(self):
        return "Tenemos {} grados {}".format(self.__temperatura, self.__unidades)

    def temperatura(self, valor = None):
        if valor == None:
            return self.__temperatura
        else:
            self.__temperatura = valor
            
    def unidad(self):
        return self.__unidades
    
    def registro(self):
        return self.__registro
    
    def cantidad(self):
        return len(self.__registro)
    
    #en temperatura introducimos el valor a convertir
    #en caso de no introducir
    #en unidades seleccionamos la unidad en la que viene
    #el dato de temperatura 0 centigrados 1 farenheit
    def conversion(self, unidades = None, temperatura = None):
        if unidades == None:
            if self.__unidades == "centigrados":
                unidades = 0
            elif self.__unidades == "farenheit":
                unidades = 1
        if temperatura == None:
            temperatura = self.__temperatura
        
        if unidades == 0:
            self.__temperatura = (temperatura * (9/5)) + 32
            self.__unidades = "farenheit"
            self.__registro.append("centigrados a farenheit")
        elif unidades == 1:
            self.__temperatura = (temperatura - 32) * (5/9)
            self.__unidades = "centigrados"
            self.__registro.append("farenheit a centigrados")
        
        