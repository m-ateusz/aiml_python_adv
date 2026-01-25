from abc import ABC, abstractmethod

class Document(ABC):
    filename: str
    def __init__(self, filename: str):
        self.filename = filename
        self.ext = filename.rsplit('.', 1)[-1]

    @abstractmethod
    def show(self): raise NotImplementedError

class PDFDocument(Document):
    def show(self):
        print(f'dPDF File: {self.filename}')

class DOCXDocument(Document):
    def show(self):
        print(f'dDOCX File: {self.filename}')



document = PDFDocument('test.pdf')
document.show()

document2 = DOCXDocument('test.docx')
document2.show()