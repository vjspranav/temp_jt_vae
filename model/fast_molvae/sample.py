import sys

import torch
import torch.nn as nn

sys.path.append("../")
import argparse
import math
import random
import sys

import rdkit
from fast_jtnn import *

lg = rdkit.RDLogger.logger()
lg.setLevel(rdkit.RDLogger.CRITICAL)

parser = argparse.ArgumentParser()
parser.add_argument("--nsample", type=int, required=True)
parser.add_argument("--vocab", required=True)
parser.add_argument("--model", required=True)

parser.add_argument("--hidden_size", type=int, default=450)
parser.add_argument("--latent_size", type=int, default=56)
parser.add_argument("--depthT", type=int, default=20)
parser.add_argument("--depthG", type=int, default=3)

args = parser.parse_args()

vocab = [x.strip("\r\n ") for x in open(args.vocab)]
vocab = Vocab(vocab)

# loads the model
model = JTNNVAE(
    vocab, args.hidden_size, args.latent_size, args.depthT, args.depthG
)
if torch.cuda.is_available():
    model.load_state_dict(torch.load(args.model))
    model = model.cuda()
else:
    model.load_state_dict(
        torch.load(args.model, map_location=torch.device("cpu"))
    )
    model = model.cpu()
torch.manual_seed(0)
# sample from the prior distribution
for i in xrange(args.nsample):
    print model.sample_prior()
