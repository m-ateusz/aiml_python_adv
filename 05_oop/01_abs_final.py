from abc import ABC, abstractmethod

class Document(ABC):
    filename: str

    def __init__(self, filename: str):
        self.filename = filename

    def __new__(cls, filename: str):
        ext = filename.split('.')[-1]
        print(f'Szukam klasy dla pliku: {filename}')
        for plugin in cls.__subclasses__():
            print(f'Znalazłem następującą klasę pochodną: {plugin.__name__}')
            if ext in plugin.EXT:
                return object.__new__(plugin)

        raise ValueError(f'File type {ext} is not supported')

    @abstractmethod
    def show(self): raise NotImplementedError

    @property
    @abstractmethod
    def EXT(self) -> list[str]: raise NotImplementedError

class PdfDocument(Document):
    EXT = ['pdf']

    def show(self):
        print(f'{self.__class__.__name__}: {self.filename}')

class DocxDocument(Document):
    EXT = ['docx', 'doc']
    def show(self):
        print(f'{self.__class__.__name__}: {self.filename}')

class XlsxDocument(Document):
    EXT = ['xlsx', 'xls']

    def show(self):
        print(f'{self.__class__.__name__}: {self.filename}')

class JpegDocument(Document):
    EXT = ['jpg', 'jpeg']

    def show(self):
        print(f'JPEG {self.__class__.__name__}: {self.filename}')


document = Document('test.pdf') # Jpge JPGDocument, JPEGDocumen, JpegDocument, JpgDocument
document.show()
print(f'{type(document)=}')

document = Document('test.docx')
document.show()
print(f'{type(document)=}')

document = Document('test.jpg')
document.show()
print(f'{type(document)=}')


try:
    document = Document('test.txt')
    document.show()
except ValueError as e:
    print(e)

class TxtDocument(Document):
    EXT = ['txt']
    def show(self):
        print(f'TXT {self.__class__.__name__}: {self.filename}')

document = Document('test.txt')
document.show()

