from logtools import count_errors


def test_counts_errors():
    assert count_errors(["INFO: ok", "ERROR: bad", "ERROR: worse"]) == 3


def test_no_errors():
    assert count_errors(["INFO: ok"]) == 0
