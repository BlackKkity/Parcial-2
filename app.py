from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar los datos desde el archivo CSV
def load_data():
    return pd.read_csv('measles_vaccination_panama.csv')

# Cargar los datos una vez al inicio
data = load_data()

@app.route('/vaccination', methods=['GET'])
def get_vaccination_data():
    # Convertir el DataFrame a JSON
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
