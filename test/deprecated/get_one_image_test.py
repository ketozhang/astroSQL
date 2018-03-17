import sys
import os
os.chdir("..")
sys.path.append(os.getcwd() + '/src')
import peeweedb
from query import get_by_radec
from query import get_by_basename
from sqlconnector import connect

db = connect()
table = 'images'


# Get by ra dec radius
ra = 0.3199823595554539
dec = 13.108461467703975
radius = 1 #arcmin
rows = get_by_radec(db, table, ra, dec, radius)
# print(rows)

# Get by basename
basename = str(rows['basename'])
rows = get_by_basename(db, table, basename)
# print(rows)
