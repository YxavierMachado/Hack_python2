"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s

    if len(s) > 5:
        result = s[1:7]
    else:
        result = s
   
    return result

r_1 = fn_hack_4("fooziman")
r_2 = fn_hack_4("barziman")
r_3 = fn_hack_4("qux")
print(f" {r_1} / {r_2} / {r_3}")