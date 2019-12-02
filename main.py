class Product:
    def __init__(self, *, sno, name, height, barcode, inventory=None):
        self.name = name
        self.sno = sno
        self.height = height
        self.barcode = barcode
        self.inventory = inventory

    def show(self):
        print(self.name, self.sno, self.height, self.barcode, self.inventory)


row_data = 'S.no	1	2	3	Name	Juice	Water	Cookies	Height	180	170	190	Barcode	9780201379624	9780201379012	9771234567003'
headers = ['S.no', 'Name', 'Height', 'Barcode', 'Inventory']
data = row_data.split()
no_rows = 4
product = {}

for header in headers:
    if header in row_data:
        pos = data.index(header)
        product[header] = data[pos+1:pos+no_rows]

row = 0
while row < no_rows-1:
    try:
        product['Name'][row] = Product(sno=product['S.no'][row], name=product['Name'][row],
                                       height=product['Height'][row], barcode=product['Barcode'][row],
                                       inventory=product['Inventory'][row])
        row += 1
    except KeyError:
        product['Name'][row] = Product(sno=product['S.no'][row], name=product['Name'][row],
                                       height=product['Height'][row], barcode=product['Barcode'][row])
        row += 1

product['Name'][0].show()
product['Name'][1].show()
product['Name'][2].show()


