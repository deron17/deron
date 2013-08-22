from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm
import sys

code_dir = '/home/vokaladmin/DjangoProjects/fabrictest'

def selenium():
    with settings(warn_only=True):
        result = local('python loginandlike.py', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")
    else:
        print 'test is completed successfully!'

def test():
    local('python login.py')

def status():
    local('git status')

def commit():
    local("git add . && git commit -m 'aasd'")

def push():
    local("git push origin master")

def pull():
    with cd(code_dir):
        with settings(warn_only=True):
            result = local("git pull origin master")
    if result.failed:
        abort("Aborting")

def pull2():
    local("git pull origin master")

def deneme():
    commit()
    test()
    push()

def deploy():
    with cd(code_dir):
        with settings(warn_only=True):
            local('git reset --soft HEAD')
            local('git pull origin master')
            local('git add -A')
            commit = local('git commit -a -m "it is a automatic commit .."')
            if commit.failed:
                print 'Nothing to commit, exiting...'
                sys.exit(0)
            else:
                local('git push -u origin master')


def startprocess():
    pull()
    selenium()
    push()
