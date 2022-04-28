import socket
import os
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class LoginError(Exception):
    """Raised when login bad :(((((((((((("""

class FileAlreadyExists(Exception):
    """Raised when file already exists"""

class FileNotFoundError(Exception):
    """Raised when a particular file doesnt exist :(((((((((("""

class InvalidDirectory(Exception):
    """Raised when a directory is invalid"""


def login(username, password):
    s.connect(("192.168.0.150", 42069))
    s.send(bytes(f"{username}.{password}",'utf-8'))

    confirmation = s.recv(1024)
    confirmation = confirmation.decode('utf-8')

    if confirmation == 'INVALID':
        raise LoginError("Invalid Username or Password")

    if confirmation == 'TRUE':
        pass
    return



def send_file(file):
    s.send(bytes('SEND_FILE','utf-8'))

    filepath = file
    filename = os.path.basename(filepath)

    s.send(bytes(filename,'utf-8'))

    confirmation2 = s.recv(1024)
    confirmation2 = confirmation2.decode('utf-8')

    if confirmation2 == 'FILE_EXISTS':
        raise FileAlreadyExists(f"{filename} already exists")
    if confirmation2 == 'CONTINUE':
        pass

    f = open(filepath, "rb")
    data = f.read(1024)

    while data:
        s.send(data)
        data = f.read(1024)
        
    f.close()
    return file
    
def get_link(file):
    print('This feature has not yet been developed')


def search_file(file):
    s.send(bytes('SEARCH_FILE','utf-8'))

    s.send(bytes(file,'utf-8'))

    confirmation = s.recv(1024)
    confirmation = confirmation.decode('utf-8')

    if confirmation == 'TRUE':
        return True

    if confirmation == 'FALSE':
        return False

def get_files():
    s.send(bytes('GET_FILES','utf-8'))

    files = s.recv(1024)
    files = pickle.loads(files)

    return files


def download(file, dir):
    if not os.path.exists(dir):
        raise InvalidDirectory("The directory provided is invalid")

    if os.path.exists(dir):
        pass

    s.send(bytes('DOWNLOAD','utf-8'))
    s.send(bytes(file,'utf-8'))

    confirmation = s.recv(1024)
    confirmation = confirmation.decode('utf-8')

    if confirmation == 'FALSE':
        raise FileNotFoundError("File Doesnt exist")

    if confirmation == 'TRUE':
        f = open(f"{dir}\\{file}",'wb')

        while True:
            l = s.recv(1024)
            if not l:
                f.close()
                break 

            f.write(l)
            
    return file




def rename_file(old_name, new_name):
    s.send(bytes('RENAME','utf-8'))
    s.send(bytes(f"{old_name},{new_name}",'utf-8'))

    confirmation = s.recv(1024)
    confirmation = confirmation.decode('utf-8')

    if confirmation == 'FALSE':
        raise FileNotFoundError("File Doesnt exist")

    if confirmation == 'TRUE':
        return True