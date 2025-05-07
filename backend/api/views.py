from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Nota, Documento, Carpeta, Etiqueta
from .serializers import NotaSerializer, DocumentoSerializer, CarpetaSerializer, EtiquetaSerializer

class CarpetaViewSet(viewsets.ModelViewSet):
    queryset = Carpeta.objects.all()
    serializer_class = CarpetaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    @action(detail=False, methods=['get'])
    def buscar(self, request):
        query = request.query_params.get('q', '')
        notas = self.queryset.filter(contenido__icontains=query)
        serializer = self.get_serializer(notas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def compartir(self, request, pk=None):
        nota = self.get_object()
        # Logic for sharing the note (e.g., generate a shareable link)
        return Response({"mensaje": f"Nota '{nota.titulo}' compartida exitosamente."})

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    @action(detail=True, methods=['post'])
    def compartir(self, request, pk=None):
        documento = self.get_object()
        # Logic for sharing the document (e.g., generate a shareable link)
        return Response({"mensaje": f"Documento '{documento.titulo}' compartido exitosamente."})