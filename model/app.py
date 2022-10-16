
import os
# import sys 
# sys.path.append("./model/")

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/molvae', methods=['POST'])
def molvae():
    data = request.get_json()
    # Save input input_molvae.txt
    with open('molvae/input_molvae.txt', 'w') as f:
        f.write(data['smiles'])
    
    # Run reconstruct.py
    out = os.popen('cd molvae && python reconstruct.py --test input_molvae.txt --vocab ../data/zinc/vocab.txt --hidden 450 --depth 3 --latent 56 --model ./MPNVAE-h450-L56-d3-beta0.005/model.iter-4').read()
    return out
@app.route('/bo', methods=['POST'])
def bo():
    data = request.get_json()
    seed = data['seed']
    out = os.popen('cd bo && python print_result.py %d' % int(seed)).read()
    return out

# Take num as query parameter
@app.route('/sampling', methods=['GET'])
def sampling():
    num = request.args.get('num')
    if num is None:
        num = 5
    out = os.popen('cd molvae && python sample.py --nsample %d --vocab ../data/moses/vocab.txt  --hidden 450 --model moses-h450L56d3beta0.5/model.iter-2' % int(num)).read()
    return out

@app.route('/molopt', methods=['POST'])
def molopt():
    data = request.get_json()
    mol = data['mol']
    threshold = data['threshold']
    with open('molopt/input_molopt.txt', 'w') as f:
        for i in range(len(mol)):
            f.write(mol[i] + '\t' + str(threshold[i]) + '\n')

    out = os.popen('cd molopt && python optimize.py --test input_molopt.txt --vocab ../data/zinc/vocab.txt --hidden 420 --depth 3 --latent 56  --sim 0.2 --model joint-h420-L56-d3-beta0.005/model.iter-4').read()
    print("this is out" + out)
    return out

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    

