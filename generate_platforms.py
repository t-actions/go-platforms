#!/usr/bin/env python3
import os
import json
import logging
import subprocess

def main():
    platforms = os.getenv('PLATFORMS')
    if not platforms:
        platforms = subprocess.check_output('go tool dist list', shell = True).decode('utf-8')
    matrix = {
        'include': []
    }
    for platform in platforms.strip().split():
        parts = platform.split('/')
        if len(parts) < 2:
            logging.warn(f'[Skip] Unknown platform format {platform}')

        goos = parts[0]
        goarch = parts[1]
        goarm = parts[2] if len(parts) > 2 else ''

        if goarch != 'arm':
            goarms = ['']
        elif goarm == '':
            goarms = ['7', '6', '5']
        else:
            goarms = [goarm]
        
        for goarm in goarms:
            matrix['include'].append({
                'goos': goos,
                'goarch': goarch,
                'goarm': goarm,
            })

    print(json.dumps(matrix))

if __name__ == '__main__':
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
        datefmt = '%Y-%m-%d %X',
    )
    main()