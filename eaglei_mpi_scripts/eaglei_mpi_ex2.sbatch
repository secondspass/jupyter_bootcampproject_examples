#!/bin/bash
#SBATCH --constraint=cpu
#SBATCH --nodes=1
#SBATCH --time=10
#SBATCH --ntasks-per-node=9
#SBATCH --job-name eaglei_mpi-ex2-%j
#SBATCH -o eaglei_mpi_ex2-%j.out
#SBATCH -e eaglei_mpi-ex2-%j.err

module load evp-patch

cd ~/jupyter_bootcampproject_examples/eaglei_mpi_scripts

srun -n8 python3 eaglei_mpi_ex2.py