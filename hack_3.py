"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
    vowels = {'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v'}
    result = ''
    i = 0
    while i < len(s):
        if s[i] in vowels:
            result += vowels[s[i]]
        elif s[i] == 'q' and i < len(s) - 1 and s[i+1] == 'u':
            result += 'Qv'
            i += 1
        elif s[i] in {'z', 'm', 'r'}:
            result += s[i].lower()
        else:
            result += s[i].upper()
        i += 1
    return result

r_1 = fn_hack_3("fooziman") 
r_2 = fn_hack_3("barziman") 
r_3 = fn_hack_3("3q")
r_4 = fn_hack_3("qu") 
r_5 = fn_hack_3("qux") 

print(f"{r_1} / {r_2} / {r_3} / {r_4} / {r_5}")