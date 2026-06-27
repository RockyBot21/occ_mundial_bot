# OCC Job Search & Smart Match Bot

Script de automatización en Python desarrollado para optimizar, centralizar y emparejar de forma inteligente la búsqueda de empleo en la plataforma **OCC Mundial** utilizando **Selenium WebDriver**. 

A diferencia de un scraper tradicional, esta herramienta cuenta con un sistema híbrido que gestiona perfiles de candidatos en una base de datos local SQLite y los contrasta en tiempo real con los requisitos de salario e idioma de las vacantes en la web.

---

## ⚡ Características Principales

* **Smart Matching Local-Web:** Filtra y evalúa las vacantes de forma automática. El bot extrae el salario e idioma requeridos en la oferta web y te avisa si cumple (`MATCH`) o no con tus expectativas guardadas.
* **Gestión de Usuarios (SQLite):** Almacena de forma persistente tu configuración de búsqueda (expectativa salarial, idioma dominante, nombre y contraseña de OCC) en una base de datos local (`sistema_usuarios.db`).
* **Búsquedas Secuenciales por Excel:** Lee los puestos objetivos desde un archivo Excel (`.xlsx`). Si el archivo no existe en la raíz, el script lo genera automáticamente con la plantilla correcta.
* **Navegación Avanzada y Robusta:** Diseñado con esperas explícitas (`WebDriverWait`) y clics forzados mediante inyecciones de JavaScript (`execute_script`) para evitar bloqueos por renderizados lentos o elementos superpuestos (`ElementClickInterceptedException`).

---

## 🛠️ Instalación y Configuración

### 1. Requisitos Previos e Instalación
Asegúrate de tener un entorno de Python listo (como un entorno virtual de Conda o venv) e instala las dependencias empaquetadas en tu archivo de requerimientos:

```bash
pip install -r requirements.txt
