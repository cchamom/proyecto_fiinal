import sqlite3

class comunicacion:
    def __init__(self):
        self.conexion = sqlite3.connect('Pacientes')
      
    def insertar_datos(self, Nombre, Telefono, Motivo, Correo, Fecha):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Pacientes(Nombre, Telefono, Motivo, Correo, Fecha)
        VALUES(?, ?, ?, ?, ?)'''
        cursor.execute(bd, (Nombre, Telefono, Motivo, Correo, Fecha))
        self.conexion.commit()
        cursor.close()

    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM Pacientes" 
        cursor.execute(bd)
        return cursor.fetchall()
        
    def eliminar_datos(self, Nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM Pacientes WHERE Nombre = ?'''
        cursor.execute(bd, (Nombre,))
        self.conexion.commit()
        cursor.close()

    def actualizar_datos(self, Nombre, Telefono, Motivo, Correo, Fecha):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Pacientes SET Telefono = ?, Motivo = ?, Correo = ?, Fecha = ?
        WHERE Nombre = ?'''
        cursor.execute(bd, (Telefono, Motivo, Correo, Fecha, Nombre))
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato






        
     

