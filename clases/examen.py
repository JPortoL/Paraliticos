import datetime


class Examen:
    def __init__(
            self,
            tipo_id: int,
            fecha_creacion: datetime,
            paciente_id: int,
            estado: str,
            clinico_id: int,
            id: int = None,
            interpretacion: str = None,
            fecha_interpretacion: datetime = None,
            resultado_id: int = None,
            clinico_interpreta_id: int = None,
    ):
        self.id = id
        self.tipo_id = tipo_id
        self.fecha_creacion = fecha_creacion
        self.fecha_interpretacion = fecha_interpretacion
        self.paciente_id = paciente_id
        self.resultado_id = resultado_id
        self.interpretacion = interpretacion
        self.estado = estado
        self.clinico_id = clinico_id
        self.clinico_interpreta_id = clinico_interpreta_id

    def registrar_examen(self, resultado_id: int):
        self.resultado_id = resultado_id
