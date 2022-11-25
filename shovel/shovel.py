import os
import subprocess
import sys
import time

import django
from django.conf import settings
from django.core import management

from shovel import task

base_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "djangorestblog")
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# def _load_setting():
#     if not settings.configured:
#         django.setup()


def _wait_for_dependency(dependency, port, wait_time):
    wait_time = int(wait_time)
    while subprocess.run(
        ["nc", "-z", dependency, port], stdout=subprocess.PIPE
    ).returncode:
        print(f"{dependency} is not accepting connection, waiting...")
        time.sleep(wait_time)
    print(f"{dependency} is ready to accept connections")


def _migrate():
    print("Appying migrations...")
    # management.call_command("migrate", interactive=False)
    # os.chdir('djangorestblog')
    # while subprocess.run(["python","manage.py","migrate"]).returncode:
    # print("@@##@@")
    # while subprocess.run(["cd",".."]).returncode:
    #     print("..")
    os.system("python manage.py migrate")
    # os.chdir('..')


def _make_tests():
    os.system("pytest")


def _load_seed_blob():
    print("Loading data...")
    # management.call_command("seed_blob")
    # os.chdir('djangorestblog')
    os.system("python manage.py seed_blog")
    # os.chdir('..')


@task
def test_run_shovel():
    print("test")


@task
def run_api_dev(port=8000, dependency=None, dbport="5432", wait_time="3"):
    # _load_setting()
    if dependency:
        _wait_for_dependency(dependency, dbport, wait_time)
    os.chdir("djangorestblog")
    _make_tests()
    _migrate()
    _load_seed_blob()

    os.system("python manage.py runserver 0.0.0.0:8000")
