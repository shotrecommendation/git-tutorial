import sys
import greeter

# Default value is "World"
# Author: Wojciech Wołujewicz (wojciech.wolujewicz@notmyrealemail.com)
name = sys.argv[1]

greet = greeter.Greeter(name)
greet.greet()
