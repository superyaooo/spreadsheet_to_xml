from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import xlrd
from xml.dom import minidom

# this function indents xml tags
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



class Generator(object):
    def __init__(self, root_tag):
        self.root_tag = root_tag

    def set_root(self):
        self.root = Element(self.root_tag)
        self.tree = ElementTree(self.root)

    # adds sub element onto root
    def sub_element(self, elem, elem_text):
        self.sub_tag = Element(elem)
        self.root.append(self.sub_tag)
        self.sub_tag.text = elem_text

    def generator(self, xls_file):

        # reads xls file
        workbook = xlrd.open_workbook(xls_file)
        worksheet = workbook.sheet_by_index(0)

        # gets the number of columns and rows of the xls file
        col_num = worksheet.ncols
        row_num = worksheet.nrows

        # loops through xls rows and columns, then generates xml sections
        for row in range(1,row_num):
            # sets root of the xml section of current row
            self.set_root()
            subs = {}

            for col in range(0,col_num):
                col_name = worksheet.cell(0,col).value

                if 'Name' in col_name:
                    # sets sub-element tag name of current cell data
                    subtag_name = "name"
                    # sets sub-element text of current cell data
                    sub_text = worksheet.cell(row,col).value

                    #updates subs dictionary with sub-element tag name and text
                    subs.update({subtag_name:sub_text})

                if 'Deadline' in col_name:
                    subtag_name = "deadline"
                    sub_text = worksheet.cell(row,col).value

                    toStrip = ['.','th','nd','st','rd',' ']
                    months ={'January':'1/','Feburary':'2/','March':'3/',
                    'April':'4/','May':'5/','June':'6/','July':'7/',
                    'August':'8/','September/':'9/','October':'10/',
                    'November':'11/','December':'12/','and':','}

                    for key, val in months.iteritems():
                        if key in sub_text:
                            sub_text = sub_text.replace(key,val)

                    for i in range(0,len(toStrip)):
                        char = toStrip[i]
                        if char in sub_text:
                            sub_text = sub_text.replace(char,'')

                    subs.update({subtag_name:sub_text})

                if 'Description' in col_name:
                    subtag_name = "description"
                    sub_text = worksheet.cell(row,col).value

                    subs.update({subtag_name:sub_text})

                if 'Website' in col_name:
                    subtag_name = "url"
                    sub_text = worksheet.cell(row,col).value

                    subs.update({subtag_name:sub_text})

            # adds xml sub-element onto the root by pre-designed order
            ordered_names = ['name','url','deadline','description']
            for i in range(0,len(ordered_names)):
                sub_name = ordered_names[i]
                sub_text = subs[sub_name]

                self.sub_element(sub_name,sub_text)

            # adds xml section to file; if file doesn't exist, creates it first
            indent(self.root)
            f = open("test.xml", "a")
            self.tree.write(f)
            f.close()

    #     self.clean_up()
    #
    # # def replaceText(node, newText):
    # #     node.firstChild.replaceWholeText(newText)
    #
    #
    # def clean_up(self):
    #     doc = minidom.parse("test.xml")
    #     nodes = doc.childNodes.getElementsByTagName("program")
    #
    #     for node in nodes:
    #         deadline = node.getElementsByTagName("deadline").nodeValue
    #         if '.' in deadline:
    #             deadline = deadline.strip('.')
    #
    #
    #     f = open("test.xml","w")
    #     doc.write(f)
    #     f.close()





new_xml = Generator("program")
new_xml.generator("Scholarship_example.xlsx")
