"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""

def build_from_unique_words(*lines, word_number):
    ans = []
    for line in lines:
        tmp = sorted(set(line.split()))
        if word_number < len(tmp):
            ans.append(tmp[word_number])
    return ' '.join(ans)


print(build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1))  # 'b 2 dog'
print(build_from_unique_words('a b c', '', 'cat dog milk', word_number=0))  # 'a cat'
print(build_from_unique_words('1 2', '1 2 3', word_number=10))  # ''
print(build_from_unique_words(word_number=10))  # ''
