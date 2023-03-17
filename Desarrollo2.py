from os import system
import msvcrt
import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#/////////////////////////////////////////////////// ACADEMICOS /////////////////////////////////////////////////////////////////////////

def MenuAcademicos():
    def conexionBD():
    	global cursor
    	global connection
    	connection = pymysql.connect(
    			host='localhost',
    			user= 'root',#Cambiar por su usuario
    			password='rootroot',#Cambiar por su contraseña
    			db='prueba'
    		)
    	cursor=connection.cursor()
    	print ("Conexion exitosa...")
    
    def salir():
    	valor=messagebox.askquestion("Salir", "¿Esta seguro que desea salir...?")
    	if valor=="yes":
    		ventana.destroy()
    
    def limpiardatos():
    	Id.set("")
    	Nombre.set("")
    	Rut.set("")
    	FechaIngreso.set("")
    	PrevisionSalud.set("")
    	SueldoBruto.set("")
    	Facultad.set("")
    
    def mensaje():
    	texto='''Nicolás Cortés Alfaro  |||  Ignacio Lamilla Rojas'''
    	messagebox.showinfo(title="Información...", message=texto)
    
    def guardar():
    	conexionBD()
    	try:
    		datos=Nombre.get(), Rut.get(), FechaIngreso.get(), PrevisionSalud.get(), SueldoBruto.get(), Facultad.get()
    		sql='INSERT INTO academicos (ID, Nombre, Rut, Fecha_Ingreso, Prevision_Salud, Sueldo_Bruto, Facultad) VALUES(NULL,%s,%s,%s,%s,%s,%s)'
    		cursor.execute(sql,datos)
    		connection.commit()
    
    	except Exception as e:
    		messagebox.showwarning("Error", "El registro no se Guardo...")
    		pass
    	limpiardatos()
    	mostrar()
    
    def mostrar():
    	conexionBD()
    	registros=tree.get_children()
    	for elemento in registros:
    		tree.delete(elemento)
    		
    	try:
    		sql='SELECT * FROM academicos'
    		cursor.execute(sql)
    		for row in cursor:
    			tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
    	except Exception as e:
    		 pass
    
    def actualizar():
    	conexionBD()
    	try:
    		datos=Nombre.get(), Rut.get(), FechaIngreso.get(), PrevisionSalud.get(), SueldoBruto.get(), Facultad.get()
    		sql='UPDATE academicos SET Nombre=%s, Rut=%s, Fecha_Ingreso=%s, Prevision_Salud=%s, Sueldo_Bruto=%s, Facultad=%s WHERE ID='+Id.get()
    		cursor.execute(sql,datos)
    		connection.commit()
    	except Exception as e:
    		messagebox.showwarning("Error", "No se actualizaron los datos...")
    		pass
    	limpiardatos()
    	mostrar()
    
    def borrar():
    	conexionBD()
    	try:
    		if messagebox.askyesno(message="¿Esta seguro que desea ELIMINAR...?",title="Precaución"):
    			sql='DELETE FROM academicos WHERE ID='+Id.get()
    			cursor.execute(sql)
    			connection.commit()
    	except Exception as e:
    		messagebox.showwarning("Error", "No se eliminaron de datos...")
    		pass
    	limpiardatos()
    	mostrar()
    
    def seleccionarDato(event):
    	item=tree.identify("item",event.x,event.y)
    	Id.set(tree.item(item,"text"))
    	Nombre.set(tree.item(item,"values")[0])
    	Rut.set(tree.item(item,"values")[1])
    	FechaIngreso.set(tree.item(item,"values")[2])
    	PrevisionSalud.set(tree.item(item,"values")[3])
    	SueldoBruto.set(tree.item(item,"values")[4])
    	Facultad.set(tree.item(item,"values")[5])
    
    
    
    #------ Declaración de Variables ------#
    
    ventana = Tk()
    ventana.title("CRUD de Academicos...")
    ventana.geometry("800x500")
    Id=StringVar()
    Nombre=StringVar()
    Rut=StringVar()
    FechaIngreso=StringVar()
    PrevisionSalud=StringVar()
    SueldoBruto=StringVar()
    Facultad=StringVar()
    
    
    
    
    #------ Tabla ------#
    tree=ttk.Treeview(height=10, columns=('#1','#2','#3','#4','#5','#6'))
    tree.place(x=10,y=250) # posicion tabla
    tree.column('#0',width=50) # ancho columna 0 (ID)
    tree.heading('#0', text="ID",anchor=CENTER)
    tree.column('#1',width=180)
    tree.heading('#1', text="Nombre",anchor=CENTER)
    tree.column('#2',width=180)
    tree.heading('#2', text="Rut",anchor=CENTER)
    tree.column('#3',width=180)
    tree.heading('#3', text="Fecha Ingreso",anchor=CENTER)
    tree.column('#4',width=180)
    tree.heading('#4', text="Prevision Salud",anchor=CENTER)
    tree.column('#5',width=180)
    tree.heading('#5', text="Sueldo Bruto",anchor=CENTER)
    tree.column('#6',width=180)
    tree.heading('#6', text="Facultad",anchor=CENTER)
    
    tree.bind("<Double-1>", seleccionarDato)
    
    #----Barra de Menu-----#
    Barramenu=Menu(ventana)
    menu=Menu(Barramenu,tearoff=0)
    menu.add_command(label="Limpiar Datos",command=limpiardatos)
    menu.add_command(label="Integrantes",command=mensaje)
    Barramenu.add_cascade(label="Ayuda",menu=menu)
    
    #----- Label y Input------#
    
    e1=Entry(ventana,textvariable=Id)
    
    lNombre=Label(ventana,text="Nombre :") # Texto del label
    lNombre.place(x=50,y=10) # posicion del label
    etNombre=Entry(ventana,textvariable=Nombre,width=50) # cuadro de texto
    etNombre.place(x=200,y=10) # posicion del cuadro de texto
    
    lRut=Label(ventana,text="Rut :")
    lRut.place(x=50,y=40)
    etRut=Entry(ventana,textvariable=Rut,width=50)
    etRut.place(x=200,y=40)
    
    lFechaIngreso=Label(ventana,text="Fecha Ingreso :")
    lFechaIngreso.place(x=50,y=70)
    etFechaIngreso=Entry(ventana,textvariable=FechaIngreso,width=50)
    etFechaIngreso.place(x=200,y=70)
    
    lPrevisionSalud=Label(ventana,text="Prevision Salud :")
    lPrevisionSalud.place(x=50,y=100)
    etPrevisionSalud=Entry(ventana,textvariable=PrevisionSalud,width=50)
    etPrevisionSalud.place(x=200,y=100)
    
    lSueldoBruto=Label(ventana,text="Sueldo Bruto :")
    lSueldoBruto.place(x=50,y=130)
    etSueldoBruto=Entry(ventana,textvariable=SueldoBruto,width=50)
    etSueldoBruto.place(x=200,y=130)
    
    lFacultad=Label(ventana,text="Facultad :")
    lFacultad.place(x=50,y=160)
    etFacultad=Entry(ventana,textvariable=Facultad,width=50)
    etFacultad.place(x=200,y=160)
    
    #-------Botones------#
    
    btnGuardar=Button(ventana, text="Guardar", command=guardar)
    btnGuardar.place(x=50, y=200)
    
    btnModificar=Button(ventana, text="Modificar", command=actualizar)
    btnModificar.place(x=150, y=200)
    
    btnBuscar=Button(ventana, text="Mostrar", command=mostrar)
    btnBuscar.place(x=250, y=200)
    
    btnBorrar=Button(ventana, text="Eliminar", command=borrar)
    btnBorrar.place(x=350, y=200)
    
    ventana.config(menu=Barramenu)
    ventana.mainloop()
    
#/////////////////////////////////////////////////// ACADEMICOS /////////////////////////////////////////////////////////////////////////   

#/////////////////////////////////////////////////// ADMINISTRATIVOS ////////////////////////////////////////////////////////////////////
def MenuAdmin():
    def conexionBD():
    	global cursor
    	global connection
    	connection = pymysql.connect(
    			host='localhost',
    			user= 'root',#Cambiar por su usuario
    			password='rootroot',#Cambiar por su contraseña
    			db='prueba'
    		)
    	cursor=connection.cursor()
    	print ("Conexion exitosa...")
    
    def salir():
    	valor=messagebox.askquestion("Salir", "¿Esta seguro que desea salir...?")
    	if valor=="yes":
    		ventana.destroy()
    
    def limpiardatos():
    	Id.set("")
    	Nombre.set("")
    	Rut.set("")
    	FechaIngreso.set("")
    	PrevisionSalud.set("")
    	SueldoBruto.set("")
    	UnidadAdministrativa.set("")
    	Cargo.set("")
    
    def mensaje():
    	texto='''Nicolás Cortés Alfaro  |||  Ignacio Lamilla Rojas'''
    	messagebox.showinfo(title="Información...", message=texto)
    
    def guardar():
    	conexionBD()
    	try:
    		datos=Nombre.get(), Rut.get(), FechaIngreso.get(), PrevisionSalud.get(), SueldoBruto.get(), UnidadAdministrativa.get(), Cargo.get()
    		sql='INSERT INTO administrativos (ID, Nombre, Rut, Fecha_Ingreso, Prevision_Salud, Sueldo_Bruto, Unidad_Administrativa, Cargo) VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)'
    		cursor.execute(sql,datos)
    		connection.commit()
    
    	except Exception as e:
    		messagebox.showwarning("Error", "El registro no se Guardo...")
    		pass
    	limpiardatos()
    	mostrar()
    
    def mostrar():
    	conexionBD()
    	registros=tree.get_children()
    	for elemento in registros:
    		tree.delete(elemento)
    		
    	try:
    		sql='SELECT * FROM administrativos'
    		cursor.execute(sql)
    		for row in cursor:
    			tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    	except Exception as e:
    		 pass
    
    def actualizar():
    	conexionBD()
    	try:
    		datos=Nombre.get(), Rut.get(), FechaIngreso.get(), PrevisionSalud.get(), SueldoBruto.get(), UnidadAdministrativa.get(), Cargo.get()
    		sql='UPDATE administrativos SET Nombre=%s, Rut=%s, Fecha_Ingreso=%s, Prevision_Salud=%s, Sueldo_Bruto=%s, Unidad_Administrativa=%s, Cargo=%s WHERE ID='+Id.get()
    		cursor.execute(sql,datos)
    		connection.commit()
    	except Exception as e:
    		messagebox.showwarning("Error", "No se actualizaron los datos...")
    		pass
    	limpiardatos()
    	mostrar()
    
    def borrar():
    	conexionBD()
    	try:
    		if messagebox.askyesno(message="¿Esta seguro que desea ELIMINAR...?",title="Precaución"):
    			sql='DELETE FROM administrativos WHERE ID='+Id.get()
    			cursor.execute(sql)
    			connection.commit()
    	except Exception as e:
    		messagebox.showwarning("Error", "No se eliminaron de datos...")
    		pass
    	limpiardatos()
    	mostrar()
    
    def seleccionarDato(event):
    	item=tree.identify("item",event.x,event.y)
    	Id.set(tree.item(item,"text"))
    	Nombre.set(tree.item(item,"values")[0])
    	Rut.set(tree.item(item,"values")[1])
    	FechaIngreso.set(tree.item(item,"values")[2])
    	PrevisionSalud.set(tree.item(item,"values")[3])
    	SueldoBruto.set(tree.item(item,"values")[4])
    	UnidadAdministrativa.set(tree.item(item,"values")[5])
    	Cargo.set(tree.item(item,"values")[6])
    
    
    
    #------ Declaración de Variables ------#
    
    ventana = Tk()
    ventana.title("Sistema de Gestión...")
    ventana.geometry("800x500")
    Id=StringVar()
    Nombre=StringVar()
    Rut=StringVar()
    FechaIngreso=StringVar()
    PrevisionSalud=StringVar()
    SueldoBruto=StringVar()
    UnidadAdministrativa=StringVar()
    Cargo=StringVar()
    
    
    
    
    #------ Tabla ------#
    tree=ttk.Treeview(height=10, columns=('#1','#2','#3','#4','#5','#6','#7'))
    tree.place(x=10,y=300) # posicion tabla
    tree.column('#0',width=50) # ancho columna 0 (ID)
    tree.heading('#0', text="ID",anchor=CENTER)
    tree.column('#1',width=180)
    tree.heading('#1', text="Nombre",anchor=CENTER)
    tree.column('#2',width=120)
    tree.heading('#2', text="Rut",anchor=CENTER)
    tree.column('#3',width=120)
    tree.heading('#3', text="Fecha Ingreso",anchor=CENTER)
    tree.column('#4',width=120)
    tree.heading('#4', text="Prevision Salud",anchor=CENTER)
    tree.column('#5',width=120)
    tree.heading('#5', text="Sueldo Bruto",anchor=CENTER)
    tree.column('#6',width=180)
    tree.heading('#6', text="Unidad Administrativa",anchor=CENTER)
    tree.column('#7',width=180)
    tree.heading('#7', text="Cargo",anchor=CENTER)
    
    
    tree.bind("<Double-1>", seleccionarDato)
    
    #----Barra de Menu-----#
    Barramenu=Menu(ventana)
    menu=Menu(Barramenu,tearoff=0)
    menu.add_command(label="Limpiar Datos",command=limpiardatos)
    menu.add_command(label="Integrantes",command=mensaje)
    Barramenu.add_cascade(label="Ayuda",menu=menu)
    
    #----- Label y Input------#
    
    e1=Entry(ventana,textvariable=Id)
    
    lNombre=Label(ventana,text="Nombre :") # Texto del label
    lNombre.place(x=50,y=10) # posicion del label
    etNombre=Entry(ventana,textvariable=Nombre,width=50) # cuadro de texto
    etNombre.place(x=200,y=10) # posicion del cuadro de texto
    
    lRut=Label(ventana,text="Rut :")
    lRut.place(x=50,y=40)
    etRut=Entry(ventana,textvariable=Rut,width=50)
    etRut.place(x=200,y=40)
    
    lFechaIngreso=Label(ventana,text="Fecha Ingreso :")
    lFechaIngreso.place(x=50,y=70)
    etFechaIngreso=Entry(ventana,textvariable=FechaIngreso,width=50)
    etFechaIngreso.place(x=200,y=70)
    
    lPrevisionSalud=Label(ventana,text="Prevision Salud :")
    lPrevisionSalud.place(x=50,y=100)
    etPrevisionSalud=Entry(ventana,textvariable=PrevisionSalud,width=50)
    etPrevisionSalud.place(x=200,y=100)
    
    lSueldoBruto=Label(ventana,text="Sueldo Bruto :")
    lSueldoBruto.place(x=50,y=130)
    etSueldoBruto=Entry(ventana,textvariable=SueldoBruto,width=50)
    etSueldoBruto.place(x=200,y=130)
    
    lUnidadAdministrativa=Label(ventana,text="Unidad Administrativa :")
    lUnidadAdministrativa.place(x=50,y=160)
    etUnidadAdministrativa=Entry(ventana,textvariable=UnidadAdministrativa,width=50)
    etUnidadAdministrativa.place(x=200,y=160)
    
    lCargo=Label(ventana,text="Cargo :")
    lCargo.place(x=50,y=190)
    etCargo=Entry(ventana,textvariable=Cargo,width=50)
    etCargo.place(x=200,y=190)
    
    #-------Botones------#
    
    btnGuardar=Button(ventana, text="Guardar", command=guardar)
    btnGuardar.place(x=150, y=260)
    
    btnModificar=Button(ventana, text="Modificar", command=actualizar)
    btnModificar.place(x=250, y=260)
    
    btnBuscar=Button(ventana, text="Mostrar", command=mostrar)
    btnBuscar.place(x=350, y=260)
    
    btnBorrar=Button(ventana, text="Eliminar", command=borrar)
    btnBorrar.place(x=450, y=260)
    
    ventana.config(menu=Barramenu)
    ventana.mainloop()

#/////////////////////////////////////////////////// ADMINISTRATIVOS ////////////////////////////////////////////////////////////////////

def PagoPersonal():
    print("Pago del personal\n")
    pp=int(input("\nDesea gestionar el pago del personal? (1)SI (2) NO: "))
    while pp<1 or pp>2:
        print("El valor ingresado es incorrecto ")
        pp=int(input("\nDesea gestionar el pago del personal? (1)SI (2) NO: "))
    if pp==1:
         pps=int(input("A que departamento desea gestionar el pago? (1) Academico (2) Administrativo: "))
         while pps<1 or pps>3:
             print("El valor ingresado es incorrecto ")
             pps=int(input("A que departamento desea gestionar el pago? (1) Academico (2) Administrativo: "))
         if pps==1:
             MenuAcademicos()
             sp=int(input("Seleccione la ID del academico que desea gestionar: "))
             print("\nEl pago esta sujeto a las siguientes condiciones: ")
             condiciones()
         if pps==2:
             MenuAdmin()
             print("\nEl pago esta sujeto a las siguientes condiciones: ")
             condiciones()             
    elif pp==2:
        print("")
       
    
def salir():
    print("Hasta pronto..!")
    msvcrt.getch()
    exit()    
    
def condiciones():
	print("\n-AFP descuento del 10 porciento\n\n")
	print("-Salud descuento del 7 porciento\n\n")
	print("-Si lleva mas de 20 años prestando servicios tendra una bonificacion del 5 porciento\n\n")
	print("-Si lleva mas de 30 años prestando servicios tendra una bonificacion de 7 porciento\n\n")
	print("-Si es personal administrativo bonificacion del 3 porciento\n\n")
	print("-Si es personal docente bonificacion del 5 porciento\n\n")
	

   
def main():
    empezar=int(input("Desea ingresar al menu 1) SI  2) NO: "))
    while(empezar<0 or empezar>2):
        print("valor no valida")
        empezar=int(input("Desea ingresar al menu 1) SI  2) NO: "))
    while empezar==1:
        system("cls")
        print("|******************************|")
        print("|**|      GESTION DE        |**|")
        print("|**|      PERSONAL          |**|")
        print("|******************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Personal academico")
        print("2.- Personal administrativo")
        print("3.- Pago Personal")
        print("4.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            system("cls")
            MenuAcademicos()
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        
        elif opcion ==2:
            system("cls")
            MenuAdmin()
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        elif opcion ==3:
            system("cls")
            PagoPersonal()
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()    
            
        
        elif opcion == 4:
            empezar = 2
          
    if empezar==2:
        salir()

if __name__ == '__main__':
    main();