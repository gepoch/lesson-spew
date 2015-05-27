"""
"""
from random import choice

george_key_groups=[
    "aAqQzZ",
    "sSwWxX`~1!2@",
    "cCdDeE3#",
    "vVfFrRtTgGbB4$5%6^",
    "nNhHyY7&uUjJmM7&",
    ",<kKiI8*9(",
    ".>lLoO0)-_=+",
    "/?;:pP'\"[{]}",
]



def main(groups):
    out = ""
    for i in xrange(1000):
        group = choice(groups)
        out += ''.join(choice(group) for i in xrange(10))
        out += ' '
    print(out)

if __name__ == "__main__":
    main(george_key_groups)
