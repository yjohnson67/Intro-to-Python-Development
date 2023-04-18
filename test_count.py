import word_counter

def test_read_file():
    assert word_counter.read_file('sample_text_file.txt') == "This is a sample text file.\nIt contains several lines of text.\n"

def test_split_into_words():
    contents = "This is a sample text file.\nIt contains several lines of text.\n"
    expected_words = ['this', 'is', 'a', 'sample', 'text', 'file', 'it', 'contains', 'several', 'lines', 'of', 'text']
    assert word_counter.split_into_words(contents) == expected_words

def test_count_words():
    words = ['this', 'is', 'a', 'sample', 'text', 'file', 'it', 'contains', 'several', 'lines', 'of', 'text']
    expected_counts = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 2, 'file': 1, 'it': 1, 'contains': 1, 'several': 1, 'lines': 1, 'of': 1}
    assert word_counter.count_words(words) == expected_counts

def test_display_word_counts(capfd):
    word_counts = {'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 2, 'file': 1, 'it': 1, 'contains': 1, 'several': 1, 'lines': 1, 'of': 1}
    word_counter.display_word_counts(word_counts)
    out, err = capfd.readouterr()
    assert out == "this: 1\nis: 1\na: 1\nsample: 1\ntext: 2\nfile: 1\nit: 1\ncontains: 1\nseveral: 1\nlines: 1\nof: 1\n"