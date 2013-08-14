# Run this like fab -R www deploy

from fabric.api import *

REPO_URL     = 'https://github.com/deron17/deron.git'
PROJECT_DIR  = '/home/vokaladmin/DjangoProjects/fabrictest'
PROJECT_NAME = 'projectname'
SERVER_NAME  = 'projectname.servername' # I use gunicorn, so i have projectname.gunicorn

env.roledefs['www'] = ['www1.example.com']

# For ZSH Uncomment this line
#env.shell = '/usr/bin/env zsh -i -c'

env.hosts = 'http://127.0.0.1:8000/'
env.user = 'vokaladmin'
env.password = 'vokal106'


def pull():
    with cd(PROJECT_DIR):
        run('git pull')

def install_packages():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('pip install -r requirements.txt')

def sync_database():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('./manage.py syncdb --noinput')

def migrate_database():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('./manage.py migrate --noinput')

def stop_server():
    run('supervisorctl stop %s' % SERVER_NAME)

def start_server():
    run('supervisorctl start %s' % SERVER_NAME)

def restart_server():
    stop_server()
    start_server()

def collect_static():
    with cd(PROJECT_DIR):
        with prefix('workon %s' % PROJECT_NAME):
            run('./manage.py collectstatic --noinput')

def deploy():
    with settings(hide('stdout'), warn_only=True):
        pull()
        install_packages()
        sync_database()
        migrate_database()
        collect_static()
        restart_server()

#logging.getLogger("paramiko").setLevel(logging.DEBUG)