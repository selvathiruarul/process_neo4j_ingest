#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project process_neo4j_ingest
   Created by selva on 2/19/18.
"""


from process_neo4j_ingest import neo4j_connect

URI='bolt://im-interview-test-p3jd74h.clearlinkdata.com:7687'
USERNAME='neo4j'
PASSWORD="UT5p&>'`t4"

neo4j_object=neo4j_connect.Neo4j_Connect(URI, USERNAME, PASSWORD)

neo4j_driver=neo4j_object.get_drive()

query="USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM 'file:/home/selva/IdeaProjects/process_neo4j_ingest/process_neo4j_ingest/resources/moc.data' as line FIELDTERMINATOR '\t' MERGE (cid:cid {id:line.oid}) MERGE (oid:oid {id :line.cid}) MERGE (oid)<-[:related]-(cid)"

with neo4j_driver.session() as session:
    session.run(query)
