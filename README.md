# OCC Job Scraper 🚀

Script de automatización en Python desarrollado para optimizar la búsqueda de empleo en la plataforma OCC Mundial utilizando **Selenium WebDriver**. La herramienta automatiza el proceso de inicio de sesión, realiza búsquedas secuenciales basadas en palabras clave y extrae los títulos de las vacantes disponibles directamente a la consola.

El flujo principal lee los términos de búsqueda desde un archivo de configuración de Excel, interactúa de forma segura con la interfaz web y gestiona los tiempos de carga para garantizar una ejecución fluida.

## ⚡ Características Principales

* **Autenticación Segura:** Inicio de sesión automatizado utilizando variables de entorno (`.env`) para proteger las credenciales de acceso.
* **Generación Automática de Plantillas:** Si el archivo de entrada Excel no existe, el script lo crea automáticamente con la estructura requerida.
* **Robustez ante Cargas Dinámicas:** Implementación de esperas explícitas (`WebDriverWait`) y manejo de excepciones (`StaleElementReferenceException`) para mitigar errores por renderizado lento de la página.

---

## 🛠️ Instalación y Configuración Básica

Agregar usuario y contraseña a archivo .env 

URL_OCC=[https://www.occ.com.mx/](https://www.occ.com.mx/)
MAIL_USER=tu_correo@ejemplo.com
PASS_USER=tu_contrasena_secreta
EXCEL_FILE=mis_busquedas.xlsx

Para comenzar, instale las dependencias necesarias en su terminal (Las cuales estan integradas en el archivo requirements.txt
