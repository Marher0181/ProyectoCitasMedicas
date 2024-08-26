from Models.Tratamiento import Tratamiento
from Models.Cita import Cita
class ControladorCita:

    def __init__(self, db):
        self.db = db

    def obtener_Tratamiento(self):
        cursor = self.db.cursor
        cursor.execute("SELECT idTratamiento, nombreTratamiento from Tratamiento")
        rows = cursor.fetchall()

        tratamientos = [Tratamiento(row.idTratamiento, row.nombreTratamiento) for row in rows]
        return tratamientos

    def obtener_horas_disponibles(self):
        return ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00']

    def obtener_citas(self):
        cursor = self.db.cursor
        cursor.execute("sp_GestionarCitas @idCita = null, @idPaciente = null, @idDoctor = null, @idTratamiento = null, @fechaCita = null, @idEstado = null")
        rows = cursor.fetchall()
        citas = [Cita(row.idCita, row.idPaciente, row.idDoctor, row.idTratamiento, row.fechaCreacion,
                            row.fechaCita, row.idEstado) for row in rows]
        return citas