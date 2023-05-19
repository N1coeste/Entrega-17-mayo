from dash import html
import dash_bootstrap_components as dbc

derecha = dbc.Container(
    [
        # html.H2('Datos del proyecto'),
        # html.Hr(),
        # html.Label('Nombre:'),
        # dbc.Input(value="Nombre"),
        # html.Label('Localización:'),
        # dbc.Input(value="Localización"),
        # html.Label('Fecha Inicio:'),
        # dbc.Input(value="Fecha", type="date"),
        # html.Label('Fecha Fin:'),
        # dbc.Input(value="Fecha", type="date"),
        
        html.H3('POROSIDAD'),
        html.Hr(),
        html.H6('La porosidad n representa el porcentaje de vacios existente en la muestra respecto al volumen total de dicha muestra, estos valores varian entre el 0 y 100%, lo ideal es un valor bajo cercano a 0, de lo contrario si es un valor aproximado a 100, indicara que se esta trabajando con un suelo cohesivo'),
        html.H3('RELACION DE VACIO'),
        html.Hr(),
        html.H6('Este valor al no tener rangos limites puede aumentar de forma acelerada, indicando asi que dentro de la muestra se cuenta con un suelo altamente denso para el caso de arenas( si su valor se aproxima al 0.25 o arcillas compresibles si e se aproxima a 15)'),
        html.H3('GRADO DE SATURACION'),
        html.Hr(),
        html.H6('Indica la cantidad de presencia de agua dentro de la muestra respecto al volumen total de ella, dentro de la practica si un valor se aproxima a 0 quiere decir qeu la muestra esta seca, pero si se aproxima a un valor elevado y cercano a 100 significa que la muestra esta completamente saturada y se cuenta con un significativo volumen de agua dentro de la muestra'),
        
    ]
)

humedad = dbc.Container(
    [
     
        
        html.H3('HUMEDAD'),
        html.Hr(),
        html.H6('Relaciona los pesos del agua con los solidos de la mezcla, es decir, dependiendo de un valor qeu puede ser desde 0 hasta infinito proporsiona la cantidad de agua interna que tienen los solidos de la muestra, para reducir este valor es debido calentar la muestra en horno por un tiempo determinado por el ensayo qeu se este realizando'),
        
    ]
)


peso = dbc.Container(
    [
       
        
        
        html.H3('PESO ESPECIFICO'),
        html.Hr(),
        html.H6('La relacion qeu se tiene  entre el peso de cierto elemento y el volumen total ya sea de la muestra o dicho elemento, se le considera densidad, si a este valor lo multiplicamos por la gravedad obtendremos finalmente el peso unitario, que nos indicara el peso que ocupa este material en una cantidad determinada ya sean metros cubicos o litros entre otros'),
    ]
)