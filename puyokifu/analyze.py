import itertools
import sys

import cv2


def normalize_image(img_orig, args):
    target_size = (640, 360)
    img = img_orig[args.top:args.bottom, args.left:args.right]  # clip
    img = cv2.resize(img, target_size)

    return img


def detect_field_liveness(img):
    canny = cv2.Canny(img, 100, 500)
    mask = (canny[:-1, :] == 255) * (canny[1:, :] == 255)
    vsum = (mask * 1).sum(axis=0)

    alive1 = (vsum[60:100] >= 180).any() and (vsum[210:250] >= 180).any()
    alive2 = (vsum[530:570] >= 180).any() and (vsum[390:430] >= 180).any()

    return alive1, alive2


def analyze_play_intervals(alives1, alives2):
    # TODO
    return []


def detect_whole_play(args):
    cap = cv2.VideoCapture(args.videofile)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    if args.save_liveness is not None:
        f = open(args.save_liveness, 'w')

    alives1 = []
    alives2 = []
    for i in itertools.count():
        ret, img = cap.read()
        sys.stderr.write(' ' * 80)
        sys.stderr.write('\rframe={}'.format(i))
        sys.stderr.flush()
        if not ret:
            break
        img = normalize_image(img, args)
        a1, a2 = detect_field_liveness(img)
        alives1.append(a1)
        alives2.append(a2)

        if args.save_liveness is not None:
            f.write('{:.2f},{},{}\n'.format(
                i / fps, int(a1), int(a2)))

    return analyze_play_intervals(alives1, alives2)
