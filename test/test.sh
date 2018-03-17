#!/bin/bash

source activate astrosql_env # Only works if your anaconda has astrosql_env as an available environment
# You may run the following to create the environment:
# conda env create --name astrosql_env --file environment.yml

outfile="test.txt"
astrosql = '../astrosql' # You would not have to do this if 'astrosql' is in PATH

# Query local APASS and save
astrosql apass 1 63 1 -o test.txt -v
