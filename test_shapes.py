import math
import pytest
from shapes import calculate_rectangle_area, calculate_triangle_area, calculate_circle_area, calculate_area, get_dimensions
from pytest import MonkeyPatch

def test_calculate_rectangle_area():
    assert calculate_rectangle_area(5, 10) == 50
    assert calculate_rectangle_area(3.5, 4) == 14

def test_calculate_triangle_area():
    assert calculate_triangle_area(3, 5) == 7.5
    assert calculate_triangle_area(4, 8) == 16

def test_calculate_circle_area():
    assert abs(calculate_circle_area(5) - 78.54) < 0.01
    assert abs(calculate_circle_area(2.5) - 19.63) < 0.01

def test_calculate_area():
    assert calculate_area("rectangle", [5, 10]) == 50
    assert calculate_area("triangle", [3, 5]) == 7.5
    assert abs(calculate_area("circle", [5]) - 78.54) < 0.01

def test_get_dimensions_rectangle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_dimensions("rectangle") == [5, 5]

def test_get_dimensions_triangle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_dimensions("triangle") == [5, 5]

def test_get_dimensions_circle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_dimensions("circle") == [5]

import math
import pytest
from shapes import calculate_rectangle_area, calculate_triangle_area, calculate_circle_area, calculate_area, get_dimensions

def test_calculate_rectangle_area():
    assert calculate_rectangle_area(5, 10) == 50
    assert calculate_rectangle_area(3.5, 4) == 14

def test_calculate_triangle_area():
    assert calculate_triangle_area(3, 5) == 7.5
    assert calculate_triangle_area(4, 8) == 16

def test_calculate_circle_area():
    assert abs(calculate_circle_area(5) - 78.54) < 0.01
    assert abs(calculate_circle_area(2.5) - 19.63) < 0.01

def test_calculate_area():
    assert calculate_area("rectangle", [5, 10]) == 50
    assert calculate_area("triangle", [3, 5]) == 7.5
    assert abs(calculate_area("circle", [5]) - 78.54) < 0.01

def test_get_dimensions_rectangle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_dimensions("rectangle") == [5, 5]

def test_get_dimensions_triangle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_dimensions("triangle") == [5, 5]

def test_get_dimensions_circle(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert get_dimensions("circle") == [5]

pytest.main(["-v", "--tb=line", "-rN", __file__])