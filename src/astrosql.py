import peewee
import peeweedb
import pandas as pd
import astropy.units as u
from pathlib import Path
from pwiz import Introspector


class AstroSQL:

    def __init__(self, db):
        """

        Parameters
        ----------
        db  : peewee.MySQLDatabase
            Peewee database
        """
        if isinstance(db, peewee.MySQLDatabase):
            self.db = db
        elif isinstance(str, db):
            raise NotImplementedError
        else:
            raise ValueError('argument [db] is neither a peewee.MySQLDatabase, nor a string')

        self.tables = Introspector.from_database(db).generate_models(literal_column_names=True)

    def get_table(self, table):
        if issubclass(type(table), peewee.BaseModel) or issubclass(type(table), peewee.Model):
            table = table
        elif isinstance(table, str):
            assert table in self.tables, "Sanity Check Failed: Table queried does not exist"
            try:
                table = peeweedb.tables[table]
            except KeyError:
                table = self.tables[table]
        else:
            raise ValueError("argument [table] is neither a string or peewee.Model or peewee.BaseModel")
        return table

    def dict2sql(self, table, data):
        """
        Write a (1, n) dictionary (single row dictionary) to mySQL.

        Parameters:
        ----------
        db  : A peewee.Database
        table : str or peewee.Model
            SQL table name or peewee.Model object to be created or appended
        data : dict
            Data to be inserted. Values cannot be array-like
        """
        assert isinstance(data, dict), "argument [data] is not a Python dictionary"
        table = self.get_table(table)

        table.create(**data)

    def text2sql(self, table, file):
        # TODO: Fix column header which is not yet parseable

        if isinstance(file, str):
            assert Path(str).exists(), "{} is not a valid file path or does not exit".format(file)
        table = self.get_table(table)

        df = pd.read_csv(file, header=None, sep="\s+", comment='#')

        print("\nFirst few rows of data (", args.file,
              "):to be loaded: \n{}\n".format(df.head()))
        print("\nLast few rows of data (", args.file,
              "):to be loaded: \n{}\n".format(df.tail()))
        print("Writing to database.\nThis may take a while...")

        data = df.to_dict('records')
        table.insert_many(data)

    def get_by_basename(self, table, basename):
        """Get data from SQL database by basename. Returns a list of dict"""
        table = self.get_table(table)

        query = table.select().where(table.basename == basename)
        print(query.sql())

        data = list(query.dicts())
        return data

    def get_by_object(self, table, objname):
        table = self.get_table(table)

        query = table.select().where(table.objname == objname)
        print(query.sql())

        data = list(query.dicts())
        return data

    def get_by_radec(self, table, ra, dec, radius):
        """
        Get data from SQL database within a square area of the sky determined by ra, dec, radius.
        Returns a list of dict
        """
        table = self.get_table(table)

        radius = radius * u.arcmin.to(u.deg)

        try:
            query = table.select().where(
                table.RA.between(ra - radius, ra + radius),
                table.DEC.between(dec - radius, dec + radius)
            )
        except AttributeError:
            query = table.select().where(
                table.centerRa.between(ra - radius, ra + radius),
                table.centerDec.between(dec - radius, dec + radius)
            )

        print(query.sql())

        data = list(query.dicts())
        return data

    def get_stars_by_radec(self, table, ra, dec, radius):
        """
        Get data from SQL database within a square area of the sky determined by ra, dec, radius.
        Returns a list of dict
        """
        table = self.get_table(table)

        radius = radius * u.arcmin.to(u.deg)

        query = table.select().where(
            table.RA.between(ra - radius, ra + radius),
            table.DEC.between(dec - radius, dec + radius)
        )
        print(query.sql())

        data = list(query.dicts())
        return data

def main(args):
    raise NotImplementedError(
        "'astrosql' command itself has not been implemented. "
        "Use 'astrosql --help' for more commands"
    )
