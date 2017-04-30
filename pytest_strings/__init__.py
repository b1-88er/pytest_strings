import pytest
from pytest_strings import strings

@pytest.fixture(params=strings.noughty_string())
def noughty_string(request):
    return request.param

@pytest.fixture(params=strings.types['number'])
def number_string(request):
    return request.param

@pytest.fixture(params=strings.types['null'])
def null_strings(request):
    return request.param

@pytest.fixture(params=strings.types['escape'])
def escape_string(request):
    return request.param

@pytest.fixture(params=strings.types['truth'])
def truth_string(request):
    return request.param

@pytest.fixture(params=strings.types['false'])
def false_string(request):
    return request.param

@pytest.fixture(params=strings.types['truth'] + strings.types['false'])
def bool_string(request):
    return request.param

@pytest.fixture(params=strings.types['emoji'])
def emoji_string(request):
    return request.param

@pytest.fixture(params=strings.types['asian'])
def asian_string(request):
    return request.param

@pytest.fixture(params=strings.types['arabic'])
def arabic_string(request):
    return request.param

@pytest.fixture(params=strings.types['arabic'] + strings.types['asian'])
def nonlatin_string(request):
    return request.param

@pytest.fixture(params=strings.types['xss'])
def xss_string(request):
    return request.param

@pytest.fixture(params=strings.types['eval_injection'])
def eval_injection_string(request):
    return request.param

@pytest.fixture(params=strings.types['sql_injection'])
def sql_injection_string(request):
    return request.param

@pytest.fixture(params=strings.types['simple_ascii'])
def simple_ascii_string(request):
    return request.param

@pytest.fixture(params=strings.types['html'])
def html_string(request):
    return request.param

@pytest.fixture(params=strings.types['utf'])
def utf_string(request):
    return request.param
