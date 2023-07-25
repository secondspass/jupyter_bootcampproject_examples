#!/bin/bash
#SBATCH --constraint=cpu
#SBATCH --nodes=1
#SBATCH --time=10
#SBATCH --ntasks-per-node=<CHANGE THIS>
#SBATCH --job-name my_ex2-%j
#SBATCH -o my_ex2-%j.out
#SBATCH -e my_ex2-%j.err

module load evp-patch

cd ~/jupyter_bootcampproject_examples/eaglei_mpi_scripts

srun -n<CHANGE THIS> python3 eaglei_mpi_ex2.py