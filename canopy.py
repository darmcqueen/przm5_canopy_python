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
 
from tkinter import *
from tkinter import ttk


 
Fuzzy = 0.003
temp_ambient = 20 #celsius
temp_soil_surface = 30 #celsius
wind_speed = 100 # meters/day at top of canopy
wind_speed_soil_surface = 50
canopy_height = 1 #meters
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
root = Tk()


temperature_frame = ttk.Frame(root)
temperature_frame.pack()
temperature_frame.config(height = 50, width = 200)
temperature_frame.config(relief = RIDGE)
ttk.LabelFrame(temperature_frame, height = 20, width = 200, text = 'Temperature').pack()
temperature_frame.config(relief = RIDGE)
temperature_frame.config(padding = (15, 15))

wind_frame = ttk.Frame(root)
wind_frame.pack()
wind_frame.config(height = 50, width = 200)
ttk.LabelFrame(wind_frame, height = 20, width = 200, text = 'Wind Speed').pack()
wind_frame.config(relief = RIDGE)
wind_frame.config(padding = (15, 15))

crop_frame = ttk.Frame(root)
crop_frame.pack()
crop_frame.config(height = 50, width = 200)
ttk.LabelFrame(crop_frame, height = 20, width = 200, text = 'Crop').pack()
crop_frame.config(relief = RIDGE)
crop_frame.config(padding = (15, 15))


soil_surface_temp_value = DoubleVar()
soil_surface_temp_scale = Scale(temperature_frame, orient = HORIZONTAL,
		  length = 400, label = 'Soil Surface', variable = soil_surface_temp_value,
		  from_ = 10, to = 30)
soil_surface_temp_scale.config(variable = soil_surface_temp_value)
soil_surface_temp_scale.pack()
soil_surface_temp_scale.set(19)
soil_surface_temp = (soil_surface_temp_scale.get())
print('Soil Surface temp is {}.'.format(soil_surface_temp ))

ambient_temp_value = DoubleVar()
ambient_temp_scale = Scale(temperature_frame, orient = HORIZONTAL,
		  length = 400, label = 'Top of Canopy ', variable = ambient_temp_value,
		  from_ = 10, to = 30)
ambient_temp_scale.config(variable = ambient_temp_value)
ambient_temp_scale.pack()
ambient_temp_scale.set(22)
ambient_temp = (ambient_temp_scale.get())
print('Ambient temp is {}.'.format(ambient_temp ))


windspeed_surface_value = DoubleVar()
windspeed_surface_scale = Scale(wind_frame, orient = HORIZONTAL,
		  length = 400, label = ' Soil Surface', variable = windspeed_surface_value,
		  from_ = 10, to = 30)
windspeed_surface_scale.config(variable = windspeed_surface_value)
windspeed_surface_scale.pack()
windspeed_surface_scale.set(22)
windspeed_surface = (windspeed_surface_scale.get())
print('Surface windspeed is {}.'.format(windspeed_surface ))

windspeed_canopy_value = DoubleVar()
windspeed_canopy_scale = Scale(wind_frame, orient = HORIZONTAL,
		  length = 400, label = 'Top of Canopy', variable = windspeed_canopy_value,
		  from_ = 10, to = 30)
windspeed_canopy_scale.config(variable = windspeed_canopy_value)
windspeed_canopy_scale.pack()
windspeed_canopy_scale.set(22)
windspeed_canopy = (windspeed_surface_scale.get())
print('Windspeed at Canopy is {}.'.format(windspeed_canopy ))

canopy_height_value = DoubleVar()
canopy_height_scale = Scale(crop_frame, orient = HORIZONTAL,
		  length = 400, label = ' Canopy Height', variable = canopy_height_value,
		  from_ = 10, to = 30)
canopy_height_scale.config(variable = canopy_height_value)
canopy_height_scale.pack()
canopy_height_scale.set(22)
canopy_height = (windspeed_surface_scale.get())
print('Canopy Height is {}.'.format(canopy_height))


root.mainloop()
# soil_surface_temp =Scale(root, orient='horizontal',  label = 'Temp',variable = 10, length = 200, from_=0, to=35).pack()
# 
# ambient_temp = Scale(orient='horizontal', label = 'Ambient Temp', length = 200, from_=0, to=35).pack()
# 
# canopy_height = Scale(orient='horizontal', label = 'Canopy Height', length = 200, from_=10, to=100).pack()
# 
# wind_speed = Scale(orient='horizontal', label = 'Wind Speed', length = 200, from_=0, to=30).pack()
# 
# wind_speed_soil_surface = Scale(orient='horizontal', label = 'Wind Speed Soil Surface', length = 200, from_=0, to=30).pack()


# gradt = (ambient_temp-soil_surface_temp) / canopy_height      # kelvin/meter
# gradw = (wind_speed - wind_speed_soil_surface) / canopy_height      # 1/day
# mean_temp = ((ambient_temp+soil_surface_temp)/2 )+c2k  # mean Temperature, kelvin
# print( g_grav / mean_temp * gradt / gradw**2)



#
# Gradients



# Computes Richardson number (RiNum) (dimensionless).
# Louis J. Thibodeaux. 1996. Environmental Chemodynamics:
# Movement of Chemicals in Air, Water, and Soil. Wiley.
# 2nd Edition, p 373-375.
#  Typically, -2.0 <= RiNum < 0.2, but for some of
#  the PRZM scenarios RiNum was outside the nominal range.
#

 #RiNum = g_grav / meanT * gradt / gradw**2


# Computes the dimensionless height (zeta). See
# Louis J. Thibodeaux. 1996. Environmental Chemodynamics:
# Movement of Chemicals in Air, Water, and Soil. Wiley.
# 2nd Edition, p 379-381.
#if RiNum < (-Fuzzy):zeta = RiNum




