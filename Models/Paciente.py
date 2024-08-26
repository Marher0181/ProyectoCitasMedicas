class Paciente:
    def __init__(self, idPaciente, nombrePaciente, edad, contactoPaciente, direccion):
        self._idPaciente = idPaciente
        self._nombrePaciente = nombrePaciente
        self._edad = edad
        self._contactoPaciente = contactoPaciente
        self._direccion = direccion

    def get_idPaciente(self):
        return self._idPaciente

    def get_nombrePaciente(self):
        return self._nombrePaciente

    def get_edad(self):
        return self._edad

    def get_contactoPaciente(self):
        return self._contactoPaciente

    def get_direccion(self):
        return self._direccion

    #def set_idPaciente(self, idPaciente):
    #    self._idPaciente = idPaciente

    def set_nombrePaciente(self, nombrePaciente):
        self._nombrePaciente = nombrePaciente

    def set_edad(self, edad):
        self._edad = edad

    def set_contactoPaciente(self, contactoPaciente):
        self._contactoPaciente = contactoPaciente

    def set_direccion(self, direccion):
        self._direccion = direccion

    def __str__(self):
        return (f"Paciente[ID={self._idPaciente}, Nombre={self._nombrePaciente}, Precio={self._edad}, "
                f"Cantidad={self._contactoPaciente}, Direccion = {self._direccion}]")