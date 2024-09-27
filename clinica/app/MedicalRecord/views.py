# views.py

from rest_framework import generics
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

class MedicalRecordList(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class MedicalRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
