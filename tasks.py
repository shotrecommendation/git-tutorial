from invoke import task
import sys

name = sys.argv[1]


@task
def build(c, name=""):
    c.run(f"python3 lib/hello.py {name}")
