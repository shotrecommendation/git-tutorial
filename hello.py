import sys

# Default value is "World"
# Author: Wojciech Wołujewicz (wojciech.wolujewicz@notmyrealemail.com)
name = sys.argv[1] if len(sys.argv) > 1 else "World"

print(f"Hello, {name}!")
