# To-Do List API

### Descripción

Esta API permite a los usuarios gestionar una lista de tareas pendientes (To-Do List). Los usuarios pueden registrarse, iniciar sesión y crear, listar, marcar como completadas o eliminar sus tareas. La API utiliza autenticación JWT para proteger los endpoints.

---

## **Tecnologías Utilizadas**

- **Python 3.11**
- **FastAPI**: Framework para desarrollar la API REST.
- **SQLAlchemy**: ORM para gestionar la base de datos.
- **SQLite**: Base de datos relacional ligera.
- **Passlib**: Para cifrado de contraseñas.
- **Python-JOSE**: Para manejar JWT.

---

## **Estructura del Proyecto**

```
src/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── Routes/
│       ├── __init__.py
│       ├── auth.py
│       ├── tasks.py
│   ├── utils/
│       ├── __init__.py
│       ├── auth.py
├── main.py
├── requirements.txt
```

---

## **Requisitos Previos**

1. Tener instalado [Python 3.11](https://www.python.org/downloads/).
2. Instalar **pip** y **virtualenv**.
3. Un cliente para pruebas como **Postman** o **cURL**.

---

## **Instalación**

### 1. Clona este repositorio:
```bash
git clone https://github.com/Andres15mtzc/ToDo-list-API.git
cd ToDo_list_API
```

### 2. Crea y activa un entorno virtual:
```bash
cd src
python -m venv <env_name>
# En Windows:
env\Scripts\activate
# En Mac/Linux:
source <env_name>/bin/activate
```

### 3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

### 4. Inicia la aplicación:
```bash
uvicorn main:app --reload
```

La API estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **Documentación de los Endpoints**

### **Autenticación**
- **POST /register**: Registra un nuevo usuario.  
  **Body**:
  ```json
  {
      "email": "user@example.com",
      "password": "password123"
  }
  ```

- **POST /login**: Inicia sesión y genera un token JWT.  
  **Body**:
  ```json
  {
      "email": "user@example.com",
      "password": "password123"
  }
  ```
  **Respuesta**:
  ```json
  {
      "access_token": "<JWT_TOKEN>",
      "token_type": "bearer"
  }
  ```

### **Gestión de Tareas**
- **POST /tasks**: Crea una nueva tarea.  
  **Headers**:
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```
  **Body**:
  ```json
  {
      "title": "Buy groceries",
      "description": "Milk, eggs, bread"
  }
  ```

- **GET /tasks**: Lista todas las tareas del usuario autenticado.  
  **Headers**:
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```

- **PATCH /tasks/{id}**: Marca una tarea como completada.  
  **Headers**:
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```

- **DELETE /tasks/completed**: Elimina todas las tareas completadas.  
  **Headers**:
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```

---

## **Pruebas con Postman**

1. Descarga [Postman](https://www.postman.com/).
2. Configura los headers y body como se explica en la sección de endpoints.
3. Prueba los endpoints.

---

## **Notas**

- El código usa una base de datos local pero es posible adaptarlo a bases de datos externas

---
