
import tkinter as tk
from tkinter import*
import sqlparse #libreria de sql cup y lex
import Traductor_Delete as dl
import Traductor_Insert as ins
import Traductor_Select as slc
import pyodbc #conexion con la base de datos
server = 'MIGUELYS'
bd = 'PRUEBA'
usuario = 'sa'
contrasena = 'sa'

conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+'; DATABASE='+bd+';UID='+usuario+';PWD='+contrasena)


def Boton_Analizar(len_sql,analizador_s , name):
    consulta_mql = " "
    consulta_sin = " "
    consulta = name.get()
    formato = sqlparse.format(consulta, keyword_case="upper")
    analizado = sqlparse.parse(formato)  # analiza la primera cadena
    token_list = analizado[0]  # extraer la primera consulta (si hay más de una en la cadena)
    tokens = token_list.tokens  # extrae todas las palabras de la consulta y las clasifica según su tipo
    tipo_consulta = tokens[0].value
    cursor= conexion.cursor()         
        
    if tipo_consulta == "SELECT":
        try:
            cursor.execute(consulta)
            consulta_mql = slc.select(tokens)
            consulta_sin = "CONSULTA DE TIPO SELECT"
        except:
            consulta_sin = "ERROR SINTACTICO"

    elif tipo_consulta == "INSERT":
        try:
            cursor.execute(consulta)
            consulta_mql = ins.insert(tokens)
            consulta_sin = "CONSULTA DE TIPO INSERT"
        except:
            consulta_sin = "ERROR SINTACTICO"
    elif tipo_consulta == "DELETE":
        try:
            cursor.execute(consulta)
            consulta_mql = dl.delete(tokens)
            consulta_sin = "CONSULTA DE TIPO DELETE"
        except:
            consulta_sin = "ERROR SINTACTICO"
    else:
        #consulta_mql = "CONSULTA DE SQL ERRADA ERROR EN LA LINEA 1"
        consulta_sin = "CONSULTA DE SQL ERRADA se esperava un SELECT,DELETE,INSERT"
   
    print("LA CONSULTA REALIZADA ES: ", consulta_mql)
    print("LA CONSULTA REALIZADA ES: ",consulta_sin)
    len_sql.delete('1.0', tk.END) #ELIMINAR EL TEXT BOX
    len_sql.insert(tk.END, consulta_mql)

    analizador_s.delete('1.0', tk.END) #ELIMINAR EL TEXT BOX
    analizador_s.insert(tk.END, consulta_sin)

def Vista_tkinker():
    windows = tk.Tk()
    windows.title("Traductor SQL a MQL")
    windows.minsize(1366, 768)
    
    #analiza texto encabezado
    label = tk.Label(windows, text="Traductor de SQL a MQL",font=("Tahoma", 14), bg="green", fg="white")
    label.place(x=50, y=10, width=1250, height=60)
    
    #encabezado sql
    encMQL = tk.Label(windows, text="Resultado en MQL",font=("Tahoma", 12), fg="black")
    encMQL.place(x=740, y=80, width=200, height=30)
    #anbaliza el texto de salida qml
    len_sql = tk.Text(windows)
    len_sql.place(x=730, y=110, height = 400, width = 600)
    len_sql.insert(tk.END,"")

    #encabezado sql
    encSQL = tk.Label(windows, text="Introduzca el código en SQL",font=("Tahoma", 12), fg="black")
    encSQL.place(x=40, y=80, width=200, height=30)
    #analiza texto de etrada sql
    name = tk.StringVar()
    nameEntered = Entry(windows, textvariable=name)
    nameEntered.place(x=30, y=110, height = 400, width = 600)
    
    #salidassss errores
    analizador_s = tk.Text(windows, width= 100, height = 12)
    analizador_s.place(x=250, y=550)
    analizador_s.insert(tk.END,"")
    #encabezado sql
    encError = tk.Label(windows, text="Resultado:",font=("Tahoma", 12), fg="black")
    encError.place(x = 560, y=520, width=200, height=30)
    #analiza botn
    button = tk.Button(windows, text="Analizar", command=lambda: Boton_Analizar(len_sql,analizador_s,name))
    button.place(x=660, y=250)
    windows.mainloop()

def main():
    Vista_tkinker()

if __name__ == "__main__":
    main()
"""   
def Vista_tkinker():
    #declaramos ventana
    windows = tk.Tk()
    windows.title("MySQL pasar a MongoDB ")
    windows.minsize(700, 500)
    #analiza texto encabezado
    label = tk.Label(windows, text="Traductor de SQL - MQL",font=("Tahoma", 12), bg="#ff7763", fg="black", width=80, height=2)
    label.place(x=0, y=10)
    #anbaliza el texto de salida qml
    len_sql = tk.Text(windows, width= 35, height = 20)
    len_sql.place(x=380, y=90)
    len_sql.insert(tk.END,"")
    #salidassss errores
    analizador_s = tk.Text(windows, width= 85, height = 5)
    analizador_s.place(x=8, y=420)
    analizador_s.insert(tk.END,"")
    #analiza texto de etrada sql
    name = tk.StringVar()
    nameEntered = tk.Entry(windows,width = 47, textvariable=name)
    nameEntered.place(x=8, y=90)
    #pantalla fiunta

    #nameEntered.grid(column=0, row=1)
    #analiza botn
    button = tk.Button(windows, text="Analizar", command=lambda: Boton_Analizar(len_sql,analizador_s,name))
    button.place(x=310, y=250)
    
    #mostrar pantalllaso errores
    text_errores = Text(windows, width= 35, height = 18)
    text_errores.place(x=8, y=110)
    windows.mainloop()

def main():
    Vista_tkinker()



if __name__ == "__main__":
    main()
"""
