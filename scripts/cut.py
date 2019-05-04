import sys

from puyokifu.media import clip


in_video, out_video, t1, t2 = sys.argv[1:5]
t1 = float(t1)
t2 = float(t2)
assert in_video != out_video

clip(in_video, out_video, t1, t2)
