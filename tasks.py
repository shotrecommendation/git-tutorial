from invoke import task
import sys

name = sys.argv[2] if len(sys.argv) > 1 or "World"

@task
def build(c, name):
    c.run(f"python3 lib/hello.py {name}")
