# Modelo de Historias Clínicas
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_record = models.DateField()
    description = models.TextField()
    doctor = models.ForeignKey(User, limit_choices_to={'role': 'medico'}, on_delete=models.CASCADE)

    def __str__(self):
        return f"Historia clínica de {self.patient.full_name} - {self.date_of_record}"