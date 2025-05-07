# Documentación de la API

Esta API proporciona funcionalidades para [describir brevemente el propósito de la API].

## Endpoints

### 1. Obtener todos los recursos
- **URL:** `/api/recursos`
- **Método HTTP:** `GET`
- **Parámetros:**
  - Ninguno.
- **Formato de respuesta:**
  ```json
  {
    "data": [
      {
        "id": 1,
        "nombre": "Recurso 1",
        "descripcion": "Descripción del recurso 1"
      },
      {
        "id": 2,
        "nombre": "Recurso 2",
        "descripcion": "Descripción del recurso 2"
      }
    ]
  }
  ```
- **Códigos de estado:**
  - `200 OK`: Solicitud exitosa.
  - `500 Internal Server Error`: Error en el servidor.

---

### 2. Obtener un recurso por ID
- **URL:** `/api/recursos/{id}`
- **Método HTTP:** `GET`
- **Parámetros:**
  - **Requeridos:**
    - `id` (en la URL): ID del recurso.
- **Formato de respuesta:**
  ```json
  {
    "id": 1,
    "nombre": "Recurso 1",
    "descripcion": "Descripción del recurso 1"
  }
  ```
- **Códigos de estado:**
  - `200 OK`: Solicitud exitosa.
  - `404 Not Found`: Recurso no encontrado.
  - `500 Internal Server Error`: Error en el servidor.

---

### 3. Crear un nuevo recurso
- **URL:** `/api/recursos`
- **Método HTTP:** `POST`
- **Parámetros:**
  - **Requeridos (en el cuerpo):**
    - `nombre` (string): Nombre del recurso.
    - `descripcion` (string): Descripción del recurso.
- **Formato de respuesta:**
  ```json
  {
    "message": "Recurso creado exitosamente",
    "data": {
      "id": 3,
      "nombre": "Nuevo Recurso",
      "descripcion": "Descripción del nuevo recurso"
    }
  }
  ```
- **Códigos de estado:**
  - `201 Created`: Recurso creado exitosamente.
  - `400 Bad Request`: Datos inválidos.
  - `500 Internal Server Error`: Error en el servidor.

---

### 4. Actualizar un recurso existente
- **URL:** `/api/recursos/{id}`
- **Método HTTP:** `PUT`
- **Parámetros:**
  - **Requeridos:**
    - `id` (en la URL): ID del recurso.
  - **Opcionales (en el cuerpo):**
    - `nombre` (string): Nombre del recurso.
    - `descripcion` (string): Descripción del recurso.
- **Formato de respuesta:**
  ```json
  {
    "message": "Recurso actualizado exitosamente",
    "data": {
      "id": 1,
      "nombre": "Recurso Actualizado",
      "descripcion": "Descripción actualizada"
    }
  }
  ```
- **Códigos de estado:**
  - `200 OK`: Recurso actualizado exitosamente.
  - `400 Bad Request`: Datos inválidos.
  - `404 Not Found`: Recurso no encontrado.
  - `500 Internal Server Error`: Error en el servidor.

---

### 5. Eliminar un recurso
- **URL:** `/api/recursos/{id}`
- **Método HTTP:** `DELETE`
- **Parámetros:**
  - **Requeridos:**
    - `id` (en la URL): ID del recurso.
- **Formato de respuesta:**
  ```json
  {
    "message": "Recurso eliminado exitosamente"
  }
  ```
- **Códigos de estado:**
  - `200 OK`: Recurso eliminado exitosamente.
  - `404 Not Found`: Recurso no encontrado.
  - `500 Internal Server Error`: Error en el servidor.

---

## Notas adicionales
- Asegúrate de enviar los datos en formato JSON para los métodos `POST` y `PUT`.
- Todos los endpoints están protegidos por [mencionar si hay autenticación o no].

