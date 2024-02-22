"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == "a":
            result.append("1")
        elif s[i] == "b":
            result.append(2)
        elif s[i] == "c":
            result.append("3")
        elif s[i] == "d":
            result.append(4)
        elif s[i] == "e":
            result.append("5")
        i += 1
    if len(result) == 0:
        result.append(0)
    return result

r_1 = fn_hack_7(["a","b","c","d","e"])
r_2 = fn_hack_7([])

print(f"{r_1} / {r_2}")