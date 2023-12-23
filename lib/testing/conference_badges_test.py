# lib/testing/conference_badges_test.py

from conference_badges import batch_badge_creator

def test_batch_badge_creator():
    '''Test batch_badge_creator function.'''
    names = ["Guido van Rossum", "John Doe", "Jane Doe"]
    expected_badges = [
        "Hello, my name is Guido van Rossum.",
        "Hello, my name is John Doe.",
        "Hello, my name is Jane Doe."
    ]
    assert batch_badge_creator(names) == expected_badges
