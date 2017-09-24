from db_populate.datlibs.datlibs import DatReader

d = DatReader("test.DAT")

print(d.headers)

for row in d.reader_gen():
    # print(row)
    pass