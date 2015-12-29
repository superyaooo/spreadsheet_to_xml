from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i



#root = Element('program')
#tree = ElementTree(root)

#name = Element('name')
#root.append(name)
#name.text = "test name"

#url = Element('url')
#root.append(url)
#url.text = "test url"

#deadline = Element('deadline')
#root.append(deadline)
#deadline.text = "test deadline"

#description = Element('description')
#root.append(description)
#description.text = "test description"

class Generator(object):
    def __init__(self, root_tag):
        self.root_tag = root_tag

    def set_root(self):
        self.root = Element(self.root_tag)
        self.tree = ElementTree(self.root)

    def sub_element(self, elem, elem_text):
        self.sub_tag = Element(elem)
        self.root.append(self.sub_tag)
        self.sub_tag.text = elem_text

    def generator(self):
        self.set_root()

        #sub = raw_input("What's the sub tag?")
        #sub_text = raw_input("What's the text for %s?" % sub)

        #self.sub_element(sub, sub_text)


        #tags will not appear in order because dictionaries are unordered.
        #subs = {'name':'test name 1st', 'url':'test url 2nd', 'deadline':'test deadline 3rd', 'description':'test description 4th'}

        #for sub_tag, sub_text in subs.items():
            #self.sub_element(sub_tag, sub_text)


        subs = []
        sub1 = ['name','should be 1st']
        sub2 = ['url','should be 2nd']
        sub3 = ['deadline','should be 3rd']
        sub4 = ['description','should be 4th']

        subs.append(sub1)
        subs.append(sub2)
        subs.append(sub3)
        subs.append(sub4)

        for i in range(0,len(subs)):
            self.sub_element(subs[i][0],subs[i][1])


        indent(self.root)
        f = open("test.xml", "a")
        self.tree.write(f)
        f.close()


#indent(root)

#f=open("test.xml","a")
#tree.write(f)
#f.close()

new_xml = Generator("program")
new_xml.generator()
