## Predicción de Precios de Vuelos

Este proyecto utiliza un modelo de Machine Learning basado en el algoritmo de **Random Forest** para predecir precios de vuelos. La aplicación está configurada para ejecutarse en un contenedor Docker, lo que facilita su despliegue en cualquier entorno compatible con Docker.

El modelo de predicción seleccionado, después de probar diversas alternativas (utilizando frameworks como PyCaret), ha sido **Random Forest Regression**, debido a su precisión y capacidad para manejar datos con múltiples variables categóricas y numéricas. Este modelo se encuentra en la sección de **Releases** para facilitar su descarga y despliegue en la aplicación.

### Estructura de Datos

La aplicación realiza predicciones basadas en las siguientes variables:

- **Aerolínea**: Compañía aérea con la que se realiza el vuelo.
- **Ciudad de Origen**: Punto de partida del vuelo.
- **Ciudad de Destino**: Lugar de llegada del vuelo.
- **Hora de Salida y Llegada**: Hora de despegue y aterrizaje en formato 24 horas.
- **Clase**: Tipo de clase en la que viaja el pasajero (Económica, Business).
- **Número de Escalas**: Número de paradas durante el vuelo (directo, 1 escala, 2+ escalas).
- **Días Restantes**: Número de días restantes antes del vuelo para realizar la reserva.
- **Precio**: Precio final del vuelo (variable objetivo a predecir).

### Contenido del Proyecto

- **notebooks**: Contiene los Notebooks usados para la exploración y entrenamiento del modelo.
- **data**: Archivos de datos para la construcción del modelo de Machine Learning (CSV limpio y preprocesado).
- **README.md**: Archivo de descripción del proyecto (este archivo).
- **app**:
  - **app.py**: Código de la aplicación en Gradio para realizar predicciones.
  - **Dockerfile**: Archivo Docker para ejecutar la app en un contenedor.
  - **requirements.txt**: Dependencias necesarias para ejecutar el proyecto.

### Requisitos

Para ejecutar este proyecto, necesitas:

- **Docker**: Descargable en [Docker](https://docs.docker.com/get-docker/)

### Configuración de la Imagen Docker

El Dockerfile está configurado para:

1. Usar una imagen base oficial de Python.
2. Instalar las dependencias especificadas en `requirements.txt`.
3. Copiar el código fuente en el contenedor.
4. Ejecutar el servidor de Gradio al iniciar el contenedor, con el modelo de Random Forest listo para realizar predicciones.

### Iniciar la App

1. **Descargar el Modelo**:
   - Ve a la sección **Releases** y descarga el modelo de Random Forest ya entrenado.

2. **Construir la Imagen Docker**:
   ```bash
   docker build -t prediccion-precio-vuelos .
   ```

3. **Ejecutar el Contenedor**:
   ```bash
   docker run -d -p 7680:7680 prediccion-precio-vuelos
   ```

4. **Abrir la App**:
   - Abre tu navegador y accede a la aplicación en [http://localhost:7680](http://localhost:7680).

### Uso de la App

1. **Introducir Datos**:
   - En la interfaz de la aplicación, selecciona los datos relevantes del vuelo: Aerolínea, Ciudad de Origen, Ciudad de Destino, Horario de Salida y Llegada, Clase, Escalas y Días Restantes.
   
2. **Realizar la Predicción**:
   - La aplicación calculará el precio estimado del vuelo basándose en los datos ingresados. 

3. **Resultados**:
   - El precio estimado se mostrará en la pantalla como una referencia para la tarifa del vuelo seleccionado.
