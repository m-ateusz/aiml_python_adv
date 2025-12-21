class PrinterMixin:
    printer_name: str

    def __init__(self, printer_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {printer_name=} and {kwargs=}')
        self.printer_name = printer_name
        super().__init__(**kwargs)

    def print(self, text) -> None:
        raise NotImplemented

class ScannerMixin:
    scanner_name: str

    def __init__(self, scanner_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {scanner_name=} and {kwargs=}')
        self.scanner_name = scanner_name
        super().__init__(**kwargs)

    def scan(self, document) -> str:
        raise NotImplemented

class FaxMixin:
    fax_name: str

    def __init__(self, fax_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {fax_name=} and {kwargs=}')
        self.fax_name = fax_name
        super().__init__(**kwargs)

    def fax(self, phone, text) -> None:
        raise NotImplemented

class XeroMixin(PrinterMixin, ScannerMixin):
    xero_name: str

    def __init__(self, xero_name, **kwargs):
        print(f'Init: {self.__class__.__name__} with {xero_name=} and {kwargs=}')
        self.xero_name = xero_name
        super().__init__(**kwargs)

    def xero(self, document) -> None:
        docu = self.scan(document)
        self.print(docu)


class HP(XeroMixin, PrinterMixin, ScannerMixin, FaxMixin):
    model: str

    def __init__(self, model, **kwargs):
        print(f'Init: {self.__class__.__name__} with {model=} and {kwargs=}')
        self.model = model
        super().__init__(**kwargs)


hp = HP(model='D2055pn', xero_name='xero', printer_name='printer', fax_name='fax', scanner_name='scanner')

