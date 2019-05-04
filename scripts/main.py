import argparse
import cv2

from puyokifu.analyze import detect_whole_play


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('videofile', type=str)
    parser.add_argument('--top', type=int, default=0)
    parser.add_argument('--left', type=int, default=0)
    parser.add_argument('--right', type=int, default=-1)
    parser.add_argument('--bottom', type=int, default=-1)
    parser.add_argument('--save_liveness', type=str, default=None)
    args = parser.parse_args()

    result = [(1007, 2755), (2767, 5079), (5090, 6328), (7301, 8041)]
    # result = detect_whole_play(args)
    for i, (begin, end) in enumerate(result):
        print('# {} / {}'.format(i, len(result)))
        cap = cv2.VideoCapture(args.videofile)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.set(cv2.CAP_PROP_POS_FRAMES, begin)

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        vw = cv2.VideoWriter('{}.mp4'.format(i),
                             fourcc, fps, (width, height))
        for _ in range(end - begin):
            ret, img = cap.read()
            assert ret
            vw.write(img)


if __name__ == '__main__':
    main()
