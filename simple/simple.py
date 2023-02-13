
import argparse
import socket
import sys

def simple():
    print("Hello, World!")

def validate(args: argparse.Namespace) -> bool:
    if args.hostname == None:
        return False

    # TODO(sneha): validate this is something to make a tcp connectiont o 

    # Check valid port range for python
    if args.port is not None:
        if args.port > 65535 and args.port < 1:
            return False
    
    return True

if __name__ == '__main__':
    # Use setup.py to setup package/module as script -> https://pybit.es/articles/how-to-package-and-deploy-cli-apps/
    # TODO(fix packagin issue)

    # CLI tool - accept command line arguments - get endpoint we are scanning
    parser = argparse.ArgumentParser()

    parser.add_argument("-hn", "--hostname", help="hostname", type=str)
    parser.add_argument("-p", "--port", help="port. If empty, will scan all possible ports", type=int)
   
    # TODO(sneha): Concurrency argument to see how many async calls or workers we use
    # parser.add_argument("-c", "--password", help="Password")

    args = parser.parse_args()

    # Validate the arguments
    if validate(args) is False: 
        print("Invalid arguments", file=sys.stderr)
        exit()
    
    # Try opening socket and seeing if open 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.setsockopt( socket.SOL_SOCKET, 
                     socket.SO_REUSEADDR, 1)
    server_address = (args.hostname, args.port)

    try:
        sock.connect(server_address)
        print("here")
    except Exception as msg:
        print(f"Connection is closed on port {args.port}: {msg}")
    else: 
        print(f"Closing connection on port {args.port}")
        sock.close()

    print("trying this a second time")
    # TODO(Sneha): I don't think we can reuse a socket - need to open a new socket 
    try:
        sock.connect(server_address)
        print("here")
    except Exception as msg:
        print(f"Connection is closed on port {args.port}: {msg}")
    else: 
        print(f"Closing connection on port {args.port}")
        sock.close()


    # iterate through range of allowable ports and determine what is open vs. closed 

    # return result/print list 

    ## NEXT STEP - use async calls to do this asynchronously or multiple processes 

    simple()

