import re

PATTERN = re.compile(r'')

tests = [(False, " 0" ),
        (False, "abc"),
        (True,  "000"),
        (True,  "110"),
        (False, "111"),
        (True,  "{:b}".format(12345678)),
       ]

for exp,s in tests:
    print(bool(PATTERN.match(s)))
    print(PATTERN.match(s))
    print(exp)