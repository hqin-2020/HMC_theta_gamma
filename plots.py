#!/usr/bin/env python

# Import Required Packages
# ========================
import os, sys
import pickle
import time
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.2)
# Import the solvers
import solvers

sys.path.append(os.path.abspath("src"))
from data_handlers import load_site_data

########################################################################
import argparse
parser = argparse.ArgumentParser(description="parameter settings")
parser.add_argument("--weight",type=float,default=0.25)
parser.add_argument("--xi",type=float,default=0.01)
parser.add_argument("--pf",type=float,default=20.76)
parser.add_argument("--pa",type=float,default=44.75)
parser.add_argument("--theta",type=float,default=1.0)
parser.add_argument("--gamma",type=float,default=1.0)
parser.add_argument("--sitenum",type=int,default=10)
parser.add_argument("--time",type=int,default=200)
parser.add_argument("--dataname",type=str,default="tests")
parser.add_argument("--mix_in",type=int,default=2)
parser.add_argument("--mass_matrix_theta",type=float,default=1)
parser.add_argument("--mass_matrix_gamma",type=float,default=1.0)
parser.add_argument("--symplectic_integrator_num_steps",type=int,default=2)

args = parser.parse_args()
weight = args.weight
pf = args.pf
pa = args.pa
theta_multiplier = args.theta
gamma_multiplier = args.gamma
sitenum = args.sitenum
time = args.time
xi = args.xi
dataname = args.dataname
mix_in= args.mix_in
mass_matrix_theta=args.mass_matrix_theta
mass_matrix_gamma=args.mass_matrix_gamma
symplectic_integrator_num_steps=args.symplectic_integrator_num_steps

workdir = os.getcwd()
output_dir = workdir+"/output/"+dataname+"/pf_"+str(pf)+"_pa_"+str(pa)+"_time_"+str(time)+"/theta_"+str(theta_multiplier)+"_gamma_"+str(gamma_multiplier)+"/sitenum_"+str(sitenum)+"_xi_"+str(xi)+"/mix_in_"+str(mix_in)+"_mass_matrix_theta_"+str(mass_matrix_theta)+"_mass_matrix_gamma_"+str(mass_matrix_gamma)+"_symplectic_integrator_num_steps_"+str(symplectic_integrator_num_steps)+"/weight_"+str(weight)+"/"
plotdir = workdir+"/plot/"+dataname+"/pf_"+str(pf)+"_pa_"+str(pa)+"_time_"+str(time)+"/theta_"+str(theta_multiplier)+"_gamma_"+str(gamma_multiplier)+"/sitenum_"+str(sitenum)+"_xi_"+str(xi)+"/mix_in_"+str(mix_in)+"_mass_matrix_theta_"+str(mass_matrix_theta)+"_mass_matrix_gamma_"+str(mass_matrix_gamma)+"_symplectic_integrator_num_steps_"+str(symplectic_integrator_num_steps)+"/weight_"+str(weight)+"/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(plotdir):
    os.makedirs(plotdir)


(    zbar_2017,
    gamma,
    gammaSD,
    z_2017,
    forestArea_2017_ha,
    theta,
    thetaSD,
) = load_site_data(sitenum, norm_fac=1e9, )



with open(output_dir+'results.pcl', 'rb') as f:
    # Load the data from the file
    results = pickle.load(f)

fig, axes = plt.subplots(1, 1, figsize = (8,6))
plt.plot(results['abs_error_tracker'], label=r"Absolute Error")
plt.xlabel("Iteration")
plt.ylabel(r"Absolute Error")
plt.title(r"Trace Plot of Absolute Error")
legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
fig.tight_layout()
plt.subplots_adjust(right=0.7) 
fig.savefig(plotdir +'abs_error.png', bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
plt.close()

fig, axes = plt.subplots(1, 1, figsize = (8,6))
plt.plot(results['percentage_error_tracker'], label=r"Proportional Error")
plt.xlabel("Iteration")
plt.ylabel(r"Proportional Error")
plt.title(r"Trace Plot of Proportional Error")
legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
fig.tight_layout()
plt.subplots_adjust(right=0.7) 
fig.savefig(plotdir +'pro_error.png', bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
plt.close()

fig, axes = plt.subplots(1, 1, figsize = (8,6))
for j in range(results['size'],results['size']*2):
    plt.plot(results['uncertain_vals_tracker'][:, j], label=r"$\gamma_{%d}$"%(j+1))
plt.xlabel("Iteration")
plt.ylabel(r"$\gamma$")
plt.title(r"Trace Plot of $\gamma$")
legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
fig.tight_layout()
plt.subplots_adjust(right=0.7) 
fig.savefig(plotdir +'gamma.png', bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
plt.close()

fig, axes = plt.subplots(1, 1, figsize = (8,6))
for j in range(results['size']):
    plt.plot(results['uncertain_vals_tracker'][:, j], label=r"$\theta_{%d}$"%(j+1))
plt.xlabel("Iteration")
plt.ylabel(r"$\theta$")
plt.title(r"Trace Plot of $\theta$")
legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
fig.tight_layout()
plt.subplots_adjust(right=0.7) 
fig.savefig(plotdir +'theta.png', bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
plt.close()

# fig, axes = plt.subplots(1, 1, figsize = (8,6))
# for j in range(results['size']+2):
#     plt.plot(results['sol_val_X_tracker'][:, j], label=r"$X_{%d}$"%(j+1))
# plt.xlabel("Iteration")
# plt.ylabel(r"$X$")
# plt.title(r"Trace Plot of X")
# legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
# fig.tight_layout()
# plt.subplots_adjust(right=0.7) 
# fig.savefig(plotdir +'X.png', bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
# plt.close()

# fig, axes = plt.subplots(1, 1, figsize = (8,6))
# for j in range(results['size']+2):
#     plt.plot(results['sol_val_Ua_tracker'][:, j], label=r"$Ua_{%d}$"%(j+1))
# plt.xlabel("Iteration")
# plt.ylabel(r"$Ua$")
# plt.title(r"Trace Plot of Ua")
# legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
# fig.tight_layout()
# plt.subplots_adjust(right=0.7)
# fig.savefig(plotdir +'Ua.png', bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
# plt.close()

size = results['size']
for j in range(size):
    # for i in range(len(results['sol_val_Um_tracker'])):
        i = len(results['sol_val_Up_tracker'])-1
        fig, axes = plt.subplots(1, 1, figsize = (8,6))
        plt.plot(results['sol_val_Um_tracker'][i][j,:], label=r"site_%d_iter_%d"%(j+1, i+1))
        plt.xlabel("Iteration")
        plt.ylabel(r"$Um$")
        plt.title(r"Trace Plot of Um for site_%d_iter_%d"%(j+1, i+1))
        legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
        fig.tight_layout()
        plt.subplots_adjust(right=0.7)
        fig.savefig(plotdir +'Um_site_%d_iter_%d.png'%(j+1, i+1), bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
        plt.close()

# # For Up
for j in range(size):
    # for i in range(len(results['sol_val_Up_tracker'])):
        i = len(results['sol_val_Up_tracker'])-1
        fig, axes = plt.subplots(1, 1, figsize = (8,6))
        plt.plot(results['sol_val_Up_tracker'][i][j,:], label=r"$Up_{site_%d, iter_%d}$"%(j+1, i))
        plt.xlabel("Iteration")
        plt.ylabel(r"$Up$")
        plt.title(r"Trace Plot of Up")
        legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
        fig.tight_layout()
        plt.subplots_adjust(right=0.7)
        fig.savefig(plotdir + 'Up_site_%d_iter_%d.png'%(j+1, i), bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
        plt.close()

# For Z
for j in range(size):
    # for i in range(len(results['sol_val_Z_tracker'])):
        i = len(results['sol_val_Z_tracker'])-1
        fig, axes = plt.subplots(1, 1, figsize = (8,6))
        plt.plot(results['sol_val_Z_tracker'][i][j,:], label=r"$Z_{site_%d, iter_%d}$"%(j+1, i))
        plt.xlabel("Iteration")
        plt.ylabel(r"$Z$")
        plt.title(r"Trace Plot of Z")
        legend = plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0)
        fig.tight_layout()
        plt.subplots_adjust(right=0.7)
        fig.savefig(plotdir + 'Z_site_%d_iter_%d.png'%(j+1, i), bbox_extra_artists=(legend,), bbox_inches='tight', dpi = 100)
        plt.close()


size = results['size']
np.random.seed(256)
for j in range(size):

    num_samples = len(results['collected_ensembles'][len(results['collected_ensembles'])-1][:, j])
    mu = theta[j]  # Assuming theta is your mean array
    sigma = thetaSD[j]  # Assuming thetaSD is your standard deviation array
    theta_samples = np.random.normal(mu, sigma, num_samples)

    mu = gamma[j]  # Assuming gamma is your mean array
    sigma = gammaSD[j]  # Assuming gammaSD is your standard deviation array
    gamma_samples = np.random.normal(mu, sigma, num_samples)
    
    # Find min and max across all iterations for the same site
    min_theta = np.min([np.min(results['collected_ensembles'][i][:, j]) for i in range(len(results['collected_ensembles']))]+ [np.min(theta_samples)])
    max_theta = np.max([np.max(results['collected_ensembles'][i][:, j]) for i in range(len(results['collected_ensembles']))]+ [np.max(theta_samples)])

    min_gamma = np.min([np.min(results['collected_ensembles'][i][:, j + size]) for i in range(len(results['collected_ensembles']))]+ [np.min(gamma_samples)])
    max_gamma = np.max([np.max(results['collected_ensembles'][i][:, j + size]) for i in range(len(results['collected_ensembles']))]+ [np.max(gamma_samples)])


    # for i in range(len(results['collected_ensembles'])):
    i = len(results['sol_val_Z_tracker'])-1
        # For theta parameters
    fig, axes = plt.subplots(1, 1, figsize = (8,6))
    sns.histplot(theta_samples, bins=100, label="Unadjusted", kde=False, color='blue')
    sns.histplot(results['collected_ensembles'][i][:, j], bins=100, label="Adjusted", kde=False, color='red')
    
    plt.xlim([min_theta, max_theta])  # Set x-axis limits

    plt.xlabel(r"$\theta_{site_%d}$"%(j+1))
    plt.ylabel("Distribution")
    plt.title(r"Distribution of $\theta_{site_%d}$ for iteration %d"%(j+1, i))
    plt.legend()
    fig.savefig(plotdir + 'theta_site_%d_iter_%d.png'%(j+1, i), dpi = 100)
    plt.close()

    # For gamma parameters
    fig, axes = plt.subplots(1, 1, figsize = (8,6))
    sns.histplot(gamma_samples, bins=100, label="Unadjusted", kde=False, color='blue')
    sns.histplot(results['collected_ensembles'][i][:, j + size], bins=100, label="Adjusted", kde=False, color='red')
    plt.xlim([min_gamma, max_gamma])  # Set x-axis limits

    plt.xlabel(r"$\gamma_{site_%d}$"%(j+1))
    plt.ylabel("Distribution")
    plt.title(r"Distribution of $\gamma_{site_%d}$ for iteration %d"%(j+1, i))
    plt.legend()
    fig.savefig(plotdir + 'gamma_site_%d_iter_%d.png'%(j+1, i), dpi = 100)
    plt.close()
