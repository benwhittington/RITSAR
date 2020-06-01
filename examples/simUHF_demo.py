##############################################################################
#                                                                            #
#  This is a demonstration of the ritsar toolset using a simple point        #
#  simulator. Algorithms can be switched in and out by commenting/           #
#  uncommenting the lines of code below.                                     #
#                                                                            #
##############################################################################

# Add include directories to default path list
from sys import path

path.append('../')
path.append('./dictionaries')

# Include Dictionaries
from SARplatformUHF import plat_dict

# Include SARIT toolset
from ritsar import phsTools
from ritsar import imgTools

# Create platform dictionary
platform = plat_dict()

# Create image plane dictionary
img_plane = imgTools.img_plane_dict(platform, aspect=1)

# Simulate phase history, if needed
##############################################################################
nsamples = platform['nsamples']
npulses = platform['npulses']
x = img_plane['u'];
y = img_plane['v']
points = [[0, 0, 0],
          [0, -100, 0],
          [200, 0, 0]]
amplitudes = [1, 1, 1]
phs = phsTools.simulate_phs(platform, points, amplitudes)
##############################################################################

# Apply RVP correction
phs_corr = phsTools.RVP_correct(phs, platform)

# Demodulate phase history with constant reference, if needed
phs_fixed = phsTools.phs_to_const_ref(phs_corr, platform, upchirp=1)

# Apply algorithm of choice to phase history data
# img_pf = imgTools.polar_format(phs_corr, platform, img_plane, taylor = 17)
img_wk = imgTools.omega_k(phs_fixed, platform, taylor=17, upsample=2)
# img_bp = imgTools.backprojection(phs_corr, platform, img_plane, taylor = 17, upsample = 2)

# Output image
imgTools.imshow(img_wk, dB_scale=[-25, 0])
