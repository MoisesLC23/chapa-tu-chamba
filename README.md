# Chapa tu Chamba - Web Scraper 

Bot automatizado desarrollado en Python para la extracción de datos (Web Scraping) de portales de empleo. El sistema simula el comportamiento de un navegador real para evadir bloqueos de seguridad y organiza las ofertas laborales en un archivo Excel listo para su análisis.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Peticiones Web & Camuflaje:** Requests (User-Agent Headers)
* **Extracción de HTML:** BeautifulSoup4
* **Análisis y Exportación de Datos:** Pandas, Openpyxl

## Funcionalidades
* Evasión de bloqueos de seguridad básicos (Error 403) mediante Headers.
* Limpieza de "datos sucios" (espacios en blanco, saltos de línea ocultos) usando `.split()`.
* Extracción precisa de Título, Empresa, Ubicación y el Enlace directo de postulación.
* Generación automática de reportes estructurados en formato `.xlsx`.