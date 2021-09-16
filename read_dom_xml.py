from xml.dom import minidom
import os

file_name = 'dom_example.xml'
full_file = os.path.abspath(os.path.join('data', file_name))

domtree = minidom.parse(full_file)
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print("------PERSON--------")
    if person.hasAttribute('id'):
        print("ID {}" .format(person.getAttribute('id')))

    print("Name: {}" .format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = 'Change Name'
persons[0].setAttribute('id', '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = '-10'
domtree.writexml(open(file_name,'w'))