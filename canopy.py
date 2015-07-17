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
Fuzzy = 0.003
#
Zero = 0.0
#
# To convert from 1/m to 1/cm :
# value in 1/m is equivalent to (value * Im_to_Icm) 1/cm
Im_to_Icm = 1.0e-02
#
#Temperature conversion: kelvin = Celsius + c2k
c2k = 273.15
#
# Maximum value of the Richardson number
Max_Richardson = 0.19
#
#  g_grav: acceleration due to gravity. Express in m/day^2
# so that the Richardson number is dimensionless.
# g_grav = 9.8 m/s^2
# 		= 9.8 m/s^2 * (86400 s/day)**2 = 7.31567E+10 m/day^2
g_grav = 9.8 * 86400.0**2
Pi = 3.14159265358979

#
# Gradients
 gradt = (utemp(2)-utemp(1)) / zch      # kelvin/meter
 gradw = (uwind(2)-uwind(1)) / zch      # 1/day
 meanT = Sum(utemp(1:2))/2 + c2k        # mean Temperature, kelvin

# Computes Richardson number (RiNum) (dimensionless).
# Louis J. Thibodeaux. 1996. Environmental Chemodynamics:
# Movement of Chemicals in Air, Water, and Soil. Wiley.
# 2nd Edition, p 373-375.
#  Typically, -2.0 <= RiNum < 0.2, but for some of
#  the PRZM scenarios RiNum was outside the nominal range.
#  
 RiNum = g_grav / meanT * gradt / gradw**2


# Computes the dimensionless height (zeta). See
# Louis J. Thibodeaux. 1996. Environmental Chemodynamics:
# Movement of Chemicals in Air, Water, and Soil. Wiley.
# 2nd Edition, p 379-381.
if RiNum < (-Fuzzy):zeta = RiNum




