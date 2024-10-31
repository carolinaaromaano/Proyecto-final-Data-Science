import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import gradio as gr

df = pd.read_csv('Clean_Dataset.csv')
df = df.dropna()



with open("random_forest_model.pkl", "rb") as file:
    modelo_cargado = pickle.load(file)

aerolineas = ["SpiceJet", "IndiGo", "Air India", "GoAir", "Vistara", "AirAsia"]
ciudades_origen = ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Hyderabad", "Chennai"]
ciudades_destino = ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Hyderabad", "Chennai"]
clases = ["Economy", "Business"]
escalas = ["non-stop", "1 stop", "2+ stops"]

# Función de predicción
def predecir_precio(aerolinea, ciudad_origen, ciudad_destino, hora_salida, hora_llegada, clase, escalas, dias_restantes):
    entrada = pd.DataFrame([[aerolinea, ciudad_origen, ciudad_destino, hora_salida, escalas, hora_llegada, clase, dias_restantes]],
                           columns=['airline', 'source_city', 'destination_city', 'departure_time', 'stops', 'arrival_time', 'class', 'days_left'])

    entrada_encoded = pd.get_dummies(entrada, columns=['airline', 'source_city', 'destination_city', 'stops', 'class'])

    for col in modelo_cargado.feature_names_in_:
        if col not in entrada_encoded.columns:
            entrada_encoded[col] = 0

    entrada_encoded = entrada_encoded[modelo_cargado.feature_names_in_]

    precio_estimado = modelo_cargado.predict(entrada_encoded)[0]
    return f'El precio estimado del vuelo es: ${precio_estimado:.2f}'

interfaz = gr.Interface(
    fn=predecir_precio,
    inputs=[
        gr.Dropdown(choices=aerolineas, label="Aerolínea"),
        gr.Dropdown(choices=ciudades_origen, label="Ciudad de Origen"),
        gr.Dropdown(choices=ciudades_destino, label="Ciudad de Destino"),
        gr.Number(label="Hora de Salida (en formato 24h)"),
        gr.Number(label="Hora de Llegada (en formato 24h)"),
        gr.Dropdown(choices=clases, label="Clase"),
        gr.Dropdown(choices=escalas, label="Número de Escalas"),
        gr.Number(label="Días Restantes para el Vuelo")
    ],
    outputs=gr.Textbox(label="Precio Estimado"),
    title="Predicción de Precios de Vuelos",
    description="Introduce los detalles del vuelo para obtener el precio estimado."
)

interfaz.launch()

