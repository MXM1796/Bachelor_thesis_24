import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

data = np.loadtxt("HQO_04062024_SNSPD_DCR_Cap_on.txt", skiprows=16, usecols=range(9,16))
channel = 4

plt.plot(np.linspace(0,40,len(data[:,channel])), data[:,channel])
plt.yscale("log")
plt.xlim(left=13, right=23)
plt.title(f'Dark count rate (DCR) - Channel {channel} - cap on ')
plt.ylabel('Dark count rate (log) [Hz]')
plt.xlabel('Bias current [uA]')
#plt.legend()
#plt.savefig(f"HQO_20240506_DCR_Channel_{channel}_cap_on.png")
plt.show()







