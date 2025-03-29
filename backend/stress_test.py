import requests
import time
import random
from datetime import datetime, timedelta

API_URL = "http://localhost:5000/api/alumnos/generar-masivos"

def run_stress_test(registros=1000):
    start_time = time.time()
    
    response = requests.post(API_URL, json={"cantidad": registros})
    
    end_time = time.time()
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nPrueba completada: {registros} registros")
        print(f"Tiempo total: {data['tiempo_total']:.2f} segundos")
        print(f"Registros por segundo: {data['registros_por_segundo']:.2f}")
        print(f"Tiempo de ejecución local: {end_time - start_time:.2f} segundos")
    else:
        print(f"Error en la prueba: {response.text}")

if __name__ == "__main__":
    print("Seleccione cantidad de registros para prueba de estrés:")
    print("1. 1,000 registros")
    print("2. 3,000 registros")
    print("3. 5,000 registros")
    print("4. Personalizado")
    
    option = input("Opción: ")
    
    if option == "1":
        run_stress_test(1000)
    elif option == "2":
        run_stress_test(3000)
    elif option == "3":
        run_stress_test(5000)
    elif option == "4":
        registros = int(input("Ingrese cantidad de registros: "))
        run_stress_test(registros)
    else:
        print("Opción no válida")