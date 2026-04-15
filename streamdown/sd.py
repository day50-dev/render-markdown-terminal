#!/usr/bin/env bash
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "pygments",
#     "pylatexenc",
#     "appdirs",
#     "term-image",
#     "wcwidth",
#     "toml"
# ]
# ///
'''':
if command -v uv &> /dev/null; then
    exec uv run --script "$0" "$@"
else
    exec python3 "$0" "$@"
fi
'''
import sys
from pathlib import Path

from sdlib import main

if __name__ == "__main__": 
    main()
