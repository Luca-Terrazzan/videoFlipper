# Video
from moviepy.editor import VideoFileClip
from moviepy.video.fx.mirror_x import mirror_x
# Audio
import librosa
from librosa.effects import pitch_shift
# Conversion
from pydub import AudioSegment


def start():
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

    # Convert the shifted audio back to .mp3
    librosa.output.write_wav(projectFolder + editedAudioFileName, pitchTest, sr)
    mp3 = AudioSegment.from_wav(projectFolder + editedAudioFileName)
    mp3.export(projectFolder + editedAudioFileName + '.mp3', 'mp3')

    # Save the output
    video.write_videofile(
        projectFolder + editedVideoFileName,
        remove_temp = True,
        audio       = projectFolder + editedAudioFileName + '.mp3'
    )

def mirror(path):
    return mirror_x(VideoFileClip(path))

def saveVideo(video, audio, outputDir):
    """Saves a video file to a chosen directory, applying a certain audio track to it.

    Args:
        video (VideoFileClip): The video to save
        audioPath (string): The path to the desired audio track to apply to the video
        outputDir (string): The output folder
    """

    video.write_videofile(
        outputDir,
        remove_temp = True,
        audio       = audio
    )

def increasePitch(path, fileName, outputDir):
    """Increased a video segment's pitch by one semitone by extracting its audio track and saving it as
    a temporary external file

    Args:
        path (string): The path to the current video file
        fileName (string): The filename for the temporary audio file
        outputDir (string): The output directory
    """

    # Import audio from video
    print('Extracting audio from: ' + path)
    audio, sr = librosa.load(path)
    # Increase its pitch
    increasedPitch = pitch_shift(audio, sr, 1)
    # Save the .wav
    print('Saving audio .wav to: ' + outputDir + fileName)
    librosa.output.write_wav(outputDir + fileName + '.wav', increasedPitch, sr)
    # Convert the .wav to .mp3
    print('Converting to .mp3 from: ' + outputDir + fileName)
    mp3 = AudioSegment.from_wav(outputDir + fileName + '.wav')
    # Save the .mp3
    print('Saving .mp3 to: ' + outputDir + fileName)
    mp3.export(outputDir + fileName + '.mp3', 'mp3')
