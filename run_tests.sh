#!/bin/bash

set -e

source venv/bin/activate
pytest tests/
exit_code=$?

if [ $exit_code -eq 0 ]; then
  echo "All tests passed!"
  exit 0
else
  echo "Some tests failed."
  exit 1
fi
