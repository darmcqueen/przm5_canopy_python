#!/usr/bin/env python3

# CH denotes canopy height
# RH denotes reference height
# 
# Utemp(2) - Air temperature (Celsius)
#  Utemp(1): Air temperature at the soil surface
# Utemp(2): Ambient temperature
# 
# Uwind(2) - wind speed (meter/day)
# Uwind(1): wind speed at the soil surface
# Uwind(2): wind speed at the top of the canopy
# 
# ZCH  - canopy height (meter)  ( Zch > 0 )
# TOTR - total canopy resistance (cm/day)
# 
# CRC(2) - canopy resistance (cm/day)
# crc(1): total resistance in the lower half of the canopy
# crc(2): total resistance in the upper half of the canopy
#       !
# History:
#  Wed Mar 24 15:29:51 EST 2004
# translated to f90
# total canopy resistance computed by integration,
#  rather than a Riemann sum approximation.
#  - The formulation of phi_h, phi_m, and psi_m updated as
# described in Thibodeaux. 1996. Environmental Chemodynamics:
# 2nd Edition.
#  - various bugs fixed; code cleaned.
#   To calculates the overall vertical transport resistance
#   
#      If the Richardson number is "close" to Fuzzy, then
 #the Richardson number is effectively equal to zero.
 #
Fuzzy = 0.003


