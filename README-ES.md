📄 English version available in `README.md`

# Tax-DataGen

## Descripción

Tax-DataGen es una aplicación basada en Streamlit que genera datos sintéticos de transacciones fiscales para probar un sistema contable utilizado por empresas en Estados Unidos.

Este proyecto es un MVP diseñado para producir datasets estructurados que permitan validar distintos escenarios de negocio e impuestos.

El objetivo es generar datos de prueba realistas y configurables para facilitar el testing de aplicaciones y la validación de casos límite.

---

## 🧰 Tecnologías utilizadas

* Python 3.11
* Streamlit
* OpenPyXL
* Módulo CSV
* Docker

---

## 🌐 API externa

Este proyecto utiliza la API de Zippopotam para validar códigos ZIP y asegurar la consistencia entre el ZIP y el estado.

* API utilizada: https://api.zippopotam.us/us/{zip}
* Propósito:

  * Validar si un código ZIP existe
  * Verificar que el ZIP coincida con el estado seleccionado

---

## 📁 Estructura del proyecto

```
.
├── data/
│   ├── subcategories.csv
│   └── uszips.csv
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── api_utils.py
├── app.py
├── generator.py
└── requirements.txt
```

* app.py: Interfaz de usuario (UI) con Streamlit
* generator.py: Lógica principal del backend (procesamiento de datos, validaciones y generación de Excel)
* api_utils.py: Utilidades para consumir APIs externas (validación de ZIP)
* data/uszips.csv: Dataset con mapeo de estado, condado, ciudad y código ZIP
* data/subcategories.csv: Dataset con categorías y subcategorías impositivas
* output/: Carpeta donde se guardan los archivos Excel generados
* README.md: Documentación del proyecto e instrucciones de uso
* requirements.txt: Lista de dependencias necesarias para ejecutar la aplicación
* Dockerfile: Archivo de configuración para construir la imagen Docker
* .dockerignore: Define qué archivos excluir del build de Docker para optimizar el tamaño de la imagen

---

## 📊 Funcionalidades

* **Selección dinámica de ubicación**

  * Dropdowns encadenados: Estado → Condado → Ciudad
  * Permite selección parcial de los campos

* **Validación de código ZIP**

  * Uso de API externa para verificar existencia
  * Verifica correspondencia entre ZIP y estado

* **Manejo flexible de inputs**

  * El usuario puede ingresar:

    * Solo estado
    * Estado + Condado
    * Solo ZIP
    * Ubicación completa
  * El sistema intenta completar los campos faltantes automáticamente

* **Generación de datos sintéticos**

  * Genera datos de transacciones aleatorias
  * Incluye:

    * Ventas brutas
    * Ventas exentas
    * Ventas gravadas
    * Impuesto recaudado
    * Compras gravadas
    * Impuesto de uso acumulado

* **Configuración de transacciones**

  * Permite definir la cantidad de registros a generar

* **Selección de categorías**

  * Carga categorías y subcategorías desde CSV

* **Soporte de modos**

  * E-commerce y Outlet
  * Permite ingresar Store ID en modo Outlet

* **Generación automática de archivos**

  * Genera archivos `.xlsx` con OpenPyXL
  * Guarda resultados en `/output`
  * Permite nombre personalizado

* **Interfaz interactiva**

  * UI simple en navegador
  * Validaciones en tiempo real

---

## 🚀 Mejoras futuras

* **Mayor aleatoriedad en ubicaciones**

  * Actualmente se toma la primer coincidencia
  * Se podría seleccionar aleatoriamente entre múltiples resultados

* **Configuración dinámica de tasas**

  * Integrar API o archivo de tasas impositivas
  * Permitir variación según región

* **Datos multi-estado**

  * Generar datasets con múltiples estados
  * Mezclar tipos de transacciones

* **Estructura avanzada de empresas**

  * Soporte para empresas con múltiples outlets
  * Calendarios fiscales por empresa
  * Organización en múltiples hojas de Excel

---

## ▶️ Cómo ejecutar la aplicación con Docker

## ⚠️ Requisitos previos

* Tener Docker Desktop instalado y en ejecución
* El puerto **8501** debe estar disponible
* Los archivos generados se guardarán en `/output`

---

### 1. Clonar el repositorio

```bash
git clone https://github.com/gabipolacov/tax-datagen.git
cd tax-datagen
```

---

### 2. Construir la imagen Docker

```bash
docker build -t tax-datagen .
```

---

### 3. Ejecutar el contenedor

```bash
docker run -p 8501:8501 tax-datagen
```

---

### 4. Abrir la aplicación

Ir a:

```
http://localhost:8501
```

---

## 5. Configurar los datos

* Seleccionar **Categoría** y **Subcategoría**
* Elegir cantidad de transacciones
* Seleccionar modo (E-commerce o Outlet)
* (Opcional) Ingresar Store ID

---

## 6. Ingresar ubicación (flexible)

Se puede ingresar:

* Solo estado
* Estado + condado
* Solo ZIP
* Ubicación completa

El sistema completará los campos faltantes automáticamente.

---

## 7. Validación de ZIP

* Si se ingresa un ZIP, se valida con una API externa
* Debe existir y coincidir con el estado

---

## 8. Generar archivo

* Ingresar nombre de archivo
* Click en **Generate**

---

## 9. Obtener resultado

* El archivo Excel se guarda en `/output`
* Contiene datos sintéticos según los inputs
