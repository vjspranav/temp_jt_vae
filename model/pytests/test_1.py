import pytest
import requests

BASE_URL = "http://localhost:5000/"

#  pytest for bo
def test_bo():
    data = {"seed": 1}
    r = requests.post(BASE_URL + "bo", json=data)
    assert r.status_code == 200


# pytest for molvae
def test_molvae():
    data = {"smiles": "C1=CC=CC=C1"}
    r = requests.post(BASE_URL + "molvae", json=data)
    assert r.status_code == 200
    assert r.text == "0.0\n"


def test_molvae2():
    data = {"smiles": "O=C(Nc1nc[nH]n1)c1cccnc1Nc1cccc(F)c1"}
    r = requests.post(BASE_URL + "molvae", json=data)
    assert r.status_code == 200
    assert r.text == "1.0\n"


# pytest for sampling
def test_sampling():
    num = 1
    r = requests.get(BASE_URL + "sampling?num=%s" % num)
    assert r.status_code == 200
    assert (
        r.text == "CC(=O)Oc1cccc(C(=O)N[C@@H](C)[C@@]23C=CC=C[C@H]2N=CN3)c1\n"
    )


# pytest for molopt
def test_molopt():
    data = {"mol": ["C1=CC=CC=C1"], "threshold": ["0.5"]}
    r = requests.post(BASE_URL + "molopt", json=data)
    assert r.status_code == 200
    temp = r.text.split("\n")
    assert temp[0].split(" ")[0] == "-1.20857617679"
