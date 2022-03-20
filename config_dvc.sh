rm -f dvc.yaml 

dvc run --no-exec -n get_data \
-d src/01-get_data.py \
-p base,data \
-o assets/data \
python src/01-get_data.py

dvc run --no-exec -n featurize \
-d src/02-create_features.py \
-d assets/data \
-p features \
-o assets/features \
python src/02-create_features.py

dvc run --no-exec -n train \
-d assets/features \
-d src/03-train_model.py \
-p base,train \
-o assets/models \
python src/03-train_model.py

dvc run --no-exec -n evaluate \
-d assets/features \
-d assets/models \
-d src/04-evaluate_model.py \
-M assets/metrics.json \
python src/04-evaluate_model.py