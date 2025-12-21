from abc import ABC, abstractmethod

class Document:
    filename: str

    def __init__(self, filename: str):
        self.filename = filename

    def show(self):
        match self.filename.rsplit('.', 1)[-1]:
            case 'pdf':
                print(f'PDF File: {self.filename}')
            case 'docx':
                print(f'Document File: {self.filename}')
            case 'xls':
                print(f'Excel File: {self.filename}')
            case ext:
                raise ValueError(f'File type {ext} is not supported')


document = Document('test.pdf')
document.show()

document = Document('test.docx')
document.show()