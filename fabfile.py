from fabric.api import local

def pull():
    local('git pull')