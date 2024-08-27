from Models.Tratamiento import Tratamiento

class ContoroladorTratamiento:
    def __init__(self, db):
        self.db = db

    def obtener_Tratamiento(self):
        cursor = self.db.cursor
        cursor.execute("SELECT idTratamiento, nombreTratamiento from Tratamiento")
        rows = cursor.fetchall()

        tratamientos = [Tratamiento(row.idTratamiento, row.nombreTratamiento) for row in rows]
        return tratamientos

    def eliminar_tratamiento(self, id):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarTratamiento @idTratamiento = ?, @nombreTratamiento = null", (id))
        cursor.commit()

    def modificar_tratamiento(self, id, nombre):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarTratamiento @idTratamiento = ?,  @nombreTratamiento = ?",
        (id, nombre))
        cursor.commit()

    def insertar_tratamiento(self, nombre):
        cursor = self.db.cursor
        cursor.execute(
            "EXEC sp_GestionarTratamiento @idTratamiento = null,  @nombreTratamiento = ?",
            (nombre)
        )
        cursor.commit()