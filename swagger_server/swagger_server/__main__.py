#!/usr/bin/env python3
import subprocess
import os
import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Video Website'})
    # print(subprocess.run(['ps', '-a'], stdout=subprocess.PIPE))
    print(subprocess.call(['vlc', '/home/toad/Videos/Anne Sylvestre/01 - Les moulins Baptiste.mp3'], stdout=subprocess.PIPE))
    app.run(port=8080)


if __name__ == '__main__':
    main()
