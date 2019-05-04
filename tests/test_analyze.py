import csv

from puyokifu.analyze import analyze_play_intervals


def test_analyze_play_intervals():
    reader = csv.reader(open('tests/alive_test.csv', 'r'))
    alives1 = []
    alives2 = []
    for row in reader:
        alives1.append(int(row[1]))
        alives2.append(int(row[2]))

    result = analyze_play_intervals(alives1, alives2)

    assert result == [(1007, 2755), (2767, 3241)]
