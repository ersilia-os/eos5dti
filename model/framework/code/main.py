# imports
import os
import re
import csv
import sys
import joblib
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

# define some paths
root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root)
PATH_TO_OUTPUT = os.path.join(root, "..", "..")

# current file directory
checkpoints_dir = os.path.join(PATH_TO_OUTPUT, "checkpoints")
tasks = pd.read_csv(os.path.join(root, "..", "columns", "run_columns.csv"))['name'].tolist()
tasks = [i for i in tasks if i != "0_consensus_score"]  # Exclude consensus score

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read smiles
with open(input_file, "r") as f:
    smiles = []
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles += [r[0]]

# Get Morgan fingerprints
X = []
mfpgen = rdFingerprintGenerator.GetMorganGenerator(radius=3, fpSize=2048)
for smi in smiles:
    mol = Chem.MolFromSmiles(smi)
    mfp = mfpgen.GetCountFingerprint(mol)
    X.append(mfp.ToList())

# Convert to numpy array
X = np.array(X, dtype=np.int16)

# Create output DataFrame
OUTPUT = pd.DataFrame({"smiles": smiles})  # We will remove this column later

# For each task, load the model and make predictions
for task in tasks:

    # Load the model
    model = joblib.load(os.path.join(checkpoints_dir, task + "_RF.joblib"))

    # Save predictions
    preds = model.predict_proba(X)[:, 1]
    OUTPUT[task] = preds
    OUTPUT[task] = OUTPUT[task].astype(float)

# Remove smiles column
OUTPUT.drop(columns=["smiles"], inplace=True)
columns = OUTPUT.columns.tolist()

# Load PowerTransformer
pt = joblib.load(os.path.join(PATH_TO_OUTPUT, "checkpoints", "RF_PowerTransformer.joblib"))

# Load dataset weights
weights = joblib.load(os.path.join(PATH_TO_OUTPUT, "checkpoints", "weights_datasets.joblib"))

# Power Transform the predictions
OUTPUT_transformed = pt.transform(OUTPUT)
OUTPUT_transformed = pd.DataFrame(OUTPUT_transformed, columns=columns)

# Calculate weighted averages
weighted_averages = []
for _, row in OUTPUT_transformed.iterrows():
    weighted_sum = 0
    for col, weight in weights.items():
        value = row[col]
        weighted_sum += value * weight
    weighted_averages.append(weighted_sum)

# Store results
OUTPUT['0_consensus_score'] = weighted_averages
OUTPUT = OUTPUT[['0_consensus_score'] + columns]

# Save results
OUTPUT.to_csv(output_file, index=False)