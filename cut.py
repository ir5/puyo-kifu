import sys

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


in_video, out_video, t1, t2 = sys.argv[1:5]
t1 = float(t1)
t2 = float(t2)
assert in_video != out_video

ffmpeg_extract_subclip(in_video, t1, t2, targetname=out_video)
