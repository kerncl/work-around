import re

pattern = "Found --swcfg=/(.*) option()"
b = re.finditer(r"([^\\]\([^\)]*\)) ", pattern)
c = re.findall(r'([^\\]\([^\)]*\))', pattern)
for item in b:
    print(item)
for item in c:
    print(item)
