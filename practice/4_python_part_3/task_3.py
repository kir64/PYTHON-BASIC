"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain):
    return re.match(r'\bhttp[s]?://*[/]?', domain) is not None


print(is_http_domain('http://wikipedia.org'))
# True
print(is_http_domain('https://ru.wikipedia.org/'))
# True
print(is_http_domain('griddynamics.com'))
# False


"""
write tests for is_http_domain function
"""

def test_is_http_domain_1(capfd):
    print(is_http_domain('http://wikipedia.org'))
    out, err = capfd.readouterr()
    assert out == 'True\n'


def test_is_http_domain_2(capfd):
    print(is_http_domain('griddynamics.com'))
    out, err = capfd.readouterr()
    assert out == 'False\n'
