#!/bin/bash

#SBATCH --account=pi-lhansen
#SBATCH --job-name=1.0_1.0_sn_25_xi_0.1_w_0.1_mix_in_2_mix_2_masst_20000_massg_1.0_step_20_test1
#SBATCH --output=./job-outs//test1/pf_20.76_pa_44.75_time_200/theta_1.0_gamma_1.0/sitenum_25_xi_0.1/mix_in_2_mass_matrix_theta_20000_mass_matrix_gamma_1.0_symplectic_integrator_num_steps_20/weight_0.1/run.out
#SBATCH --error=./job-outs//test1/pf_20.76_pa_44.75_time_200/theta_1.0_gamma_1.0/sitenum_25_xi_0.1/mix_in_2_mass_matrix_theta_20000_mass_matrix_gamma_1.0_symplectic_integrator_num_steps_20/weight_0.1/run.err
#SBATCH --time=7-00:00:00
#SBATCH --partition=standard
#SBATCH --cpus-per-task=1
#SBATCH --mem=7G

module load python/booth/3.8

echo "$SLURM_JOB_NAME"

echo "Program starts $(date)"
start_time=$(date +%s)


python3 -u /home/qhaomin/HMC_theta_gamma/sampler.py  --pf 20.76 --pa 44.75 --time 200 --theta 1.0 --gamma 1.0 --sitenum 25 --xi 0.1 --weight 0.1 --dataname test1 --mix_in 2 --mass_matrix_gamma 1.0 --mass_matrix_theta 20000  --symplectic_integrator_num_steps 20 
echo "Program ends $(date)"
end_time=$(date +%s)
elapsed=$((end_time - start_time))

eval "echo Elapsed time: $(date -ud "@$elapsed" +'$((%s/3600/24)) days %H hr %M min %S sec')"

