import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\umesh\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_camera():
    """ Open Camera using subprocess module to run the command """
    sp.run('start microsoft.windows.camera:', shell=True)


def open_path(app):
    """
    If the application name is present in paths list then it will open it
    Returns:
        bool: application opened or not
    """
    if app in paths.keys():
        try:
            os.startfile(paths[app])
        except Exception as e:
            print(e)
            return False
        return True

    return False


def open_cmd():
    os.system('start cmd')
