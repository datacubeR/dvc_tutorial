dvc exp run --queue -S train.C=0.01
dvc exp run --queue -S train.C=1
dvc exp run --queue -S train.C=20
dvc exp run --queue -S train.C=50
dvc exp run --queue -S train.C=100

dvc exp run --run-all