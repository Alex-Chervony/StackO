# https://stackoverflow.com/questions/44191045/match-replace-within-multiple-quoted-strings-with-regex/44191111#44191111
require(stringi)
s = "The 'quick  brown' fox 'jumps over' the lazy dog"
stri_replace_all(s, regex="('[a-z]+) +([a-z]+')", '$1_$2')