class OldPrinter:
    def print_text(self, text):
        print(f"Old Printer: {text}")


class NewPrinterInterface:
    def print(self, message):
        pass


class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, message):
        self.old_printer.print_text(message)


class Client:
    def __init__(self, printer):
        self.printer = printer

    def do_print(self, message):
        self.printer.print(message)


old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)
client = Client(adapter)

client.do_print("Hello, world!")
