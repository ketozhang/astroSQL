# Filippenko Groups's astroSQL - Database Tools for Astronomers
*Currently usable only by Filipenko Group. Public release information will be announced [here](https://github.com/ketozhang/Filippenko-Group/projects/1).*

## Features
* Load text-based data to MySQL (`astrosql import_data`)
* Query APASS database with coordinates (`astrosql apass`)

## Upcoming Features
* **astroSQL** Basics:
    * Update SQL database
* **astroSQL+Photometry** Tools:
    * Calibaration with APASS
    * Conversion: Landolt and natural system
    * Calculation: zero-point, sky value, limiting magnitude
    * Algorithm: coordinate matching
    * Consolidate programs done by [I.Shivvers & T.Tu](https://github.com/ishivvers/FlipperPhoto).
* Release formal documentation on [this repository](https://github.com/ketozhang/Filippenko-Group) and [Wiki](heracles.astro.berkeley.edu/wiki/doku.php).

## Dependencies
* MySQL server
* [Anaconda Distribution](https://www.anaconda.com/download/) (*necessary if conda environment are used*)

## Installation (Linux)
1. Clone repository (alternative: download zip files from [release](https://github.com/ketozhang/Filippenko-Group/releases))
    ```sh
    $ git clone https://github.com/ketozhang/Filippenko-Group.git
    ```
2. Install and activate conda environment (*optional*)
    ```sh
    $ cd /path/to/program/folder
    $ conda env create -f environment.yaml
    $ source activate astrosql_env
    # You should now see (astrosql_env) before the $ sign
    ```
    If you do not wish to use a conda enviornment please see [`environment.yml`](https://github.com/ketozhang/Filippenko-Group/blob/master/environment.yml) for specific dependencies. You may also use `conda env update -f enviornment.yml` to automatically download dependencies to your Anaconda.
3. Make astroSQL Executable and setup PATH  
*It's an ALIAS; PATH doesn't work until binary file is set up*

    ```sh
    $ chmod a+x astrosql.py
    $ echo "alias astrosql='$(pwd)/astrosql.py'" >> ~/.bashrc
    $ source ~/.bashrc
    ```
4. Confirm astroSQL is working
    
    ```sh
    $ astrosql --help
    # If fails
    $ python astrosql.py --help #or
    $ ./astrosql.py --help
    ```
## References
**Filippenko Group - Project Team**  
The program was built for the Filippenko Group, astronomy researchers led by [Alex Filippenko](https://astro.berkeley.edu/faculty-profile/alex-filippenko) for analyzing data from the Lick Observatory and Keck Observatory.

Project team led by [Thomas Jaeger](https://astro.berkeley.edu/researcher-profile/3420275-thomas-de-jaeger), [Keto Zhang](https://github.com/ketozhang), and [Weikang Zheng](https://astro.berkeley.edu/researcher-profile/2358133-weikang-zheng).

**Source Code and Inspiration**:  
Some parts of the program was provided by and inspired from [Issac Shiver](https://github.com/ishivvers) and [Thomas Tu](https://github.com/thomastu) from [FlipperPhoto repo](https://github.com/ketozhang/FlipperPhoto/tree/master/flipp/libs).


