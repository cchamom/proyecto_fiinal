from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame, messagebox
from conexio import comunicacion
from time import strftime
import pandas as pd

#ventana principal
class ventana(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Nombre = StringVar()
        self.Telefono = StringVar()
        self.Motivo = StringVar()
        self.Correo = StringVar()
        self.Fecha = StringVar()

        # para ampliar o adaptar la ventaba
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=5)

        self.base_datos = comunicacion

        self.widgets()

    # Resto del código de la clase Ventana...
    def widgets(self):
        self.frame_uno = Frame(self.master, bg="white", height=200, width=800)
        self.frame_uno.grid(column=0, row=0, sticky="nsew")  
        self.frame_dos = Frame(self.master, bg="white", height=300, width=800 )
        self.frame_dos.grid(column=0, row=1, sticky="nsew")

        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)
        
        Label(self.frame_uno, text="Opciones", bg="white", fg="black", font=("Kaufmann BT", 13, "bold",)).grid( column=2, row=0)
        Button(self.frame_uno, text="ACTUALIZAR", font=("Arial", 9, "bold"),
        command=self.actualizar_tabla, fg="black", bg="deep sky blue", width=20, bd=3).grid(column=2, row=1, pady=5)
        Label(self.frame_uno, text="Agregar y actualizar usuarios", fg="black", bg="white",
          font=("Kaufmann BT", 13, "bold")).grid(columnspan=2, column=0, row=1, pady=5)
    
    # Ajustar las filas para evitar superposición
        Label(self.frame_uno, text="Nombre", fg="black", bg="white", font=("Rockwell", 13, "bold",)).grid(column=0, row=2, pady=5)
        Label(self.frame_uno, text="Telefono", fg="black", bg="white", font=("Rockwell", 13, "bold",)).grid(column=0, row=3, pady=5)
        Label(self.frame_uno, text="Motivo de la visita", fg="black", bg="white", font=("Rockwell", 13, "bold",)).grid(column=0, row=4, pady=5)
        Label(self.frame_uno, text="Correo", fg="black", bg="white", font=("Rockwell", 13, "bold",)).grid(column=0, row=5, pady=5)
        Label(self.frame_uno, text="Fecha", fg="black", bg="white", font=("Rockwell", 13, "bold",)).grid(column=0, row=6, pady=5)

    # Campos de entrada de los label
        Entry(self.frame_uno, textvariable=self.Nombre, font=("Comic Sans MS", 12), highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=2)
        Entry(self.frame_uno, textvariable=self.Telefono, font=("Comic Sans MS", 12), highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=3)
        Entry(self.frame_uno, textvariable=self.Motivo, font=("Comic Sans MS", 12), highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=4)
        Entry(self.frame_uno, textvariable=self.Correo, font=("Comic Sans MS", 12), highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=5)
        Entry(self.frame_uno, textvariable=self.Fecha, font=("Comic Sans MS", 12), highlightbackground="deep sky blue", highlightthickness=5).grid(column=1, row=6)

    # Botones para las acciones
        Button(self.frame_uno, text="Añadir Paciente", font=("Arial", 9, "bold"), bg="deep sky blue",
           width=20, bd=3, command=self.agregar_datos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text="Mostrar Pacientes", font=("Arial", 9, "bold"), bg="deep sky blue",
           width=20, bd=3, command=self.obtener_fila).grid(column=2, row=3, pady=5, padx=5)
        Button(self.frame_uno, text="Eliminar Paciente", font=("Arial", 9, "bold"), bg="deep sky blue",
           width=20, bd=3, command=self.eliminar_datos).grid(column=2, row=4, pady=5, padx=5)
        Button(self.frame_uno, text="Actualizar Registros", font=("Arial", 9, "bold"), bg="deep sky blue",
           width=20, bd=3, command=self.actualizar_datos).grid(column=2, row=5, pady=5, padx=5)

#Parte de la tabla de datos
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font=("Helvetica", 10, "bold"), foreground="black", background="white")
        estilo_tabla.map("Treeview", background=[("selected", "deep sky blue")], foreground=[("selected", "black")])
        estilo_tabla.configure("Heading", background="white", foreground="deep sky blue", font=("Helvetica", 10, "bold"))
        
        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky="nsew")
        
        ladox = ttk.Scrollbar(self.frame_dos, orient="horizontal", command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky="ew")
        
        ladoy = ttk.Scrollbar(self.frame_dos, orient="vertical", command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky="ns")
        
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)


# Creación de la tabla
        self.tabla["columns"] = ("Nombre", "Telefono", "Motivo", "Correo", "Fecha")
        self.tabla.column("Nombre", minwidth=100, width=120, anchor="center")
        self.tabla.column("Telefono", minwidth=100, width=120, anchor="center")
        self.tabla.column("Motivo", minwidth=100, width=120, anchor="center")
        self.tabla.column("Correo", minwidth=100, width=120, anchor="center")
        self.tabla.column("Fecha", minwidth=100, width=105, anchor="center")

# Configuramos el encabezado
        self.tabla.heading("Nombre", text="Nombre", anchor="center")
        self.tabla.heading("Telefono", text="Telefono", anchor="center")
        self.tabla.heading("Motivo", text="Motivo", anchor="center")
        self.tabla.heading("Correo", text="Correo", anchor="center")
        self.tabla.heading("Fecha", text="Fecha", anchor="center")

# Configuramos los eventos para seleccionar la fila y ejecutar los métodos de ejecución de fila y eliminación de datos
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

# Método para obtener los valores de la fila
    def obtener_fila(self, event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.Nombre.set(self.data["text"][0])
        self.Telefono.set(self.data["values"][0])
        self.Motivo.set(self.data["values"][1])
        self.Correo.set(self.data["values"][2])
        self.Fecha.set(self.data["values"][3])

# Método para eliminar los datos
    def eliminar_datos(self, event):
        self.limpiar_campos()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion("Informacion", "¿Desea eliminar al paciente?")
        if x == "Si":
            self.tabla.delete(item)
            self.base_datos.eliminar_datos(self.data["text"])

#metodo para agregar datos
    def agregar_datos(self):
        Nombre = self.Nombre.get()
        Telefono = self.Telefono.get()
        Motivo = self.Motivo.get()
        Correo = self.Correo.get()
        Fecha = self.Fecha.get()
        datos = (Telefono, Motivo, Correo, Fecha)
        if Nombre and Telefono and Motivo and Correo and Fecha !="":
            self.tabla.insert("", 0, text= Nombre, values = datos)
            self.base_datos.insertar_datos(Nombre, Telefono, Motivo, Correo, Fecha) 
            self.limpiar_campos()
              
#para actualizar la tabla
    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i = 1
        for dato in datos:
            i = i+1
            self.tabla.insert("", i, text=datos[i][1:2][0], values=datos[i][2:5])

#actualizar los datos de la base de datos
    def actualizar_datos(self):
        item = self.tabla.focus()
        self.data=self.tabla.item(item)
        Nombre = self.data["text"]
        datos = self.base_datos.mostrar_datos()
        for fila in datos:
            Nombre = fila[0]
            Nombre_bd = fila[1]
            if Nombre_bd == Nombre:
                if Nombre != None:
                    Nombre = self.Nombre.get()
                    Telefono = self.Telefono.get()
                    Motivo = self.Telefono.get()
                    Correo = self.Correo.get()
                    Fecha = self.Fecha.get()
                    if Nombre and Telefono and Motivo and Correo and Fecha != "":
                        self.base_datos.actualizar_datos(Nombre, Telefono, Motivo, Correo, Fecha)
                        self.tabla.delete(self.tabla.children())
                        datos = self.base_datos.mostrar_datos()
                        i = -1
                        for dato in datos:
                            i = i+1
                            self.tabla.insert("", i, text = datos[i][1:2][0], values=datos[2:5])

#para limpiar los campos de los label
    def limpiar_campos(self):
        self.Nombre.set("")
        self.Telefono.set("") 
        self.Motivo.set("")
        self.Correo.set("")
        self.Fecha.set("")

 #para guardar datos exportando un archivo exel 
    def guardar_datos(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        i = -1
        Nombre, Telefono, Motivo, Correo, Fecha = [],[],[],[],[]
        for dato in datos:
            i = i+1
            Nombre.append(datos[i][1])
            Telefono.append(datos[i][2])
            Motivo.append(datos[i][3])
            Correo.append(datos[i][4])
            Fecha.append(datos[i][5])
        fecha= str(strftime("%d-%m-%y-_%H-%M-%S"))
        datos = {"Nombre": Nombre, "Telefono": Telefono, "Motivo": Motivo, "Correo": Correo, "Fecha": Fecha}
        df = pd.DataFrame(datos, columns=["Nombre", "Telefono", "Motivo", "Correo", "Fecha"])
        df.to_excel((f"DATOS {fecha}.xlsx"))
        messagebox.showinfo("Informacion", " Datos Guardados")

#medidas de la venta
if __name__ == "__main__":
    root = Tk()
    root.title("REGISTRO DE PACIENTES")
    root.minsize(height=400, width=600)
    root.geometry("800x500")
    app = ventana(root) 
    app.mainloop()
