import sys

# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip


in_video, out_video, t1, t2 = sys.argv[1:5]
t1 = float(t1)
t2 = float(t2)
assert in_video != out_video

video = VideoFileClip(in_video)
video = video.subclip(t1, t2)
video.write_videofile(out_video, audio=False)
