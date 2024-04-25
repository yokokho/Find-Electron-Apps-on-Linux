import os

def is_electron_app(directory):
    for file in os.listdir(directory):
        if file.endswith('.asar') or file == 'LICENSE.electron.txt':
            return True
    return False

def get_app_name(directory):
    split_directory = directory.split('/')
    if directory.startswith('/usr/share/'):
        if len(split_directory) > 3:
            return split_directory[3]
    elif directory.startswith('/opt/'):
        if len(split_directory) > 2:
            return split_directory[2]
    elif directory.startswith('/home/'):
        if len(split_directory) > 4:
            return split_directory[4]
    else:
        return os.path.basename(directory)


def find_electron_apps():
    directories_to_search = ['/opt', '/usr/share', '/home']
    electron_apps = []

    for directory in directories_to_search:
        for root, dirs, files in os.walk(directory):
            if is_electron_app(root):
                app_name = get_app_name(root)
                electron_apps.append((app_name, root))
                dirs[:] = []

    if electron_apps:
        print("_" * 100)
        print(f"{'App Name':30s} {'Location'}")
        print("=" * 100)
        for app_name, location in electron_apps:
            print(f"{app_name:30s} {location}")
    else:
        print("Electron-based applications not found.")

if __name__ == "__main__":
    find_electron_apps()
