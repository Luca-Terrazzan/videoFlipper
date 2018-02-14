import os
# from flipper import mirror
from flipper import mirror
from flipper import saveVideo

root = './videos/original/'
done = './videos/done/'
edited = './videos/edited/'

# Iterates over a directory files
print('Looking for video files...')
for filename in os.listdir(root):
    if filename.endswith('.mp4'):
        print('Video found: ' + filename)
        print('Mirroring...')
        video = mirror(root + '/' + filename)
        saveVideo(video, edited + '/' + filename)
        os.rename(root + '/' + filename, done + '/' + filename)

