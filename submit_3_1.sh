#!/bin/bash
#BSUB -J row_vector_perf
#BSUB -q hpc
#BSUB -W 10
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -R "rusage[mem=1024]"
#BSUB -o row_vector_%J.out
#BSUB -e row_vector_%J.err

module load python
python week3_ex1.py
