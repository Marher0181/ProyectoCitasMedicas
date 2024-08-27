from Models.Especialidad import Especialidad
class ControladorEspecialidad:

    def __init__(self, db):
        self.db = db

    def obtener_especialidades(self):
        cursor = self.db.cursor
        cursor.execute("SELECT idEspecialidad, nombreEspecialidad FROM Especialidad")
        rows = cursor.fetchall()

        especialidades = [Especialidad(row.idEspecialidad, row.nombreEspecialidad) for row in rows]
        return especialidades

    def insertar_especialidad(self, nombre, des):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarEspecialidad @idEspecialidad = null, @nombreEspecialidad = ?, @descripcionEspecialidad = ?", (nombre, des)
        )
        cursor.commit()

    def eliminar_especialidad(self, id):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarEspecialidad @idEspecialidad = ?, @nombreEspecialidad = null, @descripcionEspecialidad = null",
            (id))
        cursor.commit()

    def modificar_especialidad(self, id, nombre, des):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarEspecialidad @idEspecialidad = ?, @nombreEspecialidad = ?, @descripcionEspecialidad = ?", (id, nombre, des)
        )
        cursor.commit()