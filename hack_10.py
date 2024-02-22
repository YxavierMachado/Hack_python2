"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    count = 1
    for item in s:
        if isinstance(item, dict):
            new_dict = {str(count): str(count + 1)}
            result.append(new_dict)
            count += 2
        else:
            new_set = {str(count), str(count + 1)}
            result.append(new_set)
            count += 2
    return result

s = [{"a":"b"},{"c","d"},{"e":"f"}]
print(fn_hack_10(s))