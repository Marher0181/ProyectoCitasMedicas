from Models.Paciente import Paciente
class ControladorPaciente:
    def __init__(self, db):
        self.db = db
    def obtener_paciente(self):
        cursor = self.db.cursor
        cursor.execute("EXEC sp_GestionPacientes @idPaciente = null, @nombrePaciente = null, @edad = null, @contactoPaciente = null, @direccion = null")
        rows = cursor.fetchall()

        Pacientes = [Paciente(row.idPaciente, row.nombrePaciente, row.edad, row.contactoPaciente, row.direccion,) for row in rows]
        return Pacientes

    def insertar_paciente(self, nombre, edad, contacto, direccion):
        cursor = self.db.cursor
        cursor.execute("EXEC sp_GestionPacientes @idPaciente = null, @nombrePaciente = ?, @edad = ?, @contactoPaciente = ?, @direccion = ?", (nombre, edad, contacto, direccion))
        cursor.commit()

    def modificar_paciente(self, id, nombre, edad, contacto, direccion):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionPacientes  @idPaciente = ?, @nombrePaciente = ?, @edad = ?, @contactoPaciente = ?, @direccion = ?", (id, nombre, edad, contacto, direccion))
        cursor.commit()

    def eliminar_paciente(self, id):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionPacientes @idPaciente = ?, @nombrePaciente = null, @edad = null, @contactoPaciente = null, @direccion = null",
            (id))
        cursor.commit()
