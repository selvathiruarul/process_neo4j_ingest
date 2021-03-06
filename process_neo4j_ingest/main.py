#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project process_neo4j_ingest
   Created by selva on 2/19/18.
"""

from neo4j_connect import Neo4j_Connect

import os
import logging
import configparser
from neo4j import exceptions

log_format = "%(funcName)s():%(lineno)i: %(message)s %(levelname)s"

logging.basicConfig(level=logging.INFO, format=log_format)
log = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
config = configparser.RawConfigParser()
config.read(os.path.join(BASE_DIR, 'resources/properties.ini'))
properties = dict(config.items('process_neo4j_ingest'))

URI = properties['uri']
FILE_NAME = properties['file_name']
USERNAME = properties['neo4j_username']
PASSWORD = os.environ.get('NEO4J_PASSWORD')


def read_query(file_name):
    """
    Method to read the query file
    :param file_name: 
    :return: 
    """

    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name) as file_object:
            queries = file_object.readlines()
            for query in queries:
                yield query.strip()
    else:
        raise FileNotFoundError

def get_connection():
    """
    Method to acquire db connection
    :return: 
    """
    try:
        neo4j_connector = Neo4j_Connect(URI, USERNAME, PASSWORD)
        return neo4j_connector
    except exceptions.AuthError as exception:
        log.exception(exception)
    except exceptions.AddressError as exception:
        log.exception(exception)


def load_data(file_name):
    """
    Method to load data into db
    :param file_name: 
    :return: 
    """
    try:
        neo4j_connector = get_connection()
        if neo4j_connector:
            neo4j_driver = neo4j_connector.get_drive()
            with neo4j_driver.session() as session:

                for query in read_query(file_name):
                    log.info("Executing.. {query}".format(query=query))
                    result = session.run(query)
                    log.info("Completed {status}".format(status=result))

                log.exception("File Not Found")
            neo4j_connector.close()
    except exceptions.CypherError as exception:
        log.exception(exception)
        exit(1)
    except FileNotFoundError as exception:
        log.exception(exception)
        exit(1)
if __name__ == '__main__':
    load_data(os.path.join(BASE_DIR, FILE_NAME))
