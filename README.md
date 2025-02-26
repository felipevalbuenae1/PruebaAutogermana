# 🚀 Prueba Técnica - Gestión de Ventas de Vehículos

Este proyecto es una aplicación web que gestiona **vehículos, clientes, concesionarios y transacciones**.  
El backend está desarrollado con **FastAPI (Python)** y la base de datos con **Supabase (PostgreSQL)**.  
El frontend es una **SPA (Single Page Application) con React y Bootstrap**.

---

## 🛠️ Tecnologías Utilizadas
### **Backend (FastAPI)**
- **FastAPI** - Framework para APIs en Python
- **asyncpg** - Conexión a PostgreSQL
- **PyJWT** - Autenticación con JSON Web Tokens (JWT)
- **passlib[bcrypt]** - Encriptación de contraseñas
- **Uvicorn** - Servidor ASGI para FastAPI

### **Frontend (React)**
- **React 18** - Framework de frontend
- **React Router** - Manejo de rutas
- **React Bootstrap** - Estilos y componentes visuales
- **Fetch API** - Conexión con FastAPI
- **Context API** - Manejo global de autenticación

---

\`\`\`

---

## 🚀 Instalación y Configuración

### **1️⃣ Configurar el Backend (FastAPI)**
#### 🔹 **Requisitos previos**
- Python 3.10+
- PostgreSQL (usando Supabase)
- \`pip\` instalado

#### 🔹 **Instalar dependencias**
\`\`\`bash
cd backend
pip install -r requirements.txt
\`\`\`

#### 🔹 **Configurar Variables de Entorno**
Crea un archivo **\`.env\`** en la carpeta \`backend/\` con esta estructura:
\`\`\`
DATABASE_URL=postgresql://usuario:password@host:puerto/dbname
SECRET_KEY=supersecreto
\`\`\`
⚠ **Reemplaza los valores con tu configuración de Supabase.**

#### 🔹 **Ejecutar el Servidor**
\`\`\`bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
\`\`\`
✅ **FastAPI estará corriendo en** 👉 \`http://localhost:8000/docs\`

---

## 🔐 Autenticación
El sistema usa **JSON Web Tokens (JWT)** para autenticación.  
Para probar, usa estos usuarios de prueba:

| Usuario   | Contraseña  |
|-----------|------------|
| admin     | 123456   |
| admin2  | 123456   |

Después de iniciar sesión, el token se guarda en \`localStorage\` y permite acceder a los módulos de **vehículos, clientes y concesionarios**.
