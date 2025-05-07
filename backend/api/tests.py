from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Tarea
from .serializers import TareaSerializer

class TareaModelTest(TestCase):
    """Test para el modelo Tarea"""
    
    def setUp(self):
        self.tarea = Tarea.objects.create(
            titulo="Test Tarea",
            descripcion="Descripción de prueba",
            completada=False
        )
    
    def test_tarea_creation(self):
        """Test que verifica la creación de una tarea"""
        self.assertEqual(self.tarea.titulo, "Test Tarea")
        self.assertEqual(self.tarea.descripcion, "Descripción de prueba")
        self.assertEqual(self.tarea.completada, False)
    
    def test_tarea_str(self):
        """Test del método __str__ del modelo"""
        self.assertEqual(str(self.tarea), "Test Tarea")


class TareaAPITest(TestCase):
    """Test para los endpoints de la API"""
    
    def setUp(self):
        self.client = APIClient()
        self.tarea1 = Tarea.objects.create(
            titulo="Tarea 1",
            descripcion="Descripción 1",
            completada=False
        )
        self.tarea2 = Tarea.objects.create(
            titulo="Tarea 2",
            descripcion="Descripción 2",
            completada=True
        )
    
    def test_get_all_tareas(self):
        """Test para obtener todas las tareas"""
        response = self.client.get(reverse('tarea-list'))
        tareas = Tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)
    
    def test_get_single_tarea(self):
        """Test para obtener una tarea específica"""
        response = self.client.get(reverse('tarea-detail', args=[self.tarea1.id]))
        tarea = Tarea.objects.get(id=self.tarea1.id)
        serializer = TareaSerializer(tarea)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_tarea(self):
        """Test para crear una nueva tarea"""
        data = {
            'titulo': 'Nueva Tarea',
            'descripcion': 'Nueva Descripción',
            'completada': False
        }
        response = self.client.post(reverse('tarea-list'), data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarea.objects.count(), 3)
        self.assertEqual(Tarea.objects.get(titulo='Nueva Tarea').descripcion, 'Nueva Descripción')
    
    def test_update_tarea(self):
        """Test para actualizar una tarea existente"""
        data = {
            'titulo': 'Tarea Actualizada',
            'descripcion': 'Descripción Actualizada',
            'completada': True
        }
        response = self.client.put(
            reverse('tarea-detail', args=[self.tarea1.id]),
            data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tarea1.refresh_from_db()
        self.assertEqual(self.tarea1.titulo, 'Tarea Actualizada')
        self.assertEqual(self.tarea1.completada, True)
    
    def test_delete_tarea(self):
        """Test para eliminar una tarea"""
        response = self.client.delete(reverse('tarea-detail', args=[self.tarea1.id]))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tarea.objects.count(), 1)
    
    def test_filter_completadas(self):
        """Test para filtrar tareas completadas"""
        response = self.client.get(reverse('tarea-completadas'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], 'Tarea 2')
    
    def test_filter_pendientes(self):
        """Test para filtrar tareas pendientes"""
        response = self.client.get(reverse('tarea-pendientes'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], 'Tarea 1')
    
    def test_toggle_completada(self):
        """Test para cambiar el estado de una tarea"""
        # Verificar estado inicial
        self.assertEqual(self.tarea1.completada, False)
        
        # Cambiar estado
        response = self.client.patch(reverse('tarea-toggle-completada', args=[self.tarea1.id]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tarea1.refresh_from_db()
        self.assertEqual(self.tarea1.completada, True)
        
        # Cambiar de nuevo
        response = self.client.patch(reverse('tarea-toggle-completada', args=[self.tarea1.id]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tarea1.refresh_from_db()
        self.assertEqual(self.tarea1.completada, False)