from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Bob", "Ross") == "Ross; Bob"
    assert make_full_name("Adam","James-Smith") == "James-Smith; Adam"
    assert make_full_name("Rd", "R") == "R; Rd"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Ross; Bob") == "Ross"
    assert extract_family_name("James-Smith; Adam") == "James-Smith"
    assert extract_family_name("Rd; R") == "Rd"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Ross; Bob") == "Bob"
    assert extract_given_name("James-Smith; Adam") == "Adam"
    assert extract_given_name("Rd; R") == "R"
    assert extract_given_name("; ") == ""





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
