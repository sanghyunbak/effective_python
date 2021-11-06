from datetime import datetime
from unittest.mock import Mock

from com.shbak.effective_python._01_example._78_mock_complex_dependency.main import get_animals

def get_mock():
    mock = Mock(spec=get_animals)
    expected = [
        ('Spot', datetime(2019, 6, 5, 11, 15)),
        ('Fluffy', datetime(2019, 6, 5, 12, 30)),
        ('Jojo', datetime(2019, 6, 5, 12, 45)),
    ]

    # mock return_value that value when call mock function
    mock.return_value = expected
    return mock
