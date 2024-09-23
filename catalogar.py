
def catalogar(listaVehiculos, ruedas=None):
    # Si ruedas no es None, filtrar por número de ruedas
    if ruedas is not None:
        contador = 0
        for vehiculo in listaVehiculos:
            if hasattr(vehiculo, 'ruedas') and vehiculo.ruedas == ruedas:
                print(f"Clase: {type(vehiculo).__name__}, Atributos: " ,vehiculo)
                contador += 1
        print(f"Se han encontrado {contador} vehiculos con {ruedas} ruedas.")
    else:
        # Mostrar todos los vehículos
        for vehiculo in listaVehiculos:
            print(f"Clase: {type(vehiculo).__name__}, Atributos: " ,vehiculo)

