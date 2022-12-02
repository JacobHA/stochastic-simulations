# Stitch together the images in the figures directory
# to make a movie (gif).

import os
import imageio

# Get the list of files in the figures directory
files = os.listdir('./figures')
# Order them by delta
files.sort(key=lambda x: float(x[6:-4]))

# Make a gif from the images using imageio
images = []
for file in files:
    images.append(imageio.imread(f'./figures/{file}'))
imageio.mimsave('./figures/movie.gif', images, duration=0.1)
