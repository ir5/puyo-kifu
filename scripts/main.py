import argparse

from puyokifu.analyze import detect_whole_play
from puyokifu.media import clip_by_frame


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('videofile', type=str)
    parser.add_argument('--top', type=int, default=0)
    parser.add_argument('--left', type=int, default=0)
    parser.add_argument('--right', type=int, default=-1)
    parser.add_argument('--bottom', type=int, default=-1)
    parser.add_argument('--save_liveness', type=str, default=None)
    args = parser.parse_args()

    # result = detect_whole_play(args)
    result = [(1067, 2816), (2826, 5139), (5150, 6388), (7361, 8041)]
    print(result)

    for i, (begin, end) in enumerate(result):
        clip_by_frame(args.videofile, '{}.mp4'.format(i),
                      begin, end)


if __name__ == '__main__':
    main()
