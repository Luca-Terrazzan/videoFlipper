from moviepy.editor import VideoFileClip
from moviepy.video.fx.mirror_x import mirror_x

video = VideoFileClip('/Users/luca.terrazzan/Documents/workspace/videoFlipper/videos/original/test.mp4')

video = mirror_x(video)

video.write_videofile("edited.mp4",
                      temp_audiofile="temp-audio.m4a",
                      remove_temp=True,
                      codec="libx264",
                      audio_codec="aac",
                      audio_bitrate='50k'
                     )
