d = {"George":6946191412, "Jim":6948925566, "Mom":6945538379, "Dad":6978920047}
d["Sam"] = 69809788945
print(d)
del d["Sam"]
print(d)
# how to print all values

for key in d:
    print("key:",key,"value:",d[key])

