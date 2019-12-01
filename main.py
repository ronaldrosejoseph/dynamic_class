class Product:
    def __init__(self, sno, name, height, barcode):
        self.name = name
        self.sno = sno
        self.height = height
        self.barcode = barcode

    def show(self):
        print(self.name, self.sno, self.height, self.barcode)


# one = Product('Ron', 26)
# one.show()

row_data = 'S.no	1	2	3	Name	Juice	Water	Cookies	Height	180	170	190	Barcode	9780201379624	9780201379012	9771234567003'
headers = ['S.no', 'Name', 'Height', 'Barcode', 'Inventory']
data = row_data.split()

print(data)
no_rows = 4

i = 0
while i < len(data):
    data[i] = Product(data[i], data[i+1])
    data[i].show()
    if i <= len(data) - no_rows + 1:
        i += no_rows - 1


