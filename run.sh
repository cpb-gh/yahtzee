#!/bin/bash

# Activate virtualenv
source venv/bin/activate

if [ "$1" = "test" ]; then
    PYTHONPATH=. pytest
elif [ "$1" = "play" ]; then
    python yahtzee.py
else
    echo "Usage: $0 [test|play]"
    exit 1
fi 