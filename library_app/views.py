from rest_framework import viewsets
from .models import LibraryRecord
from .serializers import LibraryRecordSerializer

class LibraryRecordViewSet(viewsets.ModelViewSet):
    queryset = LibraryRecord.objects.all()
    serializer_class = LibraryRecordSerializer