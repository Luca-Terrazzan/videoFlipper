import os
import glob
import sys
sys.path.append('./src')

from flipper import mirror
from flipper import saveVideo
from flipper import increasePitch

original = './videos/original/'
done = './videos/done/'
edited = './videos/edited/'

# Iterates videos to convert
print('Looking for video files...')
for filename in os.listdir(original):
    # If it actually is a video
    if filename.endswith('.mp4'):
        print('Video found: ' + filename)
        print('Mirroring...')

        # Mirror the video
        video = mirror(original + filename)

        # Increase the pitch
        print('Processing audio of ' + filename + '...')
        increasePitch(original + filename, filename, edited)
        print('Processing audio of ' + filename + ' done!')

        # Save the video in the `edited` videos directory
        print('Saving the final resutl to the `edited` folder')
        saveVideo(video, edited + filename + '.mp3', edited + filename)

        # Move the original video to the `done` videos directory
        print('Moving the processed file to the `done` folder...')
        os.rename(original + '/' + filename, done + '/' + filename)

# Delete leftovers
print('Deleting leftover files...')
mp3Leftovers = glob.glob(edited + '*.mp3')
for mp3 in mp3Leftovers:
    os.remove(mp3)
wavLeftovers = glob.glob(edited + '*.wav')
for wav in wavLeftovers:
    os.remove(wav)
