import sys
import os
os.chdir("..")
sys.path.append('src')
import peeweedb
from sqlconnector import connect
from astrosql import AstroSQL

# Initialize database
connection = connect() # is this redundant?
imagedb = AstroSQL(connection) # photometry_cal_db

table = imagedb.get_table('test')
apass = imagedb.get_table('apass')
basename = "UGC12893_20170808_094735_Aug78kld1_kait_clear"

# Check existence of database, if not make a test
if not table.table_exists():
    table.create()

# Delete test row if it is there
table.delete().where(table.basename == basename).execute()

data = {'basename': 'UGC12893_20170808_094735_Aug78kld1_kait_clear',
        'name': 'UGC12893_20170808_094735_Aug78kld1_kait_clear_c.fit', 'telescope': 'kait', 'pixscale': 0.7965,
        'day': '08', 'month': '08', 'year': '2017', 'hour': '09', 'minute': '47', 'second': '35',
        'mjd': 57973.40804398148, 'jd': 2457973.9080439815, 'Xsize': 500, 'Ysize': 500, 'exptime': 21.0,
        'filter': 'clear', 'uniformname': 'UGC12893_20170808_094735_Aug78kld1_kait_clear_c.fit',
        'savepath': 'kait/kait_image_calib_sucess/20170808/', 'WCSED': 'T', 'centerRa': 0.0599109204241749,
        'centerDec': 17.225563953240275, 'corner1Ra': 0.1179648995302298, 'corner1Dec': 17.28050819347097,
        'corner2Ra': 0.11729303587232165, 'corner2Dec': 17.17021905605131, 'corner3Ra': 0.0018914875602571574,
        'corner3Dec': 17.17060311387882, 'corner4Ra': 0.0024944896030061336, 'corner4Dec': 17.280892527891407,
        'fwhm': 2.06, 'sky': 8.5604364, 'zeromag': 22.6052, 'limitmag': 19.0812}

imagedb.dict2sql(table, data)

# Read from Database by Basename

data_lst = imagedb.get_by_basename(table, basename)
print(data_lst)

ra = 0.059910
dec = 17.225563953240275 
radius = 10 #arcsecond
data_lst = imagedb.get_by_radec(apass, ra, dec, radius)
print(data_lst)

