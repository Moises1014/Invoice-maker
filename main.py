import os

from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice



# choose english as language
os.environ["INVOICE_LANG"] = "en"

client = Client('Client')
provider = Provider('Your Company', bank_account='bank Account #', bank_code='2020')
creator = Creator('Your Name')

invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_US.UTF-8'
invoice.add_item(Item(32, 600, description="Elictrical panel change"))
invoice.add_item(Item(60, 50, description="fans", tax=7))
invoice.add_item(Item(50, 60, description="G5 connectors", tax=0))
invoice.add_item(Item(5, 600, description="Item 4", tax=7))

pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf", generate_qr_code=True)