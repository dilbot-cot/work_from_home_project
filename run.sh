#!/bin/bash

# Absolute path to this script
SCRIPT=$(readlink -f "$0")

# Absolute path this script is in
SCRIPTPATH=$(dirname "$SCRIPT")

# Run the Python script located in the 'src' subdirectory
python3 "${SCRIPTPATH}/src/main.py"