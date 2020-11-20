import glob
import pdfplumber

import shutil
import re
from collections import Counter

pdf = glob.glob("pdf/others/*")

years =['1994', '1995', '1996', '1997', '1998', '1999', '2000','2001', '2002', '2002', '2003', '2004', '2005','2006', '2007', '2008', '2009', '2010', '2011','2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

print(len(pdf))

import os


def change_name(name):
    out = name.split("/")[2]
    if ".pdf" not in out:
        out = out+".pdf"
    return(out)

def output(name_file, output_name, year):
    output_name = year+"_"+output_name
    if not os.path.exists("pdf/others/"+year):
        os.makedirs("pdf/others/"+year)

    shutil.move(name_file, 'pdf/others/'+year+"/"+output_name)


not_found=[]
outdated=[]
year_found=[]
for elem in pdf:
    counter=0
    print("Nome:"+elem)
    output_name = change_name(elem)
    print("Nome_out:"+elem)
    pdf = pdfplumber.open(elem)
    page = pdf.pages[0]
    text = page.extract_text()
    found=False
    found=[]
    year_r = re.compile('|'.join(years))
    a = year_r.findall(text)
    for i in years:
        if i in text:
            found=True
            
    if found==True:
        year_found.append(int(a[0]))
        print(a[0])
        output(elem, output_name,a[0])



    if found==False:
        not_found.append(elem)

    pdf.close()
    
#print(not_found)
#print(len(not_found))
#print(not_found)
print(len(year_found))
