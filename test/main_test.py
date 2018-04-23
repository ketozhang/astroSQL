import sys
from pathlib import Path
from termcolor import colored
sys.path.append(str(Path(__file__).absolute().parents[1]))
from astrosql.sqlconnector import connect
from astrosql.astrosql import AstroSQL

# Initialize database
connection = connect(user='keto', database='photometry_cal') # is this redundant?
imagedb = AstroSQL(connection) # photometry_cal_db

images = imagedb.get_table('images')
test = imagedb.get_table('test')
apass = imagedb.get_table('apass')
basename = "UGC12893_20170114_021408_Jan7ecjv1_kait_clear"

# Check existence of database, if not make a test
if not test.table_exists():
    test.create()

# Delete test row if it is there
# test.delete().where(table.basename == basename).execute()
#
data = {'WCSED': 'T',
        'Xsize': 500,
        'Ysize': 500,
        'basename': 'UGC12893_20170114_021408_Jan7ecjv1_kait_clear',
        'centerDec': 17.2308087040803,
        'centerRa': 0.0828087007500955,
        'corner1Dec': 17.2857047424775,
        'corner1Ra': 0.140795075737313,
        'corner2Dec': 17.1754709082448,
        'corner2Ra': 0.140288467421476,
        'corner3Dec': 17.1758960402101,
        'corner3Ra': 0.0248567487641813,
        'corner4Dec': 17.2861301294623,
        'corner4Ra': 0.0252945412882462,
        'day': '14',
        'exptime': 24.0,
        'filter': 'clear',
        'fwhm': 3.76,
        'hour': '02',
        'jd': 2457767.59314815,
        'limitmag': 18.943,
        'minute': '14',
        'mjd': 57767.0931481481,
        'month': '01',
        'name': 'Jan7ecjv_c.fit',
        'objname': 'UGC12893',
        'pixscale': 0.7965,
        'savepath': 'kait/kait_image_calib_sucess/20170114/',
        'second': '08',
        'sky': 10.207877,
        'telescope': 'kait',
        'uniformname': 'UGC12893_20170114_021408_Jan7ecjv1_kait_clear_c.fit',
        'year': '2017',
        'zeromag': 22.6581}
#
# imagedb.dict2sql(table, data)

# Read from database by basename

basename = "UGC12893_20170114_021408_Jan7ecjv1_kait_clear"
data_lst = imagedb.get_by_basename(imagedb.get_table('images'), basename)
# print(data_lst)
print(colored('\nSUCCESS: Read by basename\n', 'green')) if data_lst[0] == data else print(colored('\nFAILED\n', 'red'))

# Read from database by object name
objname = 'UGC12893'
data_lst = imagedb.get_by_object(imagedb.get_table('images'), objname)
# print(data_lst)
print(colored('\nSUCCESS: Read by objname\n', 'green')) if data_lst[2] == data else print(colored('\nFAILED\n', 'red'))

# Read from database by ra, dec, and radius
ra = 0.0828087007500955
dec = 17.2308087040803
radius = 10 # arcsecond
data_lst = imagedb.get_by_radec(imagedb.get_table('images'), ra, dec, radius)
# print(data_lst)
print(colored('\nSUCCESS: Read by ra, dec, radius\n', 'green')) if data_lst[0] == data else print(colored('\nFAILED\n', 'red'))

# Read from apass by ra, dec, and radius
ra = 0.059910
dec = 17.225563953240275 
radius = 10 # arcsecond
data_lst = imagedb.get_by_radec(apass, ra, dec, radius)
# print(data_lst)
print(colored('\nSUCCESS: Read apass by ra, dec, radius\n', 'green'))

