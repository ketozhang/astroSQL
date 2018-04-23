import sys
from pathlib import Path
from termcolor import colored
sys.path.append(str(Path(__file__).absolute().parents[1]))
from astrosql.sqlconnector import connect
from astrosql.astrosql import AstroSQL

# Initialize database
connection = connect(user='keto', database='photometry_cal') # is this redundant?
db = AstroSQL(connection) # photometry_cal_db
table = db.get_table("images")
