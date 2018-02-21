#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project process_neo4j_ingest
   Created by selva on 2/19/18.
"""

from neo4j.v1 import GraphDatabase
from neo4j import exceptions
import logging
log_format = "%(funcName)s():%(lineno)i: %(message)s %(levelname)s"
logging.basicConfig(level=logging.INFO, format=log_format)
log = logging.getLogger(__name__)

class Neo4j_Connect(object):

    def __init__(self, uri, user, password):
        try:
            self._driver = GraphDatabase.driver(uri, auth=(user, password))
        except exceptions.AuthError:
            raise exceptions.AuthError
        except exceptions.AddressError:
            raise  exceptions.AddressError

    def close(self):
        """
        Method to close db connection
        :return: 
        """
        self._driver.close()

    def get_drive(self):
        """
        Mwthod to get db driver
        :return: 
        """
        return self._driver
