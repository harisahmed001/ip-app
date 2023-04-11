#!/bin/bash

command=$1
if [ -z "${command}" ]; then
    python app.py
elif [[ "$command" == "unittest" ]]; then
    # There are no unit test cases for now
    python -m unittest
elif [[ "$command" == "debug" ]]; then
    sleep 100000
fi
