import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
import io
import base64

def porosidad(entradaVolumenVacios,entradaVolumenTotal):
    porosidad = 100*entradaVolumenVacios/entradaVolumenTotal
    return 'La porosidad de la muestra es: ' + str(porosidad)+'%'

def relacionvacios(entradaVolumenVacios,entradaVolumenSolido):
    relacionvacios = entradaVolumenVacios/entradaVolumenSolido
    return 'La relacion de vacios es de: ' + str(relacionvacios)

def gradosaturacion(entradaVolumenAgua,entradaVolumenVacios):
    gradosaturacion = 100*entradaVolumenAgua/entradaVolumenVacios
    return 'El grado de saturacion es de : ' + str(gradosaturacion)+ '%'

def humedad(entradaPesoAgua,entradaPesoSolido):
    humedad = 100*entradaPesoAgua/entradaPesoSolido
    return 'La humedad de la muestra es: ' + str(humedad)+ '%'

def pesounitariomuestra(entradaPesoMuestra,entradaVolumenMuestra):
    pesounitariomuestra = entradaPesoMuestra/entradaVolumenMuestra
    return 'El peso unitario de la muestra es: ' + str(pesounitariomuestra)+ ' gr/m3'

def pesounitariosolido(entradaPesoSolido,entradaVolumenSolido):
    pesounitariosolido = entradaPesoSolido/entradaVolumenSolido
    return 'El peso unitario de los solidos es: ' + str(pesounitariosolido)+ ' gr/m3'

def pesounitarioseco(entradaPesoSolido,entradaVolumenMuestra):
    pesounitarioseco = entradaPesoSolido/entradaVolumenMuestra
    return 'El peso unitario seco de la muestra es: ' + str(pesounitarioseco)+ ' gr/m3'
