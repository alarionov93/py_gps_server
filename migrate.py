__author__ = 'alex'

import models

models.db.connect()

try:
    print("Try to remove table Point...")
    models.db.drop_table(models.Point)
except:
    print("table Point does not exists!")
finally:
    print("Try to create table Point...")
    models.db.create_table(models.Point)

try:
    print("Try to remove table Report...")
    models.db.drop_table(models.Report)
except:
    print("table Report does not exists!")
finally:
    print("Try to create table Report...")
    models.db.create_table(models.Report)

models.db.close()
