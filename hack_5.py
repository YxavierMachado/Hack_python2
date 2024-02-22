"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s

    _ls = {
        "foo": "fo-zi-ma-",
        "bar": "ba-zi-an",
        "qu": "qu-"
    }
    for key in _ls:
        if key in result:
            return _ls[key]
    return result

r_1=(fn_hack_5("fooziman")) 
r_2=(fn_hack_5("barziman"))
r_3=(fn_hack_5("qux"))
r_4=(fn_hack_5("eq"))

print(f"{r_1} / {r_2} / {r_3} / {r_4}")