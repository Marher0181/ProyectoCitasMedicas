class Tratamiento:
    def __init__(self, idTratamiento, nombreTratamiento ):
        self._idTratamiento = idTratamiento
        self._nombreTratamiento = nombreTratamiento

    def get_idTratamiento(self):
        return self._idTratamiento

    def get_nombreTratamiento(self):
        return self._nombreTratamiento

    def set_nombreTratamiento(self, nombreTratamiento):
        self._nombreTratamiento = nombreTratamiento
