import argparse
import sys

import cv2


def detect_field_liveness(canny):
    mask = (canny[:-1, :] == 255) * (canny[1:, :] == 255)
    vsum = (mask * 1).sum(axis=0)

    alive1 = (vsum[60:100] >= 180).any() and (vsum[210:250] >= 180).any()
    alive2 = (vsum[530:570] >= 180).any() and (vsum[390:430] >= 180).any()

    return alive1, alive2


def process(args):
    cap = cv2.VideoCapture(args.videofile)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # cap.set(cv2.CAP_PROP_POS_FRAMES, 30 * 300)
    f = open('alive.csv', 'w')

    for i in range(1000000000):
        ret, img = cap.read()
        sys.stdout.write('\r{}'.format(i))
        sys.stdout.write(' ' * 80)
        sys.stdout.flush()
        if not ret:
            break
        target_size = (640, 360)
        img = img[args.top:args.bottom, args.left:args.right]  # clip
        img = cv2.resize(img, target_size)

        # canny
        canny = cv2.Canny(img, 100, 500)
        alive1, alive2 = detect_field_liveness(canny)
        f.write('{:.2f},{},{}\n'.format(i / fps, int(alive1), int(alive2)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('videofile', type=str)
    parser.add_argument('--top', type=int, default=0)
    parser.add_argument('--left', type=int, default=0)
    parser.add_argument('--right', type=int, default=-1)
    parser.add_argument('--bottom', type=int, default=-1)
    args = parser.parse_args()

    process(args)


if __name__ == '__main__':
    main()
