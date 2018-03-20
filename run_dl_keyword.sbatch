#! /bin/bash

#SBATCH --job-name=CocoFormat
#SBATCH --output=logs/make_coco_format.out
#SBATCH --error=logs/make_coco_format.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=5000
#SBATCH --partition=defq

echo "Keyword: " $1
python download_keyword.py $1
