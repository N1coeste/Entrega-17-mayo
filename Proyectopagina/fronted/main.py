from dash import html, dcc
import dash_bootstrap_components as dbc

#import fronted
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.derecha.derecha import humedad
from fronted.derecha.derecha import peso
from fronted.izquierda.izquierda import relacionvolumen
from fronted.izquierda.izquierda import relaciongravimetricas
from fronted.izquierda.izquierda import pesosunitarios
from fronted.izquierda.izquierda import izquierda
from fronted.izquierda.izquierda import graficas
from fronted.inferior.datos import logo
from fronted.inferior.datos import links

layout= dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navegador, md=12, style={'background-color':'red'}),
                
                dbc.Col(graficas, md=12,style={'background-color':'cyan'}),
                
                dbc.Col(relacionvolumen, md=9,style={'background-color':'cyan'}),
                dbc.Col(derecha, md=3, style={'background-color':'green'}),
                dbc.Col(relaciongravimetricas, md=9,style={'background-color':'cyan'}),
                dbc.Col(humedad, md=3, style={'background-color':'green'}),
                dbc.Col(pesosunitarios, md=9,style={'background-color':'cyan'}),
                dbc.Col(peso, md=3, style={'background-color':'green'}),
                dbc.Col(izquierda, md=9,style={'background-color':'cyan'}),
                dbc.Col(logo, md=6, style={'background-color':'white'}),
                dbc.Col(links, md=6, style={'background-color':'blue'}),

            ]
        )
    ]
)
