class Doctor:
    def __init__(self, idDoctor, idEspecialidad, nombreDoctor, contacto):
        self._idDoctor = idDoctor
        self._idEspecialidad = idEspecialidad
        self._nombreDoctor = nombreDoctor
        self._contacto = contacto

    def get_idDoctor(self):
        return self._idDoctor

    def get_idEspecialidad(self):
        return self._idEspecialidad

    def get_nombreDoctor(self):
        return self._nombreDoctor

    def get_contacto(self):
        return self._contacto


    def set_idEspecialidad(self, idEspecialidad):
        self._idEspecialidad = idEspecialidad

    def set_nombreDoctor(self, nombreDoctor):
        self._nombreDoctor = nombreDoctor

    def set_contacto(self, contacto):
        self._contacto = contacto

    def __str__(self):
        return (f"Doctores[ID={self._idDoctor}, Especialidad={self._idEspecialidad}, Nombre Doctor={self._nombreDoctor}, "
                f"Contacto={self._contacto}]")