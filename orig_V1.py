import socket
import sys
from sys import path
import traceback
import os
from pathlib import Path

def response_ok(body=b"This is a minimal response", mimetype=b"text/plain"):
    """ returns a basic HTTP response """
    return b"\r\n".join([
        b"HTTP/1.1 200 OK",
        b"Content-Type: " + mimetype,
        b"",
        body
    ])
def response_method_not_allowed():
    """Returns a 405 Method Not Allowed response"""
    return b"\r\n".join([
        b"HTTP/1.1 405 NOT Allowed",
        b"",
        b"405 Please take your POST and HEAD requests elsewhere"
    ])
def response_not_found():
    """Returns a 404 Not Found response"""
    return b"\r\n".join([
        b"HTTP/1.1 404 Not Found",
        b"",
        b"404 We have no idea what you're on about"
    ])

def parse_request(request):
    """ returns the path of the HTTP request.    """
    method, path, version = request.split("\r\n")[0].split(" ")

    if method != "GET":
        raise NotImplementedError

    return path

def response_path(path):
    """    This method should return appropriate content and a mime type. 
    TOOD:
    get mime types aligned
    make PNG work
       """

    content = ''
    try:
        if path == '/':
            content = "{0}".format('\n'.join([x for x in os.listdir('.\\webroot')]))
        else:
            file = open(Path.cwd().joinpath('webroot',path[1:]))
            content = file.read()
            file.close()
    except FileNotFoundError: 
        raise NameError
        '''
        #this seems weird to have an error raise an error, but I'm following the todo 
        form line 116 in the instructions 'If response_path raised # a NameError, then 
        let response be a not_found response.'
        '''
    mime_type = ""
    file_ext = path.split(".")
    file_type = ''.join(file_ext[-1:])

    if file_type == 'html':
        mime_type == "text/html"
    if file_type == 'txt':
        mime_type == "text/plain"
    if file_type == 'png':
        mime_type == "image/apng"
    if file_type == "jpeg":
        mime_type == "image/jpeg"
    else:
        mime_type == "text/plain"

    mime_type = mime_type.encode()
    content = content.encode()

    return content, mime_type


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    sock.listen(1)

    try:
        while True:
            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()  # blocking
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                request = ''
                while True:
                    data = conn.recv(1024)
                    request += data.decode('utf8')

                    if '\r\n\r\n' in request:
                        break
		
                print("Request received:\n{}\n\n".format(request))

                try:
                    path = parse_request(request)
                    # https://stackoverflow.com/questions/15710515/python-3-bytes-formatting
                    # "{0}".format('\n'.join([x for x in os.listdir('.\\webroot')])).encode()
                    response = response_ok(
                        response_path(path)[0],
                        response_path(path)[1]
                    )
                except NotImplementedError:
                    response = response_method_not_allowed()
                except NameError:
                    response = response_not_found()

                conn.sendall(response)
            except:
                traceback.print_exc()
            finally:
                conn.close() 

    except KeyboardInterrupt:
        sock.close()
        return
    except:
        traceback.print_exc()


if __name__ == '__main__':
    server()
    sys.exit(0)