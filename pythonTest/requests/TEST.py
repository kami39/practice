str = "hello,xxxx,<fuck you}aaa/bbb/ccc"
# print (str.split('<')[1].split('}')[0])
new_str = str.split('<')[1].split('}')[0]

assert(new_str == "fuck you xxx")
assert "a" == "b"