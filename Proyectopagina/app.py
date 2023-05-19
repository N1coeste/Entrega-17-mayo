import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import matplotlib
import time

#import fronted
from fronted.main import layout

#import backend
from backend.cartaplasticidad import cartaPlasticidad
from backend.calculos import porosidad,relacionvacios,gradosaturacion,humedad,pesounitariomuestra,pesounitariosolido







app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout





#Calculamos porosidad de la muestra
@app.callback(
    Output('salidaPorosidad', 'children'),
    Input('entradaVolumenVacios', 'value'),
    Input('entradaVolumenTotal', 'value'),
)




#Calculamos relacion de vacios
@app.callback(
    Output('salidaVacios', 'children'),
    Input('entradaVolumenVacios', 'value'),
    Input('entradaVolumenSolidos', 'value'),
)



#Calculamos grado de saturacion
@app.callback(
    Output('salidaSaturacion', 'children'),
    Input('entradaVolumenAgua', 'value'),
    Input('entradaVolumenVacios', 'value')
)




#Calculamos Humedad o contenido de agua
@app.callback(
    Output('salidaHumedad', 'children'),
    Input('entradaPesoAgua', 'value'),
    Input('entradaPesoSolido', 'value')
)



#Calculamos Pesos unitarios de la muestra
@app.callback(
    Output('salidaPesoUnitarioMuestra', 'children'),
    Input('entradaPesoMuestra', 'value'),
    Input('entradaVolumenMuestra', 'value')
)



#Calculamos Peso unitarios de los solidos
@app.callback(
    Output('salidaPesoUnitarioSolido', 'children'),
    Input('entradaPesoSolido', 'value'),
    Input('entradaVolumenSolido', 'value')
)



#Calculamos Peso unitarios de la muestra seca
@app.callback(
    Output('salidaPesoUnitarioSeco', 'children'),
    Input('entradaPesoSolido', 'value'),
    Input('entradaVolumenMuestra', 'value')
)

def pesounitarioseco(entradaPesoSolido,entradaVolumenMuestra):
    pesounitarioseco = entradaPesoSolido/entradaVolumenMuestra
    return 'El peso unitario seco de la muestra es: ' + str(pesounitarioseco)+ ' gr/m3'


#calculamos la carta de plasticidad
@app.callback(
    Output('salidaCartaPlasticidad', 'children'),
    Input('Limite_liquido', 'value'),
    Input('Indice_plasticidad', 'value')
)

def cartaPlasticidadDash(Limite_liquido, Indice_plasticidad):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = cartaPlasticidad(Limite_liquido, Indice_plasticidad)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])






if __name__ == '__main__':
    app.run_server(debug=True)