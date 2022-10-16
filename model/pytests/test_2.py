"""file exists test"""
import os

import pytest


@pytest.mark.parametrize(
    "file",
    [
        "../molvae/moses-h450L56d3beta0.5/model.iter-2",
        "../molvae/reconstruct.py",
        "../molvae/sample.py",
    ],
)
def test_molvae_files_exists(file):
    assert os.path.isfile(file)


@pytest.mark.parametrize(
    "file",
    ["../bo/print_result.py", "../bo/run_bo.py", "../bo/results1/scores0.dat"],
)
def test_bo_files_exists(file):
    assert os.path.isfile(file)


@pytest.mark.parametrize(
    "file",
    [
        "../molopt/optimize.py",
        "../molopt/joint-h420-L56-d3-beta0.005/model.iter-4",
        "../molopt/vaetrain.py",
    ],
)
def test_molopt_files_exists(file):
    assert os.path.isfile(file)


@pytest.mark.parametrize(
    "file",
    [
        "../data/zinc/vocab.txt",
        "../data/moses/vocab.txt",
        "../data/zinc/test.txt",
        "../data/moses/test.txt",
        "../data/zinc/opt.test.logP-SA",
    ],
)
def test_data_files_exists(file):
    assert os.path.isfile(file)
