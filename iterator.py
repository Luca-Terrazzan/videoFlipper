import sys
sys.path.append('./src')

import os
from flipper import mirror
from flipper import saveVideo

root = './videos/original/'
done = './videos/done/'
edited = './videos/edited/'

# Iterates videos to convert
print('Looking for video files...')
for filename in os.listdir(root):
    # If it actually is a video
    if filename.endswith('.mp4'):
        print('Video found: ' + filename)
        print('Mirroring...')

        # Mirror the video
        video = mirror(root + '/' + filename)

        # Save the video
        saveVideo(video, edited + '/' + filename)

        # Move the original video to the done videos directory
        os.rename(root + '/' + filename, done + '/' + filename)

