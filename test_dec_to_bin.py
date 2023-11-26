import main

def test_dec_to_bin():
    input = 10
    expected = 1010
    actual = main.dec_to_bin(input)
    assert (expected == actual)