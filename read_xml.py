import os
from xml.etree import ElementTree

file_name = 'dom_example.xml'
full_file = os.path.abspath(os.path.join('data', file_name))
dom = ElementTree.parse(full_file)

courses = dom.findall('course')

for c in courses:
    title = c.find('title').text
    nums = c.find('crse').text
    days = c.find('days').text
    print("{title} {num} {days}" .format(title=title, num=nums, days=days))