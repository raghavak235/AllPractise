# https://www.geeksforgeeks.org/tag/python-regex-programs/?type=popular
import re


def extract_from_html():
    inp= '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'
    tag ='br'
    result=re.findall()


# Python program to find files having a particular extension using RegEx
def extension_regex():
    filenames = ["gfg.html", "geeks.xml",
                 "computer.txt", "geeksforgeeks.jpg"]
    for file in filenames:
        match = re.search('\.xml$', file)
        if match:
            print('match found')



