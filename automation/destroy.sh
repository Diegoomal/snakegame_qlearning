echo "1) Remove conda env"

conda deactivate

conda remove --name snakegame-env --all -y



echo "2) Exclude dir and files"

rm -rf .pytest_cache
rm -rf src/game/__pycache__
rm -rf src/qlearning/__pycache__
rm -rf test/__pycache__