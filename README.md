[![Build Status](https://travis-ci.org/ketozhang/astroSQL.svg?branch=master)](https://travis-ci.org/ketozhang/astroSQL)

# astroSQL - Simple Database Tools for Python

Simple Python API to access existing or create astronomy MySQL database.
> While designed for astronomy, astroSQL can be used for every field.

## Features
* **astroSQL** Python API:
  - [x] create SQL database table
  - [x] read SQL database table
  - [x] update SQL database table
  - [x] SQL query using peewee ORM
* **astroSQL** Shell Command
  - [ ]  query SQL database to text-based file
  - [ ]  update SQL database with text-based file
  
## Dependencies
* MySQL server
* Python 3.x

## Setup

1. Perform a `pip install`,

    ```sh
    $ pip install astroSQL
    ```

    Check the version installed:

    ```sh
    $ pip show astroSQL
    ```

2. Edit the configuration file as necessary in `~/.astrosql/config.yml`:

    <!-- $ ls $(python -c "import site; print(site.getsitepackages()[0])")/astrosql -->
    ```yml
    # Uncomment 'forward' if you want to place config.yml elsewhere, specify the file path (maybe `~/.astrosql/config.yml` ?)
    # forward: '/path/to/config.yml'

    # Comment out any unecessary lines, empty will be read
    mysql:
        host: 'localhost'
        user: 'username'
        password: ''
        database: 'database_name'
    ```


    > <span style="color:rgb(200,0,0)">WARNING:</span> Keep this file secure if password is written

3. Test setup

    ```python
    >>> from astrosql.sqlconnector import connect
    >>> from astrosql import AstroSQL

    >>> db = AstroSQL(connect()) # connect does not need args as it reads from config.yml
    >>> db.tables.values()
    dict_values(['tb1, tb2, ...']) # should output all table names from your database
    ```

## Usage

See [wiki](https://github.com/ketozhang/astroSQL/wiki):

* [Python Usage](https://github.com/ketozhang/astroSQL/wiki/Python-Usage)

## References
**Filippenko Group - Project Team**

The program was built for the Filippenko Group, astronomy researchers led by [Alex Filippenko](https://astro.berkeley.edu/faculty-profile/alex-filippenko) for analyzing data from the Lick Observatory and Keck Observatory.

Project team led by [Keto Zhang](https://github.com/ketozhang) and [Weikang Zheng](https://astro.berkeley.edu/researcher-profile/2358133-weikang-zheng).

**Source Code and Inspiration**:

Some parts of the program was provided by and inspired from [Issac Shiver](https://github.com/ishivvers) and [Thomas Tu](https://github.com/thomastu) from the [FlipperPhoto repository](https://github.com/ketozhang/FlipperPhoto/tree/master/flipp/libs).
