#!/usr/bin/env python

"""
Simple FTP server (read-only for anonymous users).

Usage:
$ python ftp.py [-u <username> -p <password>] [-P <port:21>]
"""

import argparse

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main(args):
    """Application entry point."""

    authorizer = DummyAuthorizer()

    if args.username:
         authorizer.add_user(args.username, args.password, '.', 'elradfmwM')
    else:
        authorizer.add_anonymous('.')

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(('0.0.0.0', args.port), handler)
    server.serve_forever()


def parse_args():
    """Parse command line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', dest='username')
    parser.add_argument('-p', dest='password')
    parser.add_argument('-P', dest='port', type=int, default=21)

    args = parser.parse_args()

    if bool(args.username) ^ bool(args.password):
        raise Exception('username and password required both or neither')

    return args


if __name__ == '__main__':
    try:
        main(parse_args())
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        print ex
