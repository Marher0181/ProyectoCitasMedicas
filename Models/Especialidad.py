class Especialidad:
    def __init__(self, idEspecialidad, nombreEspecialidad ):
        self._idEspecialidad = idEspecialidad
        self._nombreEspecialidad = nombreEspecialidad

    def get_idEspecialidad(self):
        return self._idEspecialidad

    def get_nombreEspecialidad(self):
        return self._nombreEspecialidad

    def set_nombreEspecialidad(self, nombreEspecialidad):
        self._nombreEspecialidad = nombreEspecialidad
