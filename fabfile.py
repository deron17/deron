from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm
import sys

def test1():
    with settings(warn_only=True):
        result = local('python login.py', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def test():
    local('python login.py')

def commit():
    local("git add . && git commit -m 'aasd'")

def push():
    local("git push origin master")

def pull():
    code_dir = '/home/vokaladmin/DjangoProjects/fabrictest'
    with cd(code_dir):
        with settings(warn_only=True):
            result = local("git pull", capture=True)
    if result.failed:
        abort("Aborting asdasds")

def pull2():
    local("git pull")

def deneme():
    commit()
    test()
    push()

def deploy():
    with cd('/home/vokaladmin/DjangoProjects/fabrictest'):
        with settings(warn_only=True):
            local('git reset --soft HEAD')
            local('git pull origin master')
            local('git add -A')
            commit = local('git commit -a -m "Latest Selenium screenshots for .."')
            if commit.failed:
                print 'Nothing to commit, exiting...'
                sys.exit(0)
            else:
                local('git push -u origin master')