from moviepy.editor import VideoFileClip, ipython_display

video = VideoFileClip('/Users/luca.terrazzan/Documents/workspace/dm-au/videos/test3.mp4')

ipython_display(video)

video.write_videofile("edited.mp4",
                      temp_audiofile="temp-audio.m4a",
                      remove_temp=True,
                      codec="libx264",
                      audio_codec="aac"
                     )
