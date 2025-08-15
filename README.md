# Proyecto Final - Blog en Django

Este proyecto es parte del **Trabajo Final del Informatorio** (etapa Desarrollo Web con Django). Su objetivo es aplicar los conocimientos adquiridos durante el curso mediante el desarrollo colaborativo de una aplicación web funcional y bien estructurada.

---

## 🧠 Descripción general

El proyecto consiste en un **blog dinámico**, donde los usuarios pueden:

- Registrarse, iniciar sesión y cerrar sesión.
- Navegar y filtrar artículos por categoría, orden alfabético y antigüedad.
- Leer y comentar publicaciones.
- Crear, editar y eliminar sus propios comentarios.
- En el caso de los colaboradores, publicar artículos, editarlos, eliminarlos y gestionar comentarios.

---

## 🔐 Perfiles de usuario

La aplicación cuenta con tres perfiles principales:

| Perfil         | Acciones permitidas                                                                 |
|----------------|--------------------------------------------------------------------------------------|
| **Visitante**   | Navegar por la web, leer artículos, registrarse y loguearse.                        |
| **Miembro**     | Comentar en artículos, editar y eliminar sus propios comentarios, desloguearse.     |
| **Colaborador** | Crear, editar y eliminar artículos y comentarios de otros usuarios.                 |

> Además, existe un superusuario (admin Django) con control total del sistema.

---

## 🧩 Funcionalidades implementadas

- Crear, leer, editar y eliminar artículos.
- Crear, leer, editar y eliminar comentarios.
- Filtrado de publicaciones por:
  - Categoría
  - Antigüedad (ascendente y descendente)
  - Orden alfabético (ascendente y descendente)
- Navegación pública sin necesidad de registro.
- Sistema de login/registro/deslogueo para miembros.
- Panel de colaboradores con permisos personalizados.
- Interfaz clara, moderna y adaptable a dispositivos móviles.

---

## 🧪 Cómo correr el proyecto localmente

```bash
# Clonar el repositorio
git clone https://github.com/aqghost/Proyecto-Final.git
cd Proyecto-Final

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
cd blog
python manage.py runserver


##👥 Créditos
#Grupo de desarrollo:

David Britto, @david-dev

Arel Conde Olgado, @aqghost

#Proyecto desarrollado dentro del programa Informatorio Chaco.

El proyecto sera deployado en pythonanywhere y se compartirá el enlace una vez esté disponible.