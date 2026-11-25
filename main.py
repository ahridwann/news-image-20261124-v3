"""Copy the finished entry image to the output directory.

This program does no drawing, no network access and no randomness.
It only copies the pre-built entry.png that sits next to this file
into the directory named by MAKEFUN_OUTPUT_DIR.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    if not os.path.isfile(source):
        print("error: entry.png not found next to main.py: " + source,
              file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, destination)
    print("entry.png copied to " + destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
