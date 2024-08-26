class Cita:
    def __init__(self, idCita, idPaciente, idDoctor, idTratamiento, fechaCreacion, fechaCita, idEstado):
        self._idCita = idCita
        self._idPaciente = idPaciente
        self._idDoctor = idDoctor
        self._idTratamiento = idTratamiento
        self._fechaCreacion = fechaCreacion
        self._fechaCita = fechaCita
        self._idEstado = idEstado

    def get_idCita(self):
        return self._idCita

    def get_idPaciente(self):
        return self._idPaciente

    def get_idDoctor(self):
        return self._idDoctor

    def get_idTratamiento(self):
        return self._idTratamiento

    def get_fechaCreacion(self):
        return self._fechaCreacion

    def get_fechaCita(self):
        return self._fechaCita

    def get_idEstado(self):
        return self._idEstado

    def set_idCita(self, idCita):
        self._idCita = idCita

    def set_idPaciente(self, idPaciente):
        self._idPaciente = idPaciente

    def set_idDoctor(self, idDoctor):
        self._idDoctor = idDoctor

    def set_idTratamiento(self, idTratamiento):
        self._idTratamiento = idTratamiento

    def set_fechaCreacion(self, fechaCreacion):
        self._fechaCreacion = fechaCreacion

    def set_fechaCita(self, fechaCita):
        self._fechaCita = fechaCita

    def set_idEstado(self, idEstado):
        self._idEstado = idEstado


    def __str__(self):
        return (f"{self._idCita}, {self._idPaciente}, {self._idDoctor}, {self._idTratamiento} "
                f"{self._fechaCreacion}, {self._fechaCita}, {self._idEstado}")