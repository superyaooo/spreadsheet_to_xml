This app reads from an excel file and then generates an xml file with pre-designed tags/nodes, order and pretty format.
It automates most part of the tedious process of manually updating an existing XML file and adjusting the format node by node, line by line.




****************** basic xml generation concept ******************

root = Element('program')
tree = ElementTree(root)

name = Element('name')
root.append(name)
name.text = "test name"

url = Element('url')
root.append(url)
url.text = "test url"

deadline = Element('deadline')
root.append(deadline)
deadline.text = "test deadline"

description = Element('description')
root.append(description)
description.text = "test description"


def indent():
	“””indent xml tags”””

indent(root)

f=open("test.xml","a")
tree.write(f)
f.close()

****************** end of basic xml generation concept ******************





⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇  ⬇ ⬇ Generator Development Version History ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇  ⬇ ⬇ 


Version.05 successfully grabs all the data(every row, every column) from an excel file, and generates an xml file with xml nodes in the desired order and format.






********************* GENERATOR VERSION.01 ===> use raw_input *********************

        sub = raw_input("What's the sub tag?")
        sub_text = raw_input("What's the text for %s?" % sub)

        self.sub_element(sub, sub_text)




********************* GENERATOR VERSION.02 ===> use dictionary *********************

#tags will not appear in order because dictionaries are unordered.

        subs = {'name':'test name 1st', 'url':'test url 2nd', 'deadline':'test deadline 3rd', 'description':'test description 4th'}

        for sub_tag, sub_text in subs.items():
             self.sub_element(sub_tag, sub_text)




******************** GENERATOR VERSION.03 ===> use a list of lists *********************

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





************** GENERATOR VERSION.04 ===> use a list of lists and insert list by index **************


    def generator(self, xls_file):

        self.set_root()

	tags = []
        workbook = xlrd.open_workbook(xls_file)
        worksheet = workbook.sheet_by_index(0)

        col_num = worksheet.ncols

        for n in range(0,col_num):

            col_name = worksheet.cell(0,n).value

            if 'Name' in col_name:
                subtag_name = "name"
                sub_text = worksheet.cell(1,0).value

                tag = []
                tag.append(subtag_name)
                tag.append(sub_text)

                tags.insert(0, tag)


            if 'Deadline' in col_name:
                subtag_name = "deadline"
                sub_text = worksheet.cell(1,n).value

                tag = []
                tag.append(subtag_name)
                tag.append(sub_text)

                tags.insert(2,tag)


            if 'Description' in col_name:
                subtag_name = "description"
                sub_text = worksheet.cell(1,n).value

                tag = []
                tag.append(subtag_name)
                tag.append(sub_text)

                tags.insert(3,tag)

                
            if 'Website' in col_name:
                subtag_name = "url"
                sub_text = worksheet.cell(1,n).value

                tag = []
                tag.append(subtag_name)
                tag.append(sub_text)

                tags.insert(1,tag)

        for i in range(0,len(tags)):
            self.sub_element(tags[i][0],tags[i][1])
               


        indent(self.root)
        f = open("test.xml", "a")
        self.tree.write(f)
        f.close()





********************* GENERATOR VERSION.05 ===> use a dictionary and a list *********************


def generator(self, xls_file):

        workbook = xlrd.open_workbook(xls_file)
        worksheet = workbook.sheet_by_index(0)

        col_num = worksheet.ncols
        row_num = worksheet.nrows

        for row in range(1,row_num):
            self.set_root()
            subs = {}

            for col in range(0,col_num):
                col_name = worksheet.cell(0,col).value

                if 'Name' in col_name:
                    subtag_name = "name"
                    sub_text = worksheet.cell(row,col).value

                    subs.update({subtag_name:sub_text})

                if 'Deadline' in col_name:
                    subtag_name = "deadline"
                    sub_text = worksheet.cell(row,col).value

                    subs.update({subtag_name:sub_text})

                if 'Description' in col_name:
                    subtag_name = "description"
                    sub_text = worksheet.cell(row,col).value

                    subs.update({subtag_name:sub_text})

                if 'Website' in col_name:
                    subtag_name = "url"
                    sub_text = worksheet.cell(row,col).value

                    subs.update({subtag_name:sub_text})


            ordered_names = ['name','url','deadline','description']

            for i in range(0,len(ordered_names)):
                sub_name = ordered_names[i]
                sub_text = subs[sub_name]
                self.sub_element(sub_name,sub_text)

            indent(self.root)
            f = open("test.xml", "a")
            self.tree.write(f)
            f.close()
