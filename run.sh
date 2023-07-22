#!/bin/bash

# Absolute path to this script
SCRIPT=$(readlink -f "$0")

# Absolute path this script is in
SCRIPTPATH=$(dirname "$SCRIPT")

# Run the Python script
python3 "${SCRIPTPATH}/main.py"