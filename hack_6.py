"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    nueva_lista = []

    for elemento in result:
        if elemento == "a":
            nueva_lista.append("1")
        elif elemento == "b":
            nueva_lista.append("-")
        elif elemento == "c":
            nueva_lista.append("3")
        elif elemento == "d":
            nueva_lista.append("-")
        elif elemento == "e":
            nueva_lista.append("5")
    if not nueva_lista:
        return ["0"]
    return nueva_lista


r_1 = fn_hack_6(["a", "b", "c", "d", "e"])
r_2 = fn_hack_6([])

print(f"{r_1} / {r_2}")