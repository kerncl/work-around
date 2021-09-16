from xml.dom import minidom
import os

list_ = ['a','b','c','d','e','f']

xml = minidom.Document()

# Root
root = xml.createElement('root')
root.setAttribute('name', 'root name')
xml.appendChild(root)

for _ in list_:
    # Section
    section = xml.createElement('Section1')
    section.setAttribute('detail', 'other details 1')
    section.setAttribute('name', _)
    root.appendChild(section)

    # Parent
    parent = xml.createElement('Parent')
    parent.setAttribute('name', 'parent 1')
    section.appendChild(parent)

# Section 2
section = xml.createElement('Section2')
section.setAttribute('detail', 'other details 2')
section.setAttribute('name', 'other details 2')
root.appendChild(section)

xml_str = xml.toprettyxml(indent='\t')

save_path_file = 'minidom_style.xml'

with open(save_path_file, 'w') as f:
    f.write(xml_str)
