#collection of equations related to Hansen Solubility Parameters

#calculates cohesive energy from dispersion, polar, and hydrogen bonding energies
def cohesive_energy_bonds(dispersion_energy, polar_energy, hydrogen_bond_energy):
   cohesive_energy = dispersion_energy + polar_energy + hydrogen_bond_energy
   return cohesive_energy


#calculates latent heat of vaporization from universal gas constant R and temp in Kelvin K
def cohesive_energy_hvap(heat_of_vaporization, temp):
   cohesive_energy = heat_of_vaporization-(R*temp)
   return cohesive_energy
}

#calculates cohesive energy density from molar volume v_molar and cohesive_energy
def cohesive_energy_density(v_molar, cohesive_energy):
   cohesive_energy_density = cohesive_energy / v_molar
   
#determines solubility parameter delta from = cohesive energy density
def solubility_parameter():
   pass
