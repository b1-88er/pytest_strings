from pytest_strings import strings

all_cases = [i for i in strings.noughty_string()]
def test_noughty_string(noughty_string):
    assert noughty_string in all_cases

def test_arabic(arabic_string):
    assert arabic_string in strings.types['arabic']

def test_asian(asian_string):
    assert asian_string in strings.types['asian']

def test_emoji(emoji_string):
    assert emoji_string in strings.types['emoji']

def test_escape(escape_string):
    assert escape_string in strings.types['escape']

def test_eval_injenction(eval_injection_string):
    assert eval_injection_string in strings.types['eval_injection']

def test_false(false_string):
    assert false_string in strings.types['false']

def test_truth(truth_string):
    assert truth_string in strings.types['truth']

def test_html(html_string):
    assert html_string in strings.types['html']

def test_simple_ascii(simple_ascii_string):
    assert simple_ascii_string in strings.types['simple_ascii']

def test_sql_injection(sql_injection_string):
    assert sql_injection_string in strings.types['sql_injection']

def test_utf(utf_string):
    assert utf_string in strings.types['utf']

def test_xss(xss_string):
    assert xss_string in strings.types['xss']

def test_bool_string(bool_string):
    assert bool_string in strings.types['truth'] + strings.types['false']

def test_nonlatin(nonlatin_string):
    assert nonlatin_string in strings.types['asian'] + strings.types['arabic']
