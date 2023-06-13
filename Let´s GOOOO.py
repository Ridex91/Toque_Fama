import random as rnd
ganados = 0
perdidos = 0
jugados = 0
continuar = 1
while continuar == 1:
    print("Bienvenido a Toque y Fama")
    n = int(input("Elige el largo del número, desde 4 a 9: "))
    print("------------------------------------------------------------------------")
    cant_intentos = 1
    if (n < 4) or (n > 9):
        print("Error, Debe ingresar valores desde 4 a 9")
    else:
        print("El número ingresado por el jugador no puede contar con números repetidos")
        print("------------------------------------------------------------------------")
        a1 = rnd.randrange(1, 10)
        a2 = rnd.randrange(0, 10)
        a3 = rnd.randrange(0, 10)
        a4 = rnd.randrange(0, 10)
        a5 = rnd.randrange(0, 10)
        a6 = rnd.randrange(0, 10)
        a7 = rnd.randrange(0, 10)
        a8 = rnd.randrange(0, 10)
        a9 = rnd.randrange(0, 10)
        i = 0
        if n <= 9 and n >= 4:
            while i <= 20:
                if a2 != (a1, a3, a4, a5, a6, a7, a8, a9) and a3 != (a1, a2, a4, a5, a6, a7, a8, a9) and \
                a4 != (a1, a2, a3, a5, a6, a7, a8, a9) and a5 != (a1, a2, a3, a4, a6, a7, a8, a9) and \
                a6 != (a1, a2, a3, a4, a5, a7, a8, a9) and a7 != (a1, a2, a3, a4, a5, a6, a8, a9) and \
                a8 != (a1, a2, a3, a4, a5, a6, a7, a9) and a9 != (a1, a2, a3, a4, a5, a6, a7, a8):
                    if (a2 == a1) or (a2 == a3) or (a2 == a4) or (a2 == a5) or (a2 == a6) or (a2 == a7) or (a2 == a8) \
                        or (a2 == a9):
                        a2 = rnd.randrange(0, 10)
                    if (a3 == a1) or (a3 == a2) or (a3 == a4) or (a3 == a5) or (a3 == a6) or (a3 == a7) or (a3 == a8) \
                        or (a3 == a9):
                        a3 = rnd.randrange(0, 10)
                    if (a4 == a1) or (a4 == a2) or (a4 == a3) or (a4 == a5) or (a4 == a6) or (a4 == a7) or (a4 == a8) \
                        or (a4 == a9):
                        a4 = rnd.randrange(0, 10)
                    if (a5 == a1) or (a5 == a2) or (a5 == a3) or (a5 == a4) or (a5 == a6) or (a5 == a7) or (a5 == a8) \
                        or ( a5 == a9):
                        a5 = rnd.randrange(0, 10)
                    if (a6 == a1) or (a6 == a2) or (a6 == a3) or (a6 == a4) or (a6 == a5) or (a6 == a7) or (a6 == a8) \
                        or (a6 == a9):
                        a6 = rnd.randrange(0, 10)
                    if (a7 == a1) or (a7 == a2) or (a7 == a3) or (a7 == a4) or (a7 == a5) or (a7 == a6) or (a7 == a8) \
                        or (a7 == a9):
                        a7 = rnd.randrange(0, 10)
                    if (a8 == a1) or (a8 == a2) or (a8 == a3) or (a8 == a4) or (a8 == a5) or (a8 == a6) or (a8 == a7) \
                        or (a8 == a9):
                        a8 = rnd.randrange(0, 10)
                    if (a9 == a1) or (a9 == a2) or (a9 == a3) or (a9 == a4) or (a9 == a5) or (a9 == a6) or (a9 == a7) \
                        or (a9 == a8):
                        a9 = rnd.randrange(0, 10)
                i += 1
        if n == 4:
            codigo1 = (str(a1) + str(a2) + str(a3) + str(a4))
            A = int(input(f"Intento {cant_intentos}: "))
            A1 = ((A // 10 ** (n - 1)) % 10)
            A2 = ((A // 10 ** (n - 2)) % 10)
            A3 = ((A // 10 ** (n - 3)) % 10)
            A4 = ((A // 10 ** (n - 4)) % 10)
            A = str(A)
            i2 = 1
            while A != codigo1 and i2 < n:
                cant_famas = 0
                cant_toques = 0
                if A1 == a1:
                    cant_famas += 1
                elif (A1 == a1) or (A1 == a2) or (A1 == a3) or (A1 == a4):
                    cant_toques += 1
                if A2 == a2:
                    cant_famas += 1
                elif (A2 == a1) or (A2 == a2) or (A2 == a3) or (A2 == a4):
                    cant_toques += 1
                if A3 == a3:
                    cant_famas += 1
                elif (A3 == a1) or (A3 == a2) or (A3 == a3) or (A3 == a4):
                    cant_toques += 1
                if A4 == a4:
                    cant_famas += 1
                elif (A4 == a1) or (A4 == a2) or (A4 == a3) or (A4 == a4):
                    cant_toques += 1
                cant_intentos += 1
                if len(A) < len(codigo1) or len(A) > len(codigo1):
                    print("Error, pierdes tu jugada")
                if len(A) == len(codigo1):
                    print(f"Intento {cant_intentos - 1}: {A} Toques: {cant_toques} - Famas: {cant_famas}")
                A = int(input(f"Intento {cant_intentos}: "))
                A1 = ((A // 10 ** (n - 1)) % 10)
                A2 = ((A // 10 ** (n - 2)) % 10)
                A3 = ((A // 10 ** (n - 3)) % 10)
                A4 = ((A // 10 ** (n - 4)) % 10)
                A = str(A)
                i2 += 1
            if A == codigo1:
                print(f"Intento {cant_intentos}: {A} ¡Felicitaciones! Has acertado en {cant_intentos} intentos")
                ganados += 1
            else:
                print(f"Intento {n}: {A} - Fin del juego La secuencia era {codigo1}")
                perdidos += 1

        if n == 5:
            codigo2 = (str(a1) + str(a2) + str(a3) + str(a4) + str(a5))
            A = int(input(f"Intento {cant_intentos}: "))
            A1 = ((A // 10 ** (n - 1)) % 10)
            A2 = ((A // 10 ** (n - 2)) % 10)
            A3 = ((A // 10 ** (n - 3)) % 10)
            A4 = ((A // 10 ** (n - 4)) % 10)
            A5 = ((A // 10 ** (n - 5)) % 10)
            A = str(A)
            i2 = 1
            while A != codigo2 and i2 < n:
                cant_famas = 0
                cant_toques = 0
                if A1 == a1:
                    cant_famas += 1
                elif (A1 == a1) or (A1 == a2) or (A1 == a3) or (A1 == a4) or (A1 == a5):
                    cant_toques += 1
                if A2 == a2:
                    cant_famas += 1
                elif (A2 == a1) or (A2 == a2) or (A2 == a3) or (A2 == a4) or (A2 == a5):
                    cant_toques += 1
                if A3 == a3:
                    cant_famas += 1
                elif (A3 == a1) or (A3 == a2) or (A3 == a3) or (A3 == a4) or (A3 == a5):
                    cant_toques += 1
                if A4 == a4:
                    cant_famas += 1
                elif (A4 == a1) or (A4 == a2) or (A4 == a3) or (A4 == a4) or (A4 == a5):
                    cant_toques += 1
                if A5 == a5:
                    cant_famas += 1
                elif (A5 == a1) or (A5 == a2) or (A5 == a3) or (A5 == a4) or (A5 == a5):
                    cant_toques += 1
                cant_intentos += 1
                if len(A) < len(codigo2) or len(A) > len(codigo2):
                    print("Error, pierdes tu jugada")
                if len(A) == len(codigo2):
                    print(f"Intento {cant_intentos - 1}: {A} Toques: {cant_toques} - Famas: {cant_famas}")
                A = int(input(f"Intento {cant_intentos}: "))
                A1 = ((A // 10 ** (n - 1)) % 10)
                A2 = ((A // 10 ** (n - 2)) % 10)
                A3 = ((A // 10 ** (n - 3)) % 10)
                A4 = ((A // 10 ** (n - 4)) % 10)
                A5 = ((A // 10 ** (n - 5)) % 10)
                A = str(A)
                i2 += 1
            if A == codigo2:
                print(f"Intento {cant_intentos}: {A} ¡Felicitaciones! Has acertado en {cant_intentos} intentos")
                ganados += 1
            else:
                print(f"Intento {n}: {A} - Fin del juego La secuencia era {codigo2}")
                perdidos += 1

        if n == 6:
            codigo3 = (str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6))
            A = int(input(f"Intento {cant_intentos}: "))
            A1 = ((A // 10 ** (n - 1)) % 10)
            A2 = ((A // 10 ** (n - 2)) % 10)
            A3 = ((A // 10 ** (n - 3)) % 10)
            A4 = ((A // 10 ** (n - 4)) % 10)
            A5 = ((A // 10 ** (n - 5)) % 10)
            A6 = ((A // 10 ** (n - 6)) % 10)
            A = str(A)
            i2 = 1
            while A != codigo3 and i2 < n:
                cant_famas = 0
                cant_toques = 0
                if A1 == a1:
                    cant_famas += 1
                elif (A1 == a1) or (A1 == a2) or (A1 == a3) or (A1 == a4) or (A1 == a5) or (A1 == a6):
                    cant_toques += 1
                if A2 == a2:
                    cant_famas += 1
                elif (A2 == a1) or (A2 == a2) or (A2 == a3) or (A2 == a4) or (A2 == a5) or (A2 == a6):
                    cant_toques += 1
                if A3 == a3:
                    cant_famas += 1
                elif (A3 == a1) or (A3 == a2) or (A3 == a3) or (A3 == a4) or (A3 == a5) or (A3 == a6):
                    cant_toques += 1
                if A4 == a4:
                    cant_famas += 1
                elif (A4 == a1) or (A4 == a2) or (A4 == a3) or (A4 == a4) or (A4 == a5) or (A4 == a6):
                    cant_toques += 1
                if A5 == a5:
                    cant_famas += 1
                elif (A5 == a1) or (A5 == a2) or (A5 == a3) or (A5 == a4) or (A5 == a5) or (A5 == a6):
                    cant_toques += 1
                if A6 == a6:
                    cant_famas += 1
                elif (A6 == a1) or (A6 == a2) or (A6 == a3) or (A6 == a4) or (A6 == a5) or (A6 == a6):
                    cant_toques += 1
                cant_intentos += 1
                if len(A) < len(codigo3) or len(A) > len(codigo3):
                    print("Error, pierdes tu jugada")
                if len(A) == len(codigo3):
                    print(f"Intento {cant_intentos - 1}: {A} Toques: {cant_toques} - Famas: {cant_famas}")
                A = int(input(f"Intento {cant_intentos}: "))
                A1 = ((A // 10 ** (n - 1)) % 10)
                A2 = ((A // 10 ** (n - 2)) % 10)
                A3 = ((A // 10 ** (n - 3)) % 10)
                A4 = ((A // 10 ** (n - 4)) % 10)
                A5 = ((A // 10 ** (n - 5)) % 10)
                A6 = ((A // 10 ** (n - 6)) % 10)
                A = str(A)
                i2 += 1
            if A == codigo3:
                print(f"Intento {cant_intentos}: {A} ¡Felicitaciones! Has acertado en {cant_intentos} intentos")
                ganados += 1
            else:
                print(f"Intento {n}: {A} - Fin del juego La secuencia era {codigo3}")
                perdidos += 1

        if n == 7:
            codigo4 = (str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6) + str(a7))
            A = int(input(f"Intento {cant_intentos}: "))
            A1 = ((A // 10 ** (n - 1)) % 10)
            A2 = ((A // 10 ** (n - 2)) % 10)
            A3 = ((A // 10 ** (n - 3)) % 10)
            A4 = ((A // 10 ** (n - 4)) % 10)
            A5 = ((A // 10 ** (n - 5)) % 10)
            A6 = ((A // 10 ** (n - 6)) % 10)
            A7 = ((A // 10 ** (n - 7)) % 10)
            A = str(A)
            i2 = 1
            while A != codigo4 and i2 < n:
                cant_famas = 0
                cant_toques = 0
                if A1 == a1:
                    cant_famas += 1
                elif (A1 == a1) or (A1 == a2) or (A1 == a3) or (A1 == a4) or (A1 == a5) or (A1 == a6) or (A1 == a7):
                    cant_toques += 1
                if A2 == a2:
                    cant_famas += 1
                elif (A2 == a1) or (A2 == a2) or (A2 == a3) or (A2 == a4) or (A2 == a5) or (A2 == a6) or (A2 == a7):
                    cant_toques += 1
                if A3 == a3:
                    cant_famas += 1
                elif (A3 == a1) or (A3 == a2) or (A3 == a3) or (A3 == a4) or (A3 == a5) or (A3 == a6) or (A3 == a7):
                    cant_toques += 1
                if A4 == a4:
                    cant_famas += 1
                elif (A4 == a1) or (A4 == a2) or (A4 == a3) or (A4 == a4) or (A4 == a5) or (A4 == a6) or (A4 == a7):
                    cant_toques += 1
                if A5 == a5:
                    cant_famas += 1
                elif (A5 == a1) or (A5 == a2) or (A5 == a3) or (A5 == a4) or (A5 == a5) or (A5 == a6) or (A5 == a7):
                    cant_toques += 1
                if A6 == a6:
                    cant_famas += 1
                elif (A6 == a1) or (A6 == a2) or (A6 == a3) or (A6 == a4) or (A6 == a5) or (A6 == a6) or (A6 == a7):
                    cant_toques += 1
                if A7 == a7:
                    cant_famas += 1
                elif (A7 == a1) or (A7 == a2) or (A7 == a3) or (A7 == a4) or (A7 == a5) or (A7 == a6) or (A7 == a7):
                    cant_toques += 1
                cant_intentos += 1
                if len(A) < len(codigo4) or len(A) > len(codigo4):
                    print("Error, pierdes tu jugada")
                if len(A) == len(codigo4):
                    print(f"Intento {cant_intentos - 1}: {A} Toques: {cant_toques} - Famas: {cant_famas}")
                A = int(input(f"Intento {cant_intentos}: "))
                A1 = ((A // 10 ** (n - 1)) % 10)
                A2 = ((A // 10 ** (n - 2)) % 10)
                A3 = ((A // 10 ** (n - 3)) % 10)
                A4 = ((A // 10 ** (n - 4)) % 10)
                A5 = ((A // 10 ** (n - 5)) % 10)
                A6 = ((A // 10 ** (n - 6)) % 10)
                A7 = ((A // 10 ** (n - 7)) % 10)
                A = str(A)
                i2 += 1
            if A == codigo4:
                print(f"Intento {cant_intentos}: {A} ¡Felicitaciones! Has acertado en {cant_intentos} intentos")
                ganados += 1
            else:
                print(f"Intento {n}: {A} - Fin del juego La secuencia era {codigo4}")
                perdidos += 1
        if n == 8:
            codigo5 = (str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6) + str(a7) + str(a8))
            A = int(input(f"Intento {cant_intentos}: "))
            A1 = ((A // 10 ** (n - 1)) % 10)
            A2 = ((A // 10 ** (n - 2)) % 10)
            A3 = ((A // 10 ** (n - 3)) % 10)
            A4 = ((A // 10 ** (n - 4)) % 10)
            A5 = ((A // 10 ** (n - 5)) % 10)
            A6 = ((A // 10 ** (n - 6)) % 10)
            A7 = ((A // 10 ** (n - 7)) % 10)
            A8 = ((A // 10 ** (n - 8)) % 10)
            A = str(A)
            i2 = 1
            while A != codigo5 and i2 < n:
                cant_famas = 0
                cant_toques = 0
                if A1 == a1:
                    cant_famas += 1
                elif (A1 == a1) or (A1 == a2) or (A1 == a3) or (A1 == a4) or (A1 == a5) or (A1 == a6) or (A1 == a7) \
                    or (A1 == a8):
                    cant_toques += 1
                if A2 == a2:
                    cant_famas += 1
                elif (A2 == a1) or (A2 == a2) or (A2 == a3) or (A2 == a4) or (A2 == a5) or (A2 == a6) or (A2 == a7) \
                    or (A2 == a8):
                    cant_toques += 1
                if A3 == a3:
                    cant_famas += 1
                elif (A3 == a1) or (A3 == a2) or (A3 == a3) or (A3 == a4) or (A3 == a5) or (A3 == a6) or (A3 == a7) \
                    or (A3 == a8):
                    cant_toques += 1
                if A4 == a4:
                    cant_famas += 1
                elif (A4 == a1) or (A4 == a2) or (A4 == a3) or (A4 == a4) or (A4 == a5) or (A4 == a6) or (A4 == a7) \
                    or (A4 == a8):
                    cant_toques += 1
                if A5 == a5:
                    cant_famas += 1
                elif (A5 == a1) or (A5 == a2) or (A5 == a3) or (A5 == a4) or (A5 == a5) or (A5 == a6) or (A5 == a7) \
                    or (A5 == a8):
                    cant_toques += 1
                if A6 == a6:
                    cant_famas += 1
                elif (A6 == a1) or (A6 == a2) or (A6 == a3) or (A6 == a4) or (A6 == a5) or (A6 == a6) or (A6 == a7) \
                    or (A6 == a8):
                    cant_toques += 1
                if A7 == a7:
                    cant_famas += 1
                elif (A7 == a1) or (A7 == a2) or (A7 == a3) or (A7 == a4) or (A7 == a5) or (A7 == a6) or (A7 == a7) \
                    or (A7 == a8):
                    cant_toques += 1
                if A8 == a8:
                    cant_famas += 1
                elif (A8 == a1) or (A8 == a2) or (A8 == a3) or (A8 == a4) or (A8 == a5) or (A8 == a6) or (A8 == a7) \
                    or (A8 == a8):
                    cant_toques += 1
                cant_intentos += 1
                if len(A) < len(codigo5) or len(A) > len(codigo5):
                    print("Error, pierdes tu jugada")
                if len(A) == len(codigo5):
                    print(f"Intento {cant_intentos - 1}: {A} Toques: {cant_toques} - Famas: {cant_famas}")
                A = int(input(f"Intento {cant_intentos}: "))
                A1 = ((A // 10 ** (n - 1)) % 10)
                A2 = ((A // 10 ** (n - 2)) % 10)
                A3 = ((A // 10 ** (n - 3)) % 10)
                A4 = ((A // 10 ** (n - 4)) % 10)
                A5 = ((A // 10 ** (n - 5)) % 10)
                A6 = ((A // 10 ** (n - 6)) % 10)
                A7 = ((A // 10 ** (n - 7)) % 10)
                A8 = ((A // 10 ** (n - 8)) % 10)
                A = str(A)
                i2 += 1
            if A == codigo5:
                print(f"Intento {cant_intentos}: {A} ¡Felicitaciones! Has acertado en {cant_intentos} intentos")
                ganados += 1
            else:
                print(f"Intento {n}: {A} - Fin del juego La secuencia era {codigo5}")
                perdidos += 1
        if n == 9:
            codigo6 = (str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6) + str(a7) + str(a8) + str(a9))
            A = int(input(f"Intento {cant_intentos}: "))
            A1 = ((A // 10 ** (n - 1)) % 10)
            A2 = ((A // 10 ** (n - 2)) % 10)
            A3 = ((A // 10 ** (n - 3)) % 10)
            A4 = ((A // 10 ** (n - 4)) % 10)
            A5 = ((A // 10 ** (n - 5)) % 10)
            A6 = ((A // 10 ** (n - 6)) % 10)
            A7 = ((A // 10 ** (n - 7)) % 10)
            A8 = ((A // 10 ** (n - 8)) % 10)
            A9 = ((A // 10 ** (n - 9)) % 10)
            A = str(A)
            i2 = 1
            while A != codigo6 and i2 < n:
                cant_famas = 0
                cant_toques = 0
                if A1 == a1:
                    cant_famas += 1
                elif (A1 == a1) or (A1 == a2) or (A1 == a3) or (A1 == a4) or (A1 == a5) or (A1 == a6) or (A1 == a7) \
                    or (A1 == a8) or (A1 == a9):
                    cant_toques += 1
                if A2 == a2:
                    cant_famas += 1
                elif (A2 == a1) or (A2 == a2) or (A2 == a3) or (A2 == a4) or (A2 == a5) or (A2 == a6) or (A2 == a7) \
                    or (A2 == a8) or (A2 == a9):
                    cant_toques += 1
                if A3 == a3:
                    cant_famas += 1
                elif (A3 == a1) or (A3 == a2) or (A3 == a3) or (A3 == a4) or (A3 == a5) or (A3 == a6) or (A3 == a7) \
                    or (A3 == a8) or (A3 == a9):
                    cant_toques += 1
                if A4 == a4:
                    cant_famas += 1
                elif (A4 == a1) or (A4 == a2) or (A4 == a3) or (A4 == a4) or (A4 == a5) or (A4 == a6) or (A4 == a7) \
                    or (A4 == a8) or (A4 == a9):
                    cant_toques += 1
                if A5 == a5:
                    cant_famas += 1
                elif (A5 == a1) or (A5 == a2) or (A5 == a3) or (A5 == a4) or (A5 == a5) or (A5 == a6) or (A5 == a7) \
                    or (A5 == a8) or (A5 == a9):
                    cant_toques += 1
                if A6 == a6:
                    cant_famas += 1
                elif (A6 == a1) or (A6 == a2) or (A6 == a3) or (A6 == a4) or (A6 == a5) or (A6 == a6) or (A6 == a7) \
                    or (A6 == a8) or (A6 == a9):
                    cant_toques += 1
                if A7 == a7:
                    cant_famas += 1
                elif (A7 == a1) or (A7 == a2) or (A7 == a3) or (A7 == a4) or (A7 == a5) or (A7 == a6) or (A7 == a7) \
                    or (A7 == a8) or (A7 == a9):
                    cant_toques += 1
                if A8 == a8:
                    cant_famas += 1
                elif (A8 == a1) or (A8 == a2) or (A8 == a3) or (A8 == a4) or (A8 == a5) or (A8 == a6) or (A8 == a7) \
                    or (A8 == a8) or (A8 == a9):
                    cant_toques += 1
                if A9 == a9:
                    cant_famas += 1
                elif (A9 == a1) or (A9 == a2) or (A9 == a3) or (A9 == a4) or (A9 == a5) or (A9 == a6) or (A9 == a7) \
                    or (A9 == a8) or (A9 == a9):
                    cant_toques += 1
                cant_intentos += 1
                if len(A) < len(codigo6) or len(A) > len(codigo6):
                    print("Error, pierdes tu jugada")
                if len(A) == len(codigo6):
                    print(f"Intento {cant_intentos - 1}: {A} Toques: {cant_toques} - Famas: {cant_famas}")
                A = int(input(f"Intento {cant_intentos}: "))
                A1 = ((A // 10 ** (n - 1)) % 10)
                A2 = ((A // 10 ** (n - 2)) % 10)
                A3 = ((A // 10 ** (n - 3)) % 10)
                A4 = ((A // 10 ** (n - 4)) % 10)
                A5 = ((A // 10 ** (n - 5)) % 10)
                A6 = ((A // 10 ** (n - 6)) % 10)
                A7 = ((A // 10 ** (n - 7)) % 10)
                A8 = ((A // 10 ** (n - 8)) % 10)
                A9 = ((A // 10 ** (n - 9)) % 10)
                A = str(A)
                i2 += 1
            if A == codigo6:
                print(f"Intento {cant_intentos}: {A} ¡Felicitaciones! Has acertado en {cant_intentos} intentos")
                ganados += 1
            else:
                print(f"Intento {n}: {A} - Fin del juego La secuencia era {codigo6}")
                perdidos += 1
    continuar = int(input("¿Desea jugar nuevamente? 1. Si / 0. No: "))
        
    if continuar == 0:
        jugados = ganados + perdidos
        print(f"Jugados: {jugados}  - Ganados: {ganados}  - Perdidos: {perdidos} ")
        break
