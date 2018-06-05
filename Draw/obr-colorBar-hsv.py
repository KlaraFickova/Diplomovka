import numpy as np
from scipy import special as bessel # we will use only bessel functions
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.colors import hsv_to_rgb

plotName = "colorBar-hsv"

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['axes.labelsize'] = 'large'


fig, ax = plt.subplots(figsize = (7,0.4))

cmap = mpl.cm.hsv
norm = mpl.colors.Normalize(vmin=0, vmax=1)

cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                norm=norm,
                                orientation='horizontal')
cb1.set_label('f')

plt.savefig("./TeXy/images/"+plotName+".pdf", bbox_inches='tight')
