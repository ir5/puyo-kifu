import cv2
from moviepy.editor import VideoFileClip


def get_fps(videoname):
    cap = cv2.VideoCapture(videoname)
    return cap.get(cv2.CAP_PROP_FPS)


def clip_by_frame(in_video, out_video, frame_begin, frame_end):
    fps = get_fps(in_video)
    clip(in_video, out_video, frame_begin / fps, frame_end / fps)


def clip(in_video, out_video, begin, end, verbose=False):
    # begin and end are in seconds
    logger = 'bar' if verbose else None
    video = VideoFileClip(in_video)
    video = video.subclip(begin, end)
    video.write_videofile(out_video, audio=False, verbose=verbose,
                          logger=logger)
