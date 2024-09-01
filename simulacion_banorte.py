# Importamos modulos que se usaran a lo largo del programa.
import datetime
import re
import random

# Se crean las variables globales que se estarán trabajando.
saldo = 10000

# Creamos listas vacías donde guardaremos la referencia del movimiento, y en otra lista, los datos de la persona que hizo el movimiento.
folio_deposito = []
folio_retiro = []
folio_transferencia = []
datos_d= []
datos_r= []
datos_t= []

#Se crea funcion para realizar los depósitos.
def Depositos():
    global saldo
    print("""  
+-----------------------------------------+
| Ingrese la opcion que deseas:           |
+=========================================+
| Deposito a mi cuenta          |    1    |
+-----------------------------------------+
| Deposito a otra cuenta        |    2    |   
+-----------------------------------------+""")
    while True:
        # AQUI DA LA MUESTRA PARA DEPOSITO A OTRA CUENTA QUE NO SEA LA PROPI
        tipo_deposito = input("\nDeposito a tu cuenta o deposito a otra cuenta? ")

        # AQUI VALISA QUE NO SE OMITA EL DATO
        if tipo_deposito == "":
            print("no se debe de omitir el dato")
            continue

        # VALIDA QUE SEA EXATAMENTE EL DATO QUE ESTAMOS PIDIENDO CON LAS ESPECIFICACIONES
        if not bool(re.match("^[1-2]{1}$", tipo_deposito)):
            print("Dato invalido")
            continue
        # AQUI YA SE MUESTRA EL NUMERO QUEINTRODUCIRA A LA OPCION 1 DEL MENU DE DEPOSITO
        if tipo_deposito == "1":
            while True:
                print("\nNOTA:monto minimo a depositar $100, monto maximo a depositar $9000 ")
                _depositar = input("¿Cuanto dinero deseas depositar a tu cuenta?: ")

                # AQUI VALISA QUE NO SE OMITA EL DATO
                if _depositar == "":
                    print("no se debe de omitir el dato")
                    continue

                # VALIDA QUE SEA EXATAMENTE EL DATO QUE ESTAMOS PIDIENDO CON LAS ESPECIFICACIONES
                if not bool(re.match("^([1][0][0]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9]|)$", _depositar)):
                    print("Dato invalido")
                    continue
                depositar = float(_depositar)
                if depositar > 9000:
                    continue
                break
            # AQUI LA LINEA SE TRANSFORMA EN FLOAT PARA HACER LA OPERACION Y SUMARLA A LA VARIABLE SALDO
            depositar = float(_depositar)
            # EN ESTAS SIGUIENTES LINEAS DA LA FECHA Y LA HORA EXACTA EN LA QUE SE HACE EL DEPOSITO
            ahora = datetime.datetime.now()
            fecha = ahora.strftime("%d-%m-%Y")
            hora  = ahora.strftime("%H:%M")
            # AQUI SE HACE LA SUMA DE LA VARIABLE SALDO Y EL DEPOSITO YA HECHO DATO FLOAT
            saldo += depositar
            # AQUI SOLO GENERA UN FOLIO ALEATORIO
            while True:
                folio_d = random.randint(000000, 999999)
                if folio_d in folio_deposito:
                    continue
                else:
                    break
            print("Operacion exitosa !!!")
            # AQUI SOLO DE MUESTRA EL RESULTADO DEL DEPOSITO
            print(f"\nFecha:{fecha}\nDeposito en cajero de ${depositar}\nsu numero de folio es {folio_d}\ny la hora {hora} ")
            # EL FOLIO GENERADO SE AGREGA A LA LISTA FOLIO
            folio_deposito.append(folio_d)
            datos_d.append([fecha, depositar, hora])
            break
        
        # AQUI SE PIDEN DATOS PARA OPCION 2
        if tipo_deposito == "2":
            while True:
                
                print("NOTA: monto minimo a depositar $100, monto maximo a depositar $9000.")
                # PREGUNTA LA CUENTA A LA QUE TRANSFERIR
                _otra_cuenta = input("Cuenta a transferir(Introducir numero de cuenta de 16 digitos): ")

                # VALIDA EL QUE NO SE OMITA EL DATO
                if _otra_cuenta == "":
                    print("no se debe de omitir el dato")
                    continue

                # VALIDA QUE SEA UN NUMERO DE CUENTA DE 16 DIGITOS
                if not bool(re.match("^[0-9]{16}$", _otra_cuenta)):
                    print("Dato invalido")
                    continue
                break
        
            while True:
                # PREGUNTA CUANTO DINERO DESES DEPOSITTAR A LA CUENTA ASIGNADA
                _transferir = input("\n¿Cuanto dinero deseas depositar a la cuenta?: ")

                # VALIDA QUE NO SE OMITA EL DATO
                if _transferir == "":
                    print("no se debe de omitir el dato")
                    continue

                # VALIACION DEL MONTO PERMITIDO QUE SE MENCIONA EN LAS INTRUCCIONES DE DEPOSITO
                if not bool(re.match("^([1][0][0]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9]|)$", _transferir)):
                    print("Dato invalido")
                    continue
                transferir = float(_transferir)
                if transferir >9000:
                    print("\nmonto minimo a transferir $100, monto maximo a depositar $9000")
                    continue
                break
            saldo -= transferir
            while True:
                folio_t = random.randint(000000, 999999)
                if folio_t in folio_transferencia:
                    continue
                else:
                    break

            ahora = datetime.datetime.now()
            fecha = ahora.strftime("%d-%m-%Y")
            hora = ahora.strftime("%H:%M")
            print()
            print("Operacion Exitosa !!!")
            print(f"\nFecha:{fecha}\nDeposito de ${transferir} a la cuenta {_otra_cuenta},\nsu numero de folio es {folio_t} y la hora {hora} ")
            folio_transferencia.append(folio_t)
            datos_t.append([fecha, transferir, _otra_cuenta, hora ])
            break
        break
        
#Depositos()

########################################################333333######################################################################################################


#Se crea la funcion para consultar movimientos.
def ConsultarMovimientos():
    if (len(folio_deposito)>0):
        print("\t.:Movimientos de deposito a mi cuenta:.")
        for x in range(len(folio_deposito)):
            print(f"+{'-'*49}+")
            print(f"|{'Folio':7}|{'Fecha':10}|{'Depósito a mi cuenta ':24}|{'Hora':5}|")
            print(f"|{'-' * 7:7}|{'-' * 10:10}|{'-' * 24:24}|{'-' * 5:5}|")
            print(f"|{folio_deposito[x]:7}|{datos_d[x][0]:10}|{datos_d[x][1]:24}|{datos_d[x][2]:5}|")
            print(f"+{'-'*49}+\n")
    else:
        print("\nNo hay depositos de retiro realizados.\n")

    if (len(folio_retiro) > 0):
        print("\t.:Movimientos de retiro:.")
        for x in range(len(folio_retiro)):
            print(f"+{'-'*37}+")
            print(f"|{'Folio':6}|{'Fecha':10}|{'Retiro':13}|{'Hora':5}|")
            print(f"|{'-' * 6:6}|{'-' * 10:10}|{'-' * 13:13}|{'-' * 5:5}|")
            print(f"|{folio_retiro[x]:6}|{datos_r[x][0]:10}|{datos_r[x][1]:13}|{datos_r[x][2]:5}|")
        print(f"+{'-'*37}+\n")
    else:
        print("No hay retiros realizados.\n")

    if (len(folio_transferencia)>0):
        print("\t.:Movimientos de transferencia:.")
        for x in range(len(folio_transferencia)):
            print(f"+{'-'*55}+")
            print(f"|{'Folio':7}|{'Fecha':10}|{'Transferencia':13}|{'A cuenta':16}|{'Hora':5}|")
            print(f"|{'-' * 7:7}|{'-' * 10:10}|{'-' * 13:13}|{'-' * 16:16}|{'-' * 5:5}|")
            print(f"|{folio_transferencia[x]:7}|{datos_t[x][0]:10}|{datos_t[x][1]:13}|{datos_t[x][2]:16}|{datos_t[x][3]:5}|")
            print(f"+{'-'*55}+\n")
    else:
        print("No hay transferencias realizadas.")
#ConsultarMovimientos()


###################################################################################################################################################

#Se crea la funcion para hacer retiros.
def HacerRetiro():
    global saldo
    print("Su saldo actual es de: ",saldo)
    while True:
        print("NOTA: monto minimo a retirar $100, monto maximo a depositar $10000 ")
        _cant_retiro = input("Cuánto deseas retirar?: ")
        if _cant_retiro == "":
            print("No se puede omitir el dato.\n")
            continue
        if not bool(re.match("^([1][0][0]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9]|)$", _cant_retiro)):
            print("Dato invalido\n")
            continue
        cant_retiro = int(_cant_retiro)
        if cant_retiro > saldo:
            print("No cuentas con saldo suficiente.\n")
            continue
        break
    ahora = datetime.datetime.now()
    fecha = ahora.strftime("%d-%m-%Y")
    hora = ahora.strftime("%H:%M")
    while True:
        folio_r = random.randint(000000,999999)
        if folio_r in folio_retiro:
            continue
        break
    cant_retiro = float(_cant_retiro)
    saldo -= cant_retiro
    print(f"\nFecha: {fecha} Se realizó el retiro por ${cant_retiro}\nexitosamente a la {hora}\ny su clave de retiro es: {folio_r}.\n\nTu saldo restante es: {saldo}")
    folio_retiro.append(folio_r)
    datos_r.append([fecha, cant_retiro, hora])
#HacerRetiro()
#####################################################################################################################################################


def algo_mas():
    while True:
        print("""  
+------------------------------------+        
|¿Deseas hacer alguna otra operacion?|
+------------------------------------+        
|                SI                  |
+------------------------------------+
|                NO                  |  
+------------------------------------+""")
        _algo_mas=input().upper()
        _algomas=_algo_mas
        if _algo_mas=="":
            print("No se debe de omitir el dato")
            continue
        if not bool(re.match("^(SI|NO)$",_algomas)):
            print("Dato invalido")
            continue
        if _algo_mas =="SI":
            Inicio()
        if _algo_mas =="NO":
            print("\nGracias por utilizar la simulacion de cajero")
            break
        break



#############################################################################################################################################
#Se inicia el ENTRY POINT
def Inicio():
    import logo_banorte
    print("\t WELCOME TO YOUR BANK APLICATION")
    print(logo_banorte.logo)
    while True:
        print("""
+-----------------------------------------+
| Bienvenido, ingrese una opcion:         |
+=========================================+
|Depósito                       |    D    |
+-----------------------------------------+
|Consulta de saldo o movimientos|    C    |   
+-----------------------------------------+
| Retiro                        |    R    |
+-----------------------------------------+
| Salir                         |    S    |
+-----------------------------------------+
""")
        opcion = input("Ingresa una opción: ").upper()

        if opcion == "":
            print("No omitir.")
            continue
        elif (opcion.upper() == "C"):
            while True:
                print("""  
+------------------------------------+        
|Deseas consultar saldo o movimientos|
+------------------------------------+        
|         saldos         |     S     |
+------------------------------------+
|        movimientos     |     M     |  
+------------------------------------+""")
                consultar=input().upper()
                if consultar =="S":
                    print(f"Tu saldo actual es: {saldo}")
                    algo_mas()
                    break
                if consultar =="M":
                    ConsultarMovimientos()
                    algo_mas()
                    break
                else:
                    print("Opcion invalida")
                    continue
                break
        elif (opcion.upper() == "D"):
            Depositos()
            algo_mas()
            break

        elif (opcion.upper() == "R"):
            HacerRetiro()
            algo_mas()
            break
        elif (opcion.upper() == "S"):
            print("\nGracias por usar el simulador.")
            break
        else:
            print("\nopcion no valida")
            continue
        break
Inicio()