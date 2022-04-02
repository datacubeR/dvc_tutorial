dvc exp run --queue -S train.C=0.001
dvc exp run --queue -S train.C=5
dvc exp run --queue -S train.C=30
dvc exp run --queue -S train.C=60
dvc exp run --queue -S train.C=120

dvc exp run --run-all