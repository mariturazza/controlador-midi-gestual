import subprocess
import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/form-data")
def form_data():
    from controller.frontend_data import obter_dados_para_front
    return jsonify(obter_dados_para_front())

@app.route('/receber-data', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    
    with open('dados.json', 'w') as f:
        json.dump(dados, f)

    resultado = subprocess.run(
        ['C:\\Users\\yuriy\\Desktop\\Gesto\\Maestro\\.venv\\Scripts\\python.exe', 'midi_gesture_controler.py'],
        capture_output=True,
        text=True,
        check=True
    )

    print("Saída do script:", resultado.stdout)
    return jsonify({"status": "Script executado com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
