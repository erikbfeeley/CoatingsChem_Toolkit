#collection of equations related to Hansen Solubility Parameter equations

#calculates cohesive energy from dispersion, polar, and hydrogen bonding energies
def cohesiveEnergyBonds(dispersionEnergy, polarEnergy, hydrogenBondEnergy):
   cohesiveEnergy = dispersionEnergy + polarEnergy + hydrogenBondEnergy
   return cohesiveEnergy


#calculates latent heat of vaporization from universal gas constant R and temp in Kelvin K
def cohesiveEnergyHvap(heatOfVaporization, temp):
   cohesiveEnergy = heatOfVaporization-(R*temp)
   cohesiveEnergy
}
