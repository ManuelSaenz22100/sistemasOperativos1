from abc import ABC, abstractclassmethod

class DispositivoElectronico(ABC):
    def __init__(self, marca:str) -> None:
        super().__init__()
        self.marca = marca
    
    @property
    def marca(self) -> str:
        return self.__marca
    
    @marca.setter
    def marca(self, marca:str):
        if not isinstance(marca, str):
            raise TypeError("Marca debe ser tipo str")
        self.__marca = marca

    @abstractclassmethod
    def on(self):
        pass

    @abstractclassmethod
    def off(self):
        pass

    def __str__(self) -> str:
        return f"dispositivo: {self.marca}."

class Celular(DispositivoElectronico):
    def __init__(self, marca:str, precio:float) -> None:
        super().__init__(marca)
        self.precio = precio
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        if not isinstance(precio, float):
            raise TypeError("El precio debe ser un numero")
        if precio<0:
            raise ValueError("Precio debe ser mayor a cero")
        self.__precio = precio

    def on(self):
        return "Prendiendo celular..."
    
    def off(self) -> str:
        return "Apagando celular..."
    
    def llamar(self) -> str:
        return "Llamando..."
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nPrecio: {self.precio}"

class Television(DispositivoElectronico):
    def __init__(self, marca:str, canales:int) -> None:
        super().__init__(marca)
        self.canales = canales
    
    @property
    def canales(self):
        return self.__canales
    
    @canales.setter
    def canales(self, canales):
        if not isinstance(canales, (int)):
            raise TypeError("Canales debe ser tipo int")
        if canales < 0:
            raise ValueError("Los cnales no pueden ser menor a 0")
        self.__canales = canales


    def on(self):
        return f"Prendiendo..."

    def off(self):
        return f"Apagando..."
        
    def Vernetflix(self):
        print ("Viendo Netflix...")
    
    def __str__(self) -> str:
        return f"{super().__str__()}\Canales: {self.canales}"


#main
final = Celular(marca="Iphone", precio=float(20000)) 
print("Trabajo Dispositvos Electronicos")
print(final.on())
print(final.llamar())
print(final.off())









    




