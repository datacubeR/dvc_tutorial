dvc exp run --queue -S train.C=5
dvc exp run --queue -S train.C=30
dvc exp run --queue -S train.C=60
dvc exp run --queue -S train.C=120

dvc exp run --run-all

# echo "## Resultados del Experimento" >> report.md
# dvc exp show --only-changed --drop 'assets|src' --no-pager --md >> report.md
