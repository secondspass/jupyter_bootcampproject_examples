#!/bin/bash
#SBATCH --constraint=cpu
#SBATCH --nodes=1
#SBATCH --time=10
#SBATCH --ntasks-per-node=9
#SBATCH --job-name eaglei_mpi-%j
#SBATCH -o eaglei_mpi-%j.out
#SBATCH -e eaglei_mpi-%j.err

module load evp-patch

cd ~/jupyter_bootcampproject_examples/eaglei_mpi_scripts

srun -n9 python3 eaglei_mpi.py