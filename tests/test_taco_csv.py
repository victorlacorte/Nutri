import csv
import pytest

from nutri.taco_meta import TacoHeader

@pytest.fixture(scope='module')
def taco():
    return 'nutri/data/Taco_4a_edicao_2011.csv'

def test_read(taco):
    with open(taco, 'r') as f:
        reader = csv.DictReader(
                    f,
                    fieldnames=TacoHeader._fields,
                    dialect='excel')
        # Skip the header
        next(reader)
        for i, row in enumerate(reader):
            if i > 2:
                break
            print(row)
    assert False
