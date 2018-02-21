from process_neo4j_ingest.neo4j_connect import Neo4j_Connect
import pytest
from neo4j import exceptions

def test_read_query():
    with pytest.raises(exceptions.AuthError):
        neo4j_object=Neo4j_Connect('bolt://im-interview-test-p3jd74h.clearlinkdata.com:7687','neo4j','neo4j')
    with pytest.raises(exceptions.AddressError):
        neo4j_object=Neo4j_Connect('bolt://m-interview-test-p3jd74h.clearlinkdata.com:7687','neo4j','neo4j')
