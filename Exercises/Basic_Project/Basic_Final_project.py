import argparse
import os
import shutil
import datetime
import pathlib


def setup():
    parser = argparse.ArgumentParser(description="Command Line Interface")
    parser.add_argument("--ls", type=str, nargs="?", const="", help="Show list of things in Directory")
    parser.add_argument("--cd", type=str, nargs="?", const="", help="Change the current working directory")
    parser.add_argument("--mkdir", type=str,nargs = 2, help="Take name of directory to create")
    parser.add_argument('--rmdir', type=str, help="Take name of directory to remove")
    parser.add_argument("--rm", type=str, help="Remove file with the given name")
    parser.add_argument("--rmr", type=str, help="Remove directory and its contents")
    parser.add_argument("--cp", type=str, nargs=2, help="Copy a file or directory (source and destination)")
    parser.add_argument("--mv", type=str, nargs=2, help="Move a file or directory (source and destination)")
    parser.add_argument("--find", type=str, nargs=2, help="Search file or directory matches pattern starting from path")
    parser.add_argument("--cat", type=str, help="Output the contents of the file")
    parser.add_argument('--log', action="store_true", help="Show logs of user actions")
    return parser


def log_command(cmd):
    with open("history.log", 'a') as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        text = f'{cmd} : {time_now}\n'
        file.write(text)


def show_log(file_name="history.log"):
    with open(file_name, "r") as file1:
        data = file1.read()
    print(data)


def ls(path):
    if not path:
        path = pathlib.Path.home()
    if os.path.exists(path):
        print(f"Contents of {path}:")
        for item in os.listdir(path):
            print(item)
    else:
        print(f"Path '{path}' does not exist.")
def mk_dir(path,name):
    dir_path = os.path.join(path, name)
    if os.path.exists(dir_path):
        print(f"The directory '{name}' already exists in '{path}'.")
    else:
        os.mkdir(dir_path)
        print(f"Directory '{name}' has been added to '{path}'.")




def cd(path, current_dir):
    if path == "home":
        new_path = pathlib.Path.home()
    elif path == "..":
        new_path = os.path.dirname(current_dir)
    elif not path:
        new_path = current_dir
    elif path ==".":
        new_path = pathlib.Path.home()
    else:
        new_path = path

    if os.path.exists(new_path):
        os.chdir(new_path)
        print(f"Changed directory to: {os.getcwd()}")
    else:
        print(f"Path '{path}' does not exist.")
    return os.getcwd()


def rm_dir(path):
    if os.path.exists(path):
        os.rmdir(path)
        print(f'{path} is removed from PC')
    else:
        print(f'file does not exist')
def remove_f(current_dir,name):
    lis_path = os.listdir(current_dir)
    if name in lis_path:
        file_path = os.path.join(current_dir,name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f'file is removed')
        else:
            print(f'{file_path} is not file')
    else:
        print(f'{name} is not exist')

def rem_all(current_dir,name):
    list_path = os.listdir(current_dir)
    if name in list_path:
        dir_path = os.path.join(current_dir,name)
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            print(f'{dir_path} is removed Successfully!!')
        else:
            print(f'{dir_path} is not folder and we can not remove this (please use --rm)')
    else:
        print(f'this folder is not exist in this path')

def cpy(src, dst):
    if os.path.abspath(src) == os.path.abspath(dst):
        base_name = os.path.basename(src)
        parent_dir = os.path.dirname(dst)
        new_name = f"{base_name}(1)"
        dst = os.path.join(parent_dir, new_name)


    if os.path.isfile(src):
        shutil.copy(src, dst)
    elif os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        print(f"Source {src} does not exist.")

def move(src,dst):
    if os.path.abspath(src) == os.path.abspath(dst):
        print(f'It is our file(foldeer) current path')
    elif os.path.exists(src) and os.path.exists(dst):
        shutil.move(src,dst)
    else:
        print(f'path is not exist')

def find(path, format):
    match = []
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if format.lower() == os.path.splitext(file)[1].lower():
                    match.append(os.path.join(file))
    else:
        print(f'No such directory: {path}')
        return
    if match:
        for name in match:
            print(name)
    else:
        print(f'No files found with "{format}" format')

def contents(path):
    if os.path.exists(path):
        with open(path ,'r') as cont:
            res = cont.read()
            print(res)
    else:
        print(f'File Does not exist')




def main():
    current_dir = os.getcwd()
    print(f"Starting in directory: {current_dir}")

    while True:
        parser = setup()
        user_input = input(f"({current_dir}) $ ")
        log_command(user_input)
        args = parser.parse_args(user_input.split())


        if args.ls is not None:
            ls(args.ls or current_dir)

        if args.cd is not None:
            current_dir = cd(args.cd, current_dir)

        if args.log :
            show_log()
        if args.mkdir:
            mk_dir(args.mkdir[0] , args.mkdir[1])
        if args.rmdir:
            rm_dir(args.rmdir)
        if args.rm:
            remove_f(current_dir,args.rm)
        if args.rmr:
            rem_all(current_dir,args.rmr)
        if args.cp:
            cpy(args.cp[0],args.cp[1])
        if args.mv:
            move(args.mv[0],args.mv[1])
        if args.find:
            find(args.find[0],args.find[1])
        if args.cat:
            contents(args.cat)
        if args == "exit":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
