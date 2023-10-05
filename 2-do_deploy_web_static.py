#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import task, run, put, env
import os


env.hosts = ['34.205.65.92', '52.205.76.119']
env.user = 'ubuntu'


@task
def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split()[-1][:-4]
    try:
        put(archive_path, '/tmp/')
        run(f"mkdir -p /data/web_static/releases/{file_name}/")
        direct = f"/data/web_static/releases/{file_name}/"
        run(f"tar -xzf /tmp/{archive_path} -C {direct}")
        run(f"rm /tmp{archive_path}")
        run("rm -rf /data/web_static/current")
        sym = "/data/web_static/current"
        run("ln -s /data/web_static/releases/{file_name}/ {sym}")
        return True
    except Exception:
        return False
