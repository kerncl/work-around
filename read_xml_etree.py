import xml.etree.ElementTree as ET
import os

file_name = 'reed.xml'
full_path = os.path.abspath(os.path.join('data', file_name))
exist = os.path.exists(full_path)
mytree = ET.parse(full_path)
myroot = mytree.getroot()   #<Element 'root' #address>
#print(myroot.tag)   #root
print(myroot[0].tag)    #course
for x in myroot[0]:     #search  for myroot[0]
    print(x.tag, x.text)    #<tag> text </tag>
for x in myroot.findall('course'):  #access all the root
    reg_num = x.find('reg_num').text
    subj = x.find('subj').text
    print(reg_num,subj)
