from db_populate.datlibs.datlibs import DatReader
from db_populate.db_populate import DBConnect, DBInitialSetup
from db_populate.config_new_db import config_new
from db_populate.config_existing_db import config_existing

import time
tm = time.time()

## below test code is for reading in the generated dat file
## and getting the max size of each field
d = DatReader("E:/DEV/01_PROJECTS/30_DAT_VIEWER_SAMPLES/test.DAT",
              has_headers=True)
print(d.headers)
d.print_report() ## will auto inspect columns, can be slow

## below test code is to connect to the database
# args = config_new()
# database = DBConnect(**args)
# database.close()
# print("tested connect success")

database = DBInitialSetup("dat_viewer_main2")

# database.connect(**args)
# database.dbsetup()
# print("Tested DB initialization success")
i
args = config_existing()
database.connect(**args)
database.tbltest()
database.tblwrite("x")
database.tbltest()
database.close()

print(time.time() - tm)
