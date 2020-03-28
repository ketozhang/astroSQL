# astroSQL

SQL database introspection and methods in Python for existing astronomy databases.

## Features

- **astroSQL** Python API:
  - [x] Uses Peewee SQL ORM.
  - [x] Workflow: connects to database -> get by table name -> query by various methods.
  - [x] Smartly inspects database to gather table/schema removing the need to create database models.
  - [x] Collection of simple SQL read and write methods.


## System Dependencies

- Python 3.6.1+
- MySQL server

## Setup

1. Use pip to install from pypa source or git clone source

   ```sh
   # Pypa
   pip install astrosql
   ```

   ```sh
   # Github
   git clone git@github.com:ketozhang/astroSQL.git
   cd astroSQL/
   pip install .
   ```

   > But there is no setup.py?
   > `pyproject.yaml` is the setup file, using a new convention [PEP 517](https://www.python.org/dev/peps/pep-0517/)

2. Edit the configuration file as necessary in `~/.astrosql/config.yml`:

   <!-- $ ls $(python -c "import site; print(site.getsitepackages()[0])")/astrosql -->

   ```yml
   # Uncomment 'forward' if you want to place config.yml elsewhere, specify the file path (maybe `~/.astrosql/config.yml` ?)
   # forward: '/path/to/config.yml'

   # Comment out any unecessary lines, empty will be read
   mysql:
     host: "localhost"
     user: "username"
     password: ""
     database: "database_name"
   ```


    > <span style="color:rgb(200,0,0)">WARNING:</span> Keep this file secure if password is written

## Usage

1. Before you get started, make sure your SQL database is up and running.
  For instance on Linux run,

    ```sh
    sudo service mysql status
    ```

2. Test out your connection

    ```python
    from astrosql import AstroSQL

    # This will use your credentials at ~/.my.cnf
    db = AstroSQL("DATABASE_NAME")

    # You may specify the path to CNF
    db = AstroSQL("DATABASE_NAME", read_default_file="/path/to/my.cnf")

    # Otherwise manually enter it yourself
    # Check https://pymysql.readthedocs.io/en/latest/modules/connections.html for more options
    db = AstroSQL("DATABASE_NAME", user="USERNAME", password="PASSWORD", host="localhost")

    # Print all avaialable tables
    print(db.tables.values())
    ```
3. Take a look at the [API Referfence](#api_reference) section for commands.

## API Reference

### AstroSQL
```
class astrosql.AstroSQL(database, **kwargs)
```

Assume the following was run correctly `db = AstroSQL(...)`,

* `get_table`

  ```python
  db.get_table("example")
  ```
* `array2sql`

  ```python
  # Schema assumed to have columns id TINYINT, name VARCHAR, mag decimal(3, 10)
  data = [
      [1, "SN1987A", 2.9]
      [2, "SN1993J", 10.8]
  ]

  db.array2sql("example", data)

  ```
* `dict2sql`

  ```python
  data = [
    {"id": 1, "name": "SN1987A", "mag": 2.9}
    {"id": 2, "name": "SN1993J", "mag": 10.8}
  ]

  db.dict2sql("example", data)
  ```
* `text2sql`

  ```
  # data.txt
  1  SN1987A  2.9
  2  SN1993J  10.8
  ```

  ```python
  db.text2sql("example", "/path/to/data.txt")
  ```
* `get`

  **DEPRECATING**

* `get_by_basename`
  Returns a list of data matching the base file name.

  ```python
  # Assuming the schema has a column basename of some string datatype

  db.get_by_basename("example", "BASENAME")
  ```

* `get_by_object`
  Returns a list of data matching the object name.

  ```python
  # Assuming the schema has a column objname of some string  datatype

  db.get_by_object("example", "OBJNAME")
  ```
* `get_by_radec`
  Returns a list of data queried by circle of some radius centered at some RA and Dec.

  ```python
  # Assuming the schema has ra and dec columns in degrees
  ra, dec, radius = 0, 0, 1

  db.get_by_radec("example", ra, dec, radius)
  ```
* `get_by_sql`
  Returns a list of data queried by SQL query.

  ```python
  query = "SELECT * FROM example;"
  db.get_by_sql(query)
  ```

## Abandoned Features
- **astroSQL** Shell Command
  - [ ] query SQL database to text-based file
  - [ ] update SQL database with text-based file

## References

**Filippenko Group - Project Team**

The program was built for the Filippenko Group, astronomy researchers led by [Alex Filippenko](https://astro.berkeley.edu/faculty-profile/alex-filippenko) for analyzing data from the Lick Observatory and Keck Observatory.

Project team led by [Keto Zhang](https://github.com/ketozhang) and [Weikang Zheng](https://astro.berkeley.edu/researcher-profile/2358133-weikang-zheng).

**Source Code and Inspiration**:

Some parts of the program was provided by and inspired from [Issac Shiver](https://github.com/ishivvers) and [Thomas Tu](https://github.com/thomastu) from the [FlipperPhoto repository](https://github.com/ketozhang/FlipperPhoto/tree/master/flipp/libs).
