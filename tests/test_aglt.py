import copy

from krnnt.aglt import rewrite_praet, remove_aglt, rule1, rule3, rule1b

paragraph = [
    [
        {'token': 'Zrobił', 'sep': 'newline', 'tag': 'praet:sg:m1:perf',
         'lemmas': ['zrobić'], 'start': 0, 'end': 6},
        {'token': 'by', 'sep': 'none', 'tag': 'qub', 'lemmas': ['by'],
         'start': 6, 'end': 8},
        {'token': 'm', 'sep': 'none', 'tag': 'aglt:sg:pri:imperf:nwok',
         'lemmas': ['być'], 'start': 8, 'end': 9},
        {'token': 'to', 'sep': 'space', 'tag': 'subst:sg:acc:n',
         'lemmas': ['to'], 'start': 10, 'end': 12},
        {'token': '.', 'sep': 'none', 'prob': 1.0, 'tag': 'interp', 'lemmas': ['.'],
         'start': 12, 'end': 13}
    ],
    [
        {'token': 'Czy', 'sep': 'space', 'tag': 'qub', 'lemmas': ['czy'],
         'start': 14, 'end': 17},
        {'token': 'by', 'sep': 'space', 'tag': 'qub', 'lemmas': ['by'],
         'start': 18, 'end': 20},
        {'token': 'm', 'sep': 'none', 'tag': 'aglt:sg:pri:imperf:nwok',
         'lemmas': ['być'], 'start': 20, 'end': 21},
        {'token': 'to', 'sep': 'space', 'tag': 'subst:sg:acc:n',
         'lemmas': ['to'], 'start': 22, 'end': 24},
        {'token': 'zrobił', 'sep': 'space', 'tag': 'praet:sg:m1:perf',
         'lemmas': ['zrobić'], 'start': 25, 'end': 31},
        {'token': '?', 'sep': 'none', 'tag': 'interp', 'lemmas': ['?'],
         'start': 31, 'end': 32}
    ],
    [
        {'token': 'Zrobił', 'sep': 'space', 'tag': 'praet:sg:m1:perf',
         'lemmas': ['zrobić'], 'start': 33, 'end': 39},
        {'token': 'em', 'sep': 'none', 'tag': 'aglt:sg:pri:imperf:wok',
         'lemmas': ['być'], 'start': 39, 'end': 41},
        {'token': 'to', 'sep': 'space', 'tag': 'subst:sg:acc:n',
         'lemmas': ['to'], 'start': 42, 'end': 44},
        {'token': '.', 'sep': 'none', 'prob': 1.0, 'tag': 'interp', 'lemmas': ['.'],
         'start': 44, 'end': 45}
    ],
    [
        {'token': 'Aby', 'sep': 'space', 'tag': 'comp', 'lemmas': ['aby'],
         'start': 46, 'end': 49},
        {'token': 'm', 'sep': 'none', 'tag': 'aglt:sg:pri:imperf:nwok',
         'lemmas': ['być'], 'start': 49, 'end': 50},
        {'token': 'to', 'sep': 'space', 'tag': 'subst:sg:acc:n',
         'lemmas': ['to'], 'start': 51, 'end': 53},
        {'token': 'zrobił', 'sep': 'space', 'tag': 'praet:sg:m1:perf',
         'lemmas': ['zrobić'], 'start': 54, 'end': 60},
        {'token': '?', 'sep': 'none', 'tag': 'interp', 'lemmas': ['?'],
         'start': 60, 'end': 61}
    ],
    [
        {'token': 'Zrobił', 'sep': 'newline', 'tag': 'praet:sg:m1:perf',
         'lemmas': ['zrobić'], 'start': 0, 'end': 6},
        {'token': 'by', 'sep': 'none', 'tag': 'qub', 'lemmas': ['by'],
         'start': 6, 'end': 8},
        {'token': 'to', 'sep': 'space', 'tag': 'subst:sg:acc:n',
         'lemmas': ['to'], 'start': 9, 'end': 11},
        {'token': '.', 'sep': 'none', 'prob': 1.0, 'tag': 'interp', 'lemmas': ['.'],
         'start': 11, 'end': 12}
    ],
[
        {'token': 'Czy', 'sep': 'space', 'tag': 'qub', 'lemmas': ['czy'],
         'start': 14, 'end': 17},
        {'token': 'by', 'sep': 'space', 'tag': 'qub', 'lemmas': ['by'],
         'start': 18, 'end': 20},
        {'token': 'to', 'sep': 'space', 'tag': 'subst:sg:acc:n',
         'lemmas': ['to'], 'start': 21, 'end': 23},
        {'token': 'zrobił', 'sep': 'space', 'tag': 'praet:sg:m1:perf',
         'lemmas': ['zrobić'], 'start': 24, 'end': 30},
        {'token': '?', 'sep': 'none', 'tag': 'interp', 'lemmas': ['?'],
         'start': 30, 'end': 31}
    ]
]


def test_rewrite_praet():
    sentence1 = copy.deepcopy(paragraph[2])

    rewrite_praet(sentence1[1], sentence1[0])
    assert sentence1[0]['tag'] == 'praet:sg:m1:pri:perf'


def test_rewrite_cond():
    sentence1 = copy.deepcopy(paragraph[0])
    rewrite_praet(sentence1[2], sentence1[0], sentence1[1])
    assert sentence1[0]['tag'] == 'cond:sg:m1:pri:perf'

def test_rewrite_cond2():
    sentence1 = copy.deepcopy(paragraph[4])
    rewrite_praet(None, sentence1[0], sentence1[1])
    assert sentence1[0]['tag'] == 'cond:sg:m1:ter:perf'

def test_rule1_cond():
    sentence1 = copy.deepcopy(paragraph[0])

    remove_aglt(sentence1, [rule1])
    print(sentence1)
    assert sentence1[0]['tag'] == 'cond:sg:m1:pri:perf'
    assert sentence1[1]['token'] != 'by'
    assert sentence1[2]['token'] != 'm'
    assert sentence1[0]['token'] == 'Zrobiłbym'
    assert sentence1[0]['end'] == 9


def test_rule1_praet():
    sentence1 = copy.deepcopy(paragraph[2])

    remove_aglt(sentence1, [rule1])
    print(sentence1)
    assert sentence1[0]['tag'] == 'praet:sg:m1:pri:perf'
    assert sentence1[1]['token'] != 'm'
    assert sentence1[0]['token'] == 'Zrobiłem'
    assert sentence1[0]['end'] == 41

def test_rule3_1():
    sentence1 = copy.deepcopy(paragraph[1])

    print(sentence1)
    remove_aglt(sentence1, [rule1, rule3])
    print(sentence1)
    assert sentence1[3]['tag'] == 'cond:sg:m1:pri:perf'
    assert sentence1[1]['token'] == 'bym'
    assert sentence1[1]['end'] == 21

def test_rule3_2():
    sentence1 = copy.deepcopy(paragraph[3])

    remove_aglt(sentence1, [rule1, rule3])
    print(sentence1)
    assert sentence1[2]['tag'] == 'praet:sg:m1:pri:perf'
    assert sentence1[0]['token'] == 'Abym'
    assert sentence1[0]['end'] == 50

def test_rule3_3():
    sentence1 = copy.deepcopy(paragraph[4])

    remove_aglt(sentence1, [rule1b, rule3])
    print(sentence1)
    assert sentence1[0]['tag'] == 'cond:sg:m1:ter:perf'
    assert sentence1[0]['token'] == 'Zrobiłby'
    assert sentence1[0]['end'] == 8
    assert sentence1[1]['token'] != 'by'

def test_rule3_4():
    sentence1 = copy.deepcopy(paragraph[5])

    remove_aglt(sentence1, [rule1b, rule3])
    print(sentence1)
    assert sentence1[3]['tag'] == 'cond:sg:m1:ter:perf'
    assert sentence1[3]['token'] == 'zrobił'
