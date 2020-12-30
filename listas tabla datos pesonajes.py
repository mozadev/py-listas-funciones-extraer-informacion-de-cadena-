'''
Se tiene datos de personas dentro de una lista. 
Los datos contienen el nombre, el DNI, el a�o, mes y d�a de nacimiento separados por el caracter "#".
Note que la informaci�n de cada persona empieza siempre despu�s del caracter ":".
Se desea organizar la informaci�n como una tabla, es decir, como una  lista de listas. 
Tal como se muestra en la Figura de abajo.
Note que adem�s de los datos reorganizados, se ha agregado nueva informaci�n, el campo "Edad". 
La edad debe ir en la �ltima columna de la tabla reorganizada y debe ser calculada autom�ticamente.

a. Cree una funci�n, "reorganizar_datos" que reciba la lista de datos y que devuelva los datos organizados en una lista de listas. Incluya en esa funci�n el c�lculo
del campo "Edad". Para ello, puede definir otras funciones que Ud. vea necesarias.

b. Cree una funci�n, "imprima_datos" que reciba una lista de listas (los datos reorganizados) y los imprima tal como se muestra en la Figura de abajo.

data = ["Nombre:Gerardo Moscoso Tapia#DNI:23242526#A�o:1979#Mes:11# D�a:1", 
        "Nom:Gabriela Mendoza Lezama#D.N.I.:12242526#A�o_nac:1999#Mes_nac:2#D�a_naci:12", 
        "Nomb:German Rodriguez Sabato#DNI:43242526#A�o:1979#Mes:1# D�a:1", 
        "Nom y Ape:Yessenia Ramos Leon#Num DN.I.:22242526#Anho_nac:2019#MesNac:12#D�aNaci:12", 
        "Nom_y_Ape:Lorena Flores Delgado#Num DN.I.:25262224#Anho_nac:1999#MesNac:1#D�aNaci:4", 
        "Noms:Roberto Perez Ramos#N DN.I.:89622242#Anho:1989#MesNac:11#D�aNaci:14",
        "Noms:Pedro Pachecho Yari#DN.I.:15262224#Anho_nac:1991#MesNac:8#D�aNaci:20" ]

'''



data = ["Nombre:Gerardo Moscoso Tapia#DNI:23242526#A�o:1979#Mes:11# D�a:1", 
        "Nom:Gabriela Mendoza Lezama#D.N.I.:12242526#A�o_nac:1999#Mes_nac:2#D�a_naci:12", 
        "Nomb:German Rodriguez Sabato#DNI:43242526#A�o:1979#Mes:1# D�a:1", 
        "Nom y Ape:Yessenia Ramos Leon#Num DN.I.:22242526#Anho_nac:2019#MesNac:12#D�aNaci:12", 
        "Nom_y_Ape:Lorena Flores Delgado#Num DN.I.:25262224#Anho_nac:1999#MesNac:1#D�aNaci:4", 
        "Noms:Roberto Perez Ramos#N DN.I.:89622242#Anho:1989#MesNac:11#D�aNaci:14",
        "Noms:Pedro Pachecho Yari#DN.I.:15262224#Anho_nac:1991#MesNac:8#D�aNaci:20" ]



data = ["Nombre:Gerardo Moscoso Tapia#DNI:23242526#A�o:1979#Mes:11# D�a:1", 
        "Nom:Gabriela Mendoza Lezama#D.N.I.:12242526#A�o_nac:1999#Mes_nac:2#D�a_naci:12", 
        "Nomb:German Rodriguez Sabato#DNI:43242526#A�o:1979#Mes:1# D�a:1", 
        "Nom y Ape:Yessenia Ramos Leon#Num DN.I.:22242526#Anho_nac:2019#MesNac:12#D�aNaci:12", 
        "Nom_y_Ape:Lorena Flores Delgado#Num DN.I.:25262224#Anho_nac:1999#MesNac:1#D�aNaci:4", 
        "Noms:Roberto Perez Ramos#N DN.I.:89622242#Anho:1989#MesNac:11#D�aNaci:14",
        "Noms:Pedro Pachecho Yari#DN.I.:15262224#Anho_nac:1991#MesNac:8#D�aNaci:20" ]



def extrae_lista_pos_camposxpersona(cadinfxPersona):
    ini_fin =[]
    print(cadinfxPersona)
    for i in range(len(cadinfxPersona)):
        if cadinfxPersona[i] ==":":
            ini_fin.append(i+1)
        elif cadinfxPersona[i] =="#":
            ini_fin.append(i-1)
    ini_fin.append(i)# agrega la ultima posicion
    return ini_fin

def extrae_campo(cadinfxPersona, listaposicionesxpersona):
    data =[]
    for i in range(0, len(listaposicionesxpersona)-1, 2):
        data.append(cadinfxPersona[listaposicionesxpersona[i]:listaposicionesxpersona[i+1]+1])
    return data

def calcula_edad(fecha, a_a, m_a, d_a):
    y = int(fecha[0])
    m = int(fecha[1])
    d = int(fecha[2])
    if m == m_a and d<=d_a :
        return a_a-y
    elif m < m_a:
        return a_a-y
    else:
        return a_a-y-1


def reorganizar_datos(data):
    salida =[]
    for cadinfxPersona in data:
        listaposicionesxpersona = extrae_lista_pos_camposxpersona(cadinfxPersona)
        registro = extrae_campo(cadinfxPersona, listaposicionesxpersona)
        registro.append(calcula_edad(registro[2:5], 2020, 10, 14))
        print(listaposicionesxpersona)
        print(registro)
        salida.append(registro)
    return salida

def print_data(data):
    print("Nombre y Apellidos", "\tNum D.N.I.", "\tA�o", "\tMes", "\tD�a", "\tEdad")
    for i in data:
        for j in i:
            print(j, end="\t")
        print()


print_data(reorganizar_datos(data))

