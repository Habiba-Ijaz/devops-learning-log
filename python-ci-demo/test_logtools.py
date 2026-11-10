from logtools import count_errors


def test_counts_errors():
    lines = ["INFO: ok", "ERROR: bad", "ERROR: worse"]
    assert count_errors(lines) == 3


def test_no_errors():
    assert count_errors(["INFO: ok"]) == 0
