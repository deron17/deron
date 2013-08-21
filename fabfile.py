from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def pull():
    with settings(warn_only=True):
        result = local('python login.py', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def test():
    local('python login.py')

def commit():
    local("git add . && git commit -m 'aasd'")

def deneme():
    pull()
    test()