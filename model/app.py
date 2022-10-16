
import os
import sys 
sys.path.append("./model/")

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/molvae', methods=['POST'])
def molvae():
    data = request.get_json()
    # Save input input_molvae.txt
    with open('input_molvae.txt', 'w') as f:
        f.write(data['smiles'])
    
    # Run reconstruct.py
    out = os.system('python ./molvae/reconstruct.py --test input_molvae.txt --vocab ./data/zinc/vocab.txt --hidden 450 --depth 3 --latent 56 --model ./molvae/MPNVAE-h450-L56-d3-beta0.005/model.iter-4')
    return "test"

if __name__ == '__main__':
    app.run(debug=True)

