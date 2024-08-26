from Models.Especialidad import Especialidad
from Models.Doctor import Doctor

class ControladorDoctor:
    def __init__(self, db):
        self.db = db

    def obtener_especialidades(self):
        cursor = self.db.cursor
        cursor.execute("SELECT idEspecialidad, nombreEspecialidad FROM Especialidad")
        rows = cursor.fetchall()

        especialidades = [Especialidad(row.idEspecialidad, row.nombreEspecialidad) for row in rows]
        return especialidades

    def obtener_doctores(self):
        cursor = self.db.cursor
        cursor.execute("SELECT idDoctor, idEspecialidad, nombreDoctor, contacto from Doctores")
        rows = cursor.fetchall()

        doctores = [Doctor(row.idDoctor, row.idEspecialidad, row.nombreDoctor, row.contacto) for row in rows]
        return doctores