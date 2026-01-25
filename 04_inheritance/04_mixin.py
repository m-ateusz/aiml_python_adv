class PrinterMixin:
    printer_name: str

    def __init__(self, printer_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {printer_name=} and {kwargs=}')
        self.printer_name = printer_name
        self.test = printer_name
        super().__init__(**kwargs)


    def print(self, text) -> None:
        raise NotImplemented

class ScannerMixin:
    scanner_name: str

    def __init__(self, scanner_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {scanner_name=} and {kwargs=}')
        self.scanner_name = scanner_name
        self.test = scanner_name
        super().__init__(**kwargs)

    def scan(self, document) -> str:
        raise NotImplemented

    def fax(self, phone, text) -> None:
        print(f'faxing @ scanner {self.model}')



class FaxMixin:
    fax_name: str

    def __init__(self, fax_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {fax_name=} and {kwargs=}')
        self.fax_name = fax_name

        super().__init__(**kwargs)


    def fax(self, phone, text) -> None:
        print('faxing')

class XeroMixin(PrinterMixin, ScannerMixin):
    xero_name: str

    def __init__(self, xero_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {xero_name=} and {kwargs=}')
        self.xero_name = xero_name
        self.test = xero_name

        super().__init__(**kwargs)

    def xero(self, document) -> None:
        docu = self.scan(document)
        self.print(docu)


class HP(XeroMixin, PrinterMixin, FaxMixin, ScannerMixin):
    model: str

    def __init__(self, model, **kwargs):
        print(f'Init: {self.__class__.__name__} with {model=} and {kwargs=}')
        self.model = model
        super().__init__(**kwargs)

    def testa(self):
        self.fax('a', 'b')
        FaxMixin.fax(self, 'a', 'b')
        ScannerMixin.fax(self, 'a', 'b')

hp = HP(model='D2055pn', xero_name='xero', printer_name='printer', fax_name='fax', scanner_name='scanner')
hp.testa()

