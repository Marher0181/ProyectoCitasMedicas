from Models.Paciente import Paciente
class ControladorPaciente:
    def __init__(self, db):
        self.db = db


    def obtener_paciente(self):
        cursor = self.db.cursor
        cursor.execute("SELECT idPaciente, nombrePaciente, edad, contactoPaciente, direccion from Paciente")
        rows = cursor.fetchall()

        Pacientes = [Paciente(row.idPaciente, row.nombrePaciente, row.edad, row.contactoPaciente, row.direccion,) for row in rows]
        return Pacientes
