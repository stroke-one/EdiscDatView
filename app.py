from db_populate.datlibs.datlibs import DatReader
from db_populate.db_populate import DBConnect, DBInitialSetup
from db_populate.config_new_db import config_new
from db_populate.config_existing_db import config_existing

import time
tm = time.time()

## below test code is for reading in the generated dat file
## and getting the max size of each field
# d = DatReader("test.DAT", has_headers=True)
# print(d.headers)
# d.print_report()

## below test code is to connect to the database
# args = config_new()
# database = DBConnect(**args)
# database.close()
# print("tested connect success")

database = DBInitialSetup("dat_viewer_main2")

# database.connect(**args)
# database.dbsetup()
# print("Tested DB initialization success")

args = config_existing()
database.connect(**args)
# database.tblsetup()
# print("Tested table initialization success")
database.tblwrite("one")

database.tbltest()
print(time.time() - tm)
