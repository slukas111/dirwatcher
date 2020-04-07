__author__="Sasha Lukas + demo"

import logging 
import datetime
import time
import argparse
import os

logger = logging.getLogger(__file__)
exit_flag = False

def watch_directory(args):
    watching_files = {}
    logger.info('Watching directory: {}, File Ext: {}, Polling Interval: {}, Magic Text: {}'.format(
    args.path, args.ext, args.interval, args.magic 
    ))

    # Keys are the actual filename and the values are where to begin searching.

    # Look at directory and get a list of files from it.
    # Add these to dictonary if not already present, and log it as a new file.
    
    # Look through your "watching_files" dictonary
    # and compare that to a list of files that are in the dictonary.
    
    # If the file is not in your dictonary anymore you have
    # to log the file and remove it from your dictonary

    # Iterate through dictonary, open each file at the last line you read from, 
    # Start reading from that point looking for any "magic" text
    
    # Update the last position that you read from in the dictionary  
    
    while True: 
        try:
            logger.info('Inside Watch Loop')
            time.sleep(args.interval)
        except KeyboardInterrupt:
            break

def create_parser():
    """Creates parser and sets up commandline options"""
    parser = argparse.ArgumentParser(description="Watch directory for change")
    parser.add_argument('-e', '--ext', type=str, default='.txt',
                        help='Text file extension to watch') 
    parser.add_argument('-i', '--interval', type=float,
                        default=1.0, help='Number of seconds between polling')
    parser.add_argument('path', help='Directory path to watch')
    parser.add_argument('magic', help='String to watch for')
    return parser


def main():
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s [%(threadname)-12s] %(message)s', 
        datefmt='%Y-%m-%d %H:%M:S%'
    )
    logger.setLevel(logging.DEBUG)
    app_start_time = datetime.datetime.now()
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Running {0}\n'
        '    Started on {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, app_start_time.isoformat())    
)
    parser = create_parser()
    args = parser.parse_args()

    while not exit_flag:
        try:
            watch_directory(args)
        except OSError:
            logger.error('{} directory does not exist'.format(args.path))
            time.sleep(args.interval*2)
        except Exception as e:
            logger.error('Unhandled exception: {}'.format(e))
        time.sleep(args.interval)
    uptime = datetime.datetime.now()-app_start_time
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Stopped {0}\n'
        '    Uptime was {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, str(uptime))    
    )
    logging.shutdown()

if __name__ == '__main__':
    main()