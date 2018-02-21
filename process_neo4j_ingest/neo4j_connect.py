#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project process_neo4j_ingest
   Created by selva on 2/19/18.
"""

from neo4j.v1 import GraphDatabase


class Neo4j_Connect(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

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
