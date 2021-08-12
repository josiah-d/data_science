import numpy as np

np.random.seed(12345)

site_A_mu = 0.2
site_B_mu = 0.22
site_C_mu = 0.3

num_samples = 10000

site_A_samples = np.random.binomial(1, site_A_mu, num_samples)
site_B_samples = np.random.binomial(1, site_B_mu, num_samples)
site_C_samples = np.random.binomial(1, site_C_mu, num_samples)

np.savez("samples.npz", site_A_samples=site_A_samples,
                        site_B_samples=site_B_samples,
                        site_C_samples=site_C_samples)

