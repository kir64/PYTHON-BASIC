"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""

def remove_duplicated_words(line):
    word_lst, ans = line.split(), []
    for word in word_lst:
        if word not in ans:
            ans.append(word)
    return ' '.join(ans)


print(remove_duplicated_words('1 2 3'))  #'1 2 3'
print(remove_duplicated_words('cat cat cat'))  #'cat'
print(remove_duplicated_words('cat cat dog 1 dog 2'))  #'cat dog 1 2'
