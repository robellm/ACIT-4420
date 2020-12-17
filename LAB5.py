import re

file = open("canvas", "rt")
content = file.read()
#print(content)

a1 = re.findall("\w{1}\d{6}@oslomet.no", content)
print(a1)

a2 = re.findall(r'[\w\.-]+@[\w\.-]+', content)
print(a2)

a3 = re.findall(r'(\w+ [\d+ \w(?: Aug|Sep)]+[\d{2}]+:[\d{2}]+)', content)
print(a3)

a4 = re.findall(r'fs:[0-9]{3}:[0-9]{7}', content)
print(a4)

a5 = re.findall(r'\d{2}:\d{2}:\d{2}', content)
print(a5)

a6 = re.findall(r"\n([a-øA-Ø]+(?:[ -][a-øA-Ø]+){1,4})\n", content)
print(a6)

a7 = re.findall(r"\n([a-øA-Ø]+(?:[ -][a-øA-Ø]+){1,4})\n.*\n.*\n.*\n.*\n(?:[1-9][0-9]:\d{2}:\d{2})", content)
print(a7)

a8 = re.findall(r"\n([a-øA-Ø]+(?:[ -][a-øA-Ø]+){1,4})\n.+\n.+\n.+\n\d+\w(?: Aug)", content)
print(a8)
