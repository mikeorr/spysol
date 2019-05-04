import math
import random
import sys

import pytest

isclose = pytest.mark.skipif(sys.version_info < (3, 5),
    reason="Requires Python >= 3.5 for 'math.isclose()'.")

@isclose
def test_random_reproducible():
    r = random.Random(2)
    assert math.isclose(r.random(), 0.9560342718892494)
    assert math.isclose(r.random(), 0.9478274870593494)
    assert math.isclose(r.random(), 0.05655136772680869)
