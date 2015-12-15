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

models.db.close()
