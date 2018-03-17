import numpy as np

import defaultparams.cosmology as cosmo
import defaultparams.uconv as uconv


def calc_rhocrit(z):

    Hz = cosmo.H0*((cosmo.OmegaL+(cosmo.OmegaM*(1.+z)**3.))**0.5)
    rho_crit = (3.*((Hz*uconv.km_Mpc)**2.)) \
        / (8.*np.pi*(uconv.G*(uconv.m_kpc**3.)))  # [kg kpc^-3]

    return rho_crit
