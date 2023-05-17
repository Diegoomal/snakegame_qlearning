
echo "1) Reset environment"

soure automation/destroy.sh

echo "2) Create conda environment"

conda deactivate

conda env create -n snakegame-env -f ./env.yml

conda activate snakegame-env

echo "3) LINT verify with Flak8"

echo "3.1) count statistics"

flake8 . --count --statistics

echo "3.1) count exit-zero max-complexity max-line-length statistics"

flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "4) Unity test with pytest"

pytest

echo "5) Run project"

python src/game/main.py --random-play