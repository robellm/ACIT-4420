import re

file = open("canvas", "rt")
content = file.read()
#print(content)

a1 = re.findall("\w{1}\d{6}@oslomet.no", content)
print(a1)
print()

a2 = re.findall(r'[\w\.-]+@[\w\.-]+', content)
print(a2)
print()

a3 = re.findall(r'(\d{1,2} (?:Aug|Sep) \w{2} \d+:\d+)', content)
print(a3)
print()

a4 = re.findall(r'(fs:\d+:\d+)', content)  
print(a4)
print()

a5 = re.findall(r'(\d+:\d+:\d+)', content)
print(a5)
print()

a6 = re.findall(r"\n([a-øA-Ø]+(?:[ -][a-øA-Ø]+)+)\n", content)      # (?:\n)([a-øA-Ø]+(?:[ -][a-øA-Ø]+)+)(?:\n)
print(a6)
print()

a7 = re.findall(r"\n([a-øA-Ø]+(?:[ -][a-øA-Ø]+)+)\n.*\n.*\n.*\n.*\n(?:[1-9][0-9]:\d{2}:\d{2})", content)
print(a7)
print()

a8 = re.findall(r"\n([a-øA-Ø]+(?:[ -][a-øA-Ø]+)+)\n.+\n.+\n.+\n\d+\w(?: Aug)", content)
print(a8)
