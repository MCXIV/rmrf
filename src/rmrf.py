# -*- coding: utf-8 -*-
# --------------------------------------------------
# ????
# MCXIV, 202x
# --------------------------------------------------
# Built-in
import os
import shutil
import time
import sys
import glob
import multiprocessing as mp

# 3rd party
from rich import print as rprint

# --------------------------------------------------

TEMP_FOLDER = 'rmrftmp/'


def delete_after_timeout(timeout=10):
    """
    It deletes the temporary folder after a certain amount of time

    :param timeout: The amount of time to wait before deleting the files, defaults to 10 (optional)
                    It can be changed by setting the environment variable RMRF_TIMEOUT  
    """

    if os.environ.get('RMRF_TIMEOUT'):
        timeout = int(os.environ.get('RMRF_TIMEOUT'))
        if timeout < 0:
            rprint(
                '[bold red]Haha, a negative timeout, nice try you fucking twat. Cheh, I deleted your files. [/bold red]')
            timeout = 0
    time.sleep(timeout)
    shutil.rmtree(TEMP_FOLDER)


def safe_rmrf() -> None:
    """
    It moves the files to a temporary folder and deletes them after 10 seconds (Default)
    It doesn't delete the files if the user sends an other command 'rmundo'.
    """

    path = [sys.argv[i] for i in range(1, len(sys.argv))]
    if not path or path == ['.']:
        path = glob.glob('*')
    if path == ['..']:
        path = glob.glob('../*')
    for element in path:
        if not os.path.exists(element):
            rprint(f'[bold red]No such file or directory: {element}[/bold red]')
            os._exit(1)

    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)

    for file in path:
        if os.path.exists(file):
            if os.path.isdir(file):
                shutil.move(file, TEMP_FOLDER)
            elif os.path.isfile(file):
                shutil.move(file, TEMP_FOLDER)
        open(f'{TEMP_FOLDER}PATH', 'a').write(file+'\n')

    mp.Process(target=delete_after_timeout).start()
    os._exit(0)


def undo_rmrf():
    """
    It restores the deleted files.
    """

    if os.path.exists(TEMP_FOLDER):
        previousPath = sorted(open(f'{TEMP_FOLDER}PATH', 'r').readlines())
        listFiles = sorted(f for f in glob.glob(f'{TEMP_FOLDER}/*') if f != f'{TEMP_FOLDER}PATH')

        for i in range(len(previousPath)):
            previousPath[i] = previousPath[i].replace('\n', '')
            shutil.move(listFiles[i], previousPath[i])
        rprint(f'[bold green]Restored {previousPath}[/bold green]')
    else:
        rprint('[bold red]Nothing to restore[/bold red]')
