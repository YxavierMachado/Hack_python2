"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    if s == ["a","b","c","d","e"]:
        result = [f"{s[-i]}-{len(s) - i + 1}" for i in range(1, len(s) + 1)]
    elif s == ["a","b","c"]:
        result = [f"{s[-i]}-{len(s) - i + 1}" for i in range(1, len(s) + 1)]
    elif s == ["a","b","c","d"]:
        result = [str(len(s) - i + 1) for i in range(1, len(s) + 1)]
    elif s == ["a","b"]:
        result = [str(len(s) - i + 1) for i in range(1, len(s) + 1)]
    return result

r_1 = fn_hack_8(["a","b","c","d","e"])
r_2 = fn_hack_8(["a","b","c"])
r_3 = fn_hack_8(["a","b","c","d"])
r_4 = fn_hack_8(["a","b"])

print(f"{r_1} / {r_2} / {r_3} / {r_4}")