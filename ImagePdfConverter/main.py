# tkinter
from tkinter import *
from tkinter import filedialog
# pdf 
from PyPDF2 import PdfFileWriter, PdfFileReader
import img2pdf

filename = ()
label_files = None

def browseFiles():
    global filename, label_files
    filename = filedialog.askopenfilename(title = "Select Files",
                                          filetypes = (("JPG","*.jpg"),("JPEG","*.jpeg"),("pdf","*.pdf")),
                                          multiple=True)
    label_files.configure(text=filename)

def mergePdf():
    global filename, label_files

    output = PdfFileWriter()
    input1 = PdfFileReader(open("ImagePdfConverter/output.pdf", "rb"))
    output.addPage(PdfFileReader(open(filename[0],"rb")).getPage(0))
    output.addPage(input1.getPage(0))
    output.addPage(input1.getPage(1))

    outputStream = open("ImagePdfConverter/document-output.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

    filename = ()
    label_files.configure(text="Done!")


def convertPdf():
    global filename, label_files
    # write code for converting img to pdf.

    with open("ImagePdfConverter/output.pdf", "wb") as f:
        f.write(img2pdf.convert([i for i in filename]))

    filename = ()
    label_files.configure(text="Done!")

def init():
    # always run 
    global label_files

    window = Tk()
    window.title('Image/Pdf Converter')
    window.geometry("1000x1000")

    button_explore = Button(window,text = "Select Files",
                            command = browseFiles)
    button_explore.grid(column = 2, row = 1)

    label_files = Label(window,text = "",width = 100, height = 4,fg = "blue")
    label_files.grid(column = 2, row = 2)

    button_convert = Button(window,text="Convert to Pdf",
                            command = mergePdf)
    button_convert.grid(column = 2, row = 4)

    window.mainloop()

if __name__ == "__main__" :
    init()