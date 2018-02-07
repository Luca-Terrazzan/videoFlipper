# Video
from moviepy.editor import VideoFileClip
from moviepy.video.fx.mirror_x import mirror_x
# Audio
import librosa
from librosa.effects import pitch_shift
# Conversion
from pydub import AudioSegment

projectFolder = '/Users/luca.terrazzan/Documents/workspace/videoFlipper/'
videoFolder = 'videos/original/'
editedAudioFileName = 'audiotrack.wav'
editedVideoFileName = 'videotrack.mp4'

# Mirror the video
video = VideoFileClip(projectFolder + videoFolder + 'test.mp4')
video = mirror_x(video)

# Shift the pitch up a semitone
audio, sr = librosa.load(projectFolder + videoFolder + 'test.mp4')
pitchTest = pitch_shift(audio, sr, 1)
librosa.output.write_wav(projectFolder + editedAudioFileName, pitchTest, sr)

# Convert the shifted audio back to .mp3
mp3 = AudioSegment.from_wav(projectFolder + editedAudioFileName)
mp3.export(projectFolder + editedAudioFileName + '.mp3', 'mp3')

# Save the output
video.write_videofile(
    projectFolder + editedVideoFileName,
    remove_temp = True,
    audio       = projectFolder + editedAudioFileName + '.mp3'
)
