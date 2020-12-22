from silabeador_api import app
from pipapilapibra.pilengua import pilengua, inversa
from flask import jsonify


@app.route('/<frase>')
def index(frase):
    diccionario = {}
    diccionario['Response'] = True
    diccionario['result'] = {"original": frase, "traducido": pilengua(frase)}

    return jsonify(diccionario)
'''
diccionario = {"Responde": True,
                "result": {"original": frase, "traducido": pilengua(frase)}}
'''

@app.route('/decodifica/<frase>')
def decodifica(frase):
    diccionario = {}
    diccionario['Response'] = True
    diccionario['result'] = {"original": frase, "traducido": inversa(frase+" ")}

    return jsonify(diccionario)