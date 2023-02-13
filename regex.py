import re

regex_expression    = r'[A-F0-9][A-F0-9]\:[A-F0-9][A-F0-9]\:[A-F0-9][A-F0-9]\:[A-F0-9][A-F0-9]\:[A-F0-9][A-F0-9]\:[A-F0-9][A-F0-9]\:[A-F0-9][A-F0-9]\:[A-F0-9][A-F0-9]'
regex_expression2   = r'[A-F0-9]{12}'
regex_expression3   = r'([A-F0-9][A-F0-9][\:|\-?]){6}'
regex_expression4   = r'([0-9a-f]{2}(?::[0-9a-f]{2}){5})|([0-9a-f]{2}(?:\-[0-9a-f]{2}){5})'
regex_expression5   = r'(?:(?:[A-F0-9]{2}[:|-]){5})[A-F0-9]{2}'

def search(digitado):
    compiled_expression = re.compile(regex_expression5)
    results = re.findall(compiled_expression, digitado, )
    return results

