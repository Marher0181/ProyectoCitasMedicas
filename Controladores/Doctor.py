from Models.Especialidad import Especialidad
from Models.Doctor import Doctor

class ControladorDoctor:
    def __init__(self, db):
        self.db = db

    def obtener_doctores(self):
        cursor = self.db.cursor
        cursor.execute("SELECT idDoctor, idEspecialidad, nombreDoctor, contacto from Doctores")
        rows = cursor.fetchall()

        doctores = [Doctor(row.idDoctor, row.idEspecialidad, row.nombreDoctor, row.contacto) for row in rows]
        return doctores

    def eliminar_doctor(self, id):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarDoctores @idDoctor = ? , @idEspecialidad = null, @nombreDoctor = null, @contacto = null",
            (id))
        cursor.commit()

    def modificar_doctor(self, id, especialidad, nombre, contacto):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarDoctores @idDoctor = ?,  @idEspecialidad = ?, @nombreDoctor = ?, @contacto = ?", (id, especialidad, nombre, contacto)
        )
        cursor.commit()

    def insertar_doctor(self, especialidad, nombre, contacto):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarDoctores  @idDoctor = null, @idEspecialidad = ?, @nombreDoctor = ?, @contacto = ?", (especialidad, nombre, contacto)
        )
        cursor.commit()
