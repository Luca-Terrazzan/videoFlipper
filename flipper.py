""" test """
from moviepy.editor import VideoFileClip

VIDEO = VideoFileClip('/Users/luca.terrazzan/Documents/workspace/dm-au/videos/test3.mp4')

VIDEO.write_videofile("myHolidays_edited.mp4",
                      temp_audiofile="temp-audio.m4a",
                      remove_temp=True,
                      codec="libx264",
                      audio_codec="aac"
                     )
