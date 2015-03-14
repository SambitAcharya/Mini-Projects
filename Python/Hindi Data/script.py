from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import codecs

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

text =  convert('socialcops.pdf')

saveFile = open('socialcops.txt','w')
saveFile.write(text)
saveFile.close()

with codecs.open('socialcops.txt', encoding='utf-8') as f:
    text = f.read()

with codecs.open('socialcops2.txt','w', encoding='utf-8') as f:
    f.write(text)

# saveFile2 = open('socialcops2.txt','w')
# saveFile2.write(text)
# saveFile2.close()

# print text
