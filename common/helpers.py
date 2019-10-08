import os
import sys
import random
import numpy as np
from datetime import datetime, timedelta

def create_logs(directory='logs', file_prefix='log_', n_lines=1000, n_files=100):
    """
    Creates sample logs for Spark.
    
    Log Format: {DATE} - {LOGGER} - {LOGLEVEL} - {MESSAGE}
    
    Args:
        directory (str): defines directory where logs are stored
        file_prefix (str): log filename prefix
        n_file (int): number of files to be created
    """
    
    LOGLEVELS = ['INFO', 'DEBUG', 'WARNING', 'ERROR']
    LOGGERS = ['LOGGER1', 'LOGGER2', 'HTTPLOGGER']
    
    START_DATE = datetime(2019, 1, 1)
    
    ip_addresses = get_random_ip_addresses()
    url_endpoints = get_random_urls()
    
    for idx in range(1, n_files + 1):
        date_string = (START_DATE + timedelta(days=idx)).strftime('%m-%d-%Y:%H:%M:%S')
        file_path = os.path.join(directory, file_prefix + str(idx) + '.log')
        print('Creating File: %s @ %s' % (file_path, date_string))
        
        log_data = ['%s - %s - %s - action="request" - %s - %s' % (date_string, 
                                                                   random.choice(LOGGERS),
                                                                   random.choice(LOGLEVELS),
                                                                   random.choice(ip_addresses),
                                                                   random.choice(ip_addresses),
                                                                  ) for _ in range(n_lines)]
        with open(file_path, 'w+') as outfile:
            outfile.writelines(log_data)
    
def get_random_ip_addresses(size=200):
    """
    Create random ip addresses.

    Args:
        size (int): number of ip addresses to be created.
    """
    ipv4_1 = np.char.array(np.random.randint(1, 255, size=size))
    ipv4_2 = np.char.array(np.random.randint(1, 255, size=size))
    ipv4_3 = np.char.array(np.random.randint(1, 255, size=size))

    ip_addresses = (ipv4_1 + b'.' + ipv4_2 + b'.' + ipv4_3).astype(str).\
                    tolist()
    
    return ip_addresses

def get_random_urls(prefix='http://www.example-shop.com/product/', size=1000, start_index=None):
    """
    Create random url endpoints.

    Args:
        size (int): number of urls to be created.
        start_index (int): optional argument for starting number.
    """
    
    if not start_index:
        start_index = 1     
    end_index = start_index + size
    
    urls = [prefix + str(url_suffix) for url_suffix in range(start_index, end_index + 1)] 

    return urls