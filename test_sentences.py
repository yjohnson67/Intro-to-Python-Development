import pytest
from sentences import get_determiner, get_noun, get_verb, get_preposition

def test_get_determiner():
    for i in range(10):
        determiner = get_determiner(1)
        assert determiner in ["a", "one", "the"]
    for i in range(10):
        determiner = get_determiner(2)
        assert determiner in ["some", "many", "the"]

def test_get_noun():
    for i in range(10):
        noun = get_noun(1)
        assert noun in ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    for i in range(10):
        noun = get_noun(2)
        assert noun in ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

def test_get_verb():
    for i in range(10):
        verb = get_verb(0, "present")
        assert verb in ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for i in range(10):
        verb = get_verb(1, "present")
        assert verb in ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for i in range(10):
        verb = get_verb(0, "past")
        assert verb in ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for i in range(10):
        verb = get_verb(1, "future")
        assert verb in ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

def test_get_preposition():
    for i in range(10):
        preposition = get_preposition()
        assert preposition in ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

def test_get_preposition_phrase():
    for i in range(10):
        preposition = get_preposition()
        assert preposition in ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without", "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women", "a", "one", "the", "some", "many", "the"]

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])