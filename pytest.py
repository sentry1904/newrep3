import pytest
import numpy as np
import py2  # import your script

def test_ascii_bar_chart_output(capsys):
    labels = ["A", "B"]
    values = [10, 20]
    py2.ascii_bar_chart(values, labels)
    captured = capsys.readouterr()
    # Check that both labels appear in the output
    assert "A" in captured.out
    assert "B" in captured.out
    # Check that values are shown
    assert "(10)" in captured.out
    assert "(20)" in captured.out

def test_random_values_generation():
    labels = ["Task A", "Task B", "Task C", "Task D"]
    values = np.random.randint(5, 100, size=len(labels))
    assert len(values) == len(labels)
    assert all(5 <= v < 100 for v in values)

