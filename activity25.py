print("DICTIONARY")

bnd = ["sungho", "riwoo","jaehyun","leehan","taesan","woonhak"]
bnd_m = {"03f" : "sungho","03s": "riwoo","03t": "jaehyun","04f": "taesan","04s": "leehan","06": "woonhak"}

print(bnd)
bnd.append("zico")
print(bnd)

print(bnd[-1])

print(bnd_m["06"])

bnd.append("koz")
print(bnd)

bnd.remove("zico")
print(bnd)

bnd.pop()
print(bnd)

bnd.sort()
print(bnd)

bnd.reverse()
print(bnd)


