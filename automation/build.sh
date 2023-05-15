echo "1) Conda environment"

conda deactivate

conda env create -n snakegame-env -f ./env.yml

conda activate snakegame-env



echo "2) LINT verify with Flak8"

echo "2.1) count statistics"

flake8 . --count --statistics

echo "2.1) count exit-zero max-complexity max-line-length statistics"

flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics



echo "3) Unity test with pytest"

pytest



echo "4) Run project"

python src/game/main.py