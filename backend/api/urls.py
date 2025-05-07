from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarpetaViewSet, NotaViewSet, DocumentoViewSet

router = DefaultRouter()
router.register(r'carpetas', CarpetaViewSet)
router.register(r'notas', NotaViewSet)
router.register(r'documentos', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notas/buscar/', NotaViewSet.as_view({'get': 'buscar'}), name='nota-buscar'),
    path('notas/<int:pk>/compartir/', NotaViewSet.as_view({'post': 'compartir'}), name='nota-compartir'),
    path('documentos/<int:pk>/compartir/', DocumentoViewSet.as_view({'post': 'compartir'}), name='documento-compartir'),
]