import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Constants
hbar = 1.054571817e-34  # Reduced Planck constant
c = 2.998e8  # Speed of light in vacuum (m/s)

# Wavelength in meters
lambda_IR = 780e-9

# Stable Laser Power in watts
mili_watt = 1e-3

# Constants for conversion
GHz = 1e9
MHz = 1e6

# Pulse frequency in Hz
pulse_freq = 10 * MHz

# detector_deadtime in s 

# corresponds to 66 Mhz
detector_deadtime = 1.5e-8 

freq_deadtime = 1 / detector_deadtime 

# Function to calculate pulse width depending on pulse frequency in Hz
def freq_to_pulse_width(frequency):
    """
    Calculates the segment of lenght depending on the pulse frequency or the deadtime depending frequency of the detector.

    Parameters:
    - frequency: Pulse frequency in Hz.

    Returns:
    - Pulse width in meters.
    """
    return c / frequency

# Function to calculate average photon number per pulse
def avg_photon_number_per_pulse(wavelength, laser_power, pulse_frequency):
    """
    Calculates the average photon number per pulse.

    Parameters:
    - wavelength: Wavelength in meters.
    - laser_power: Laser power in watts.
    - pulse_frequency: Pulse frequency in Hz.

    Returns:
    - Average photon number per pulse.
    """
    # Photon energy
    e_phot = hbar * 2 * np.pi * (c / wavelength)
    # Photon flux
    phot_flux = laser_power / e_phot
    # Average photon number per pulse
    avg_photon_number = phot_flux * freq_to_pulse_width(pulse_frequency) / c

    return avg_photon_number


# Function to calculate Optical Density (OD) factor for Single Photon Source (SPS)
def OD_factor_for_SPS(mean_photon_number_per_pulse, avg_phot_demand):
    """
    Calculates the Optical Density (OD) factor for Single Photon Source (SPS).

    Parameters:
    - mean_photon_number_per_pulse: Mean photon number per pulse.
    - avg_phot_demand: Average photon demand.

    Returns:
    - Optical Density (OD) factor for Single Photon Source (SPS).
    """
    return -np.log10(avg_phot_demand / mean_photon_number_per_pulse)

# Calculate average photon number per pulse and print result
avg_photon_number = avg_photon_number_per_pulse(lambda_IR, mili_watt, freq_deadtime)
pulse_width = freq_to_pulse_width(freq_deadtime)
print(f"There are {avg_photon_number} Photons per pulse with a length of {freq_deadtime} m at a frequency of {freq_deadtime} Hz")

# Calculate OD factor for SPS and print result
od_factor = OD_factor_for_SPS(avg_photon_number, 1e-2)
print(f"OD Factor for faint (fake) Single Photon Source (SPS) (attenuated Laser): {round(od_factor, 3)}")

# Calculating damping factors for fixed Power and fixed pulse width
power_arr = mili_watt * np.linspace(1, 50, 50)
pulsing_freq_arr = np.linspace(1, 50, 50) * GHz

# Plotting OD factor against average photon number per pulse for fixed pulse width
fig, ax = plt.subplots()
avg_phot_numb_per_pulse = avg_photon_number_per_pulse(lambda_IR, power_arr, freq_deadtime)
OD_for_SPS = OD_factor_for_SPS(avg_photon_number_per_pulse(lambda_IR, power_arr, freq_deadtime), 1e-2)
ax.plot(avg_phot_numb_per_pulse, OD_for_SPS)
ax.set(ylabel='OD', xlabel='Average Photon Number per Pulse',
       title=f'OD to $10^{-2}$ photons per pulse for fixed pulse width {round(pulse_width, 3)} m')
ax.grid()

plt.savefig(f"HQO_20240503_Pow_depending_OD_at_{freq_deadtime}Hz.png")
plt.show()



# def laser_power(x):
#     # Photon energy
#     e_phot = hbar * 2 * np.pi * (c / lambda_IR)
#     # Average photon number per pulse
#     return x*c/freq_to_pulse_width(10 * GHz) * e_phot 


# def laser_power_inverse(x):
#     # Photon energy
#     e_phot = hbar * 2 * np.pi * (c / lambda_IR)
#     # Average photon number per pulse
#     return (x*c/freq_to_pulse_width(10 * GHz) * e_phot)**(-1)

# secax = ax.secondary_xaxis('top', functions=(laser_power,laser_power_inverse))
# secax.set_xlabel('Laser_power [W]')


# Data for a three-dimensional line

# X, Y = np.meshgrid(power_arr, pulsing_freq_arr)
# Z = OD_factor_for_SPS(avg_photon_number_per_pulse(lambda_IR, X, Y), 1e-2)

# fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

# fig.update_layout(title='OD Factor', autosize=False,
#                   width=500, height=500,
#                   margin=dict(l=65, r=50, b=65, t=90))

# fig.update_layout(scene = dict(
#                     yaxis_title= f'Avg. Photon number per Pulse',
#                     xaxis_title='Pulse width [m]',
#                     zaxis_title='OD'),
#                     width=700,
#                     margin=dict(r=20, b=10, l=10, t=10))


# fig.show()