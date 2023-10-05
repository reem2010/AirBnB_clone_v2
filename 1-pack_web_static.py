#!/usr/bin/python3
"""script that generates a .tgz archive"""
from fabric.api import task, local
import datetime


@task
def do_pack():
    """generates a .tgz archive"""
    local("mkdir -p versions")
    time = datetime.datetime.now()
    file_code = f"{time.year}{time.month}{time.day}{time.hour}"
    file_code = file_code + f"{time.minute}{time.second}"
    local(f"tar -cvzf versions/web_static_{file_code}.tgz web_static")
    path = local(f"pwd web_static_{file_code}.tgz", capture=True)
    return (path)
