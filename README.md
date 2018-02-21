# proces_neo4j_ingest [![Build Status](https://travis-ci.org/selvathiruarul/process_twitter_visualize.svg?branch=master)](https://travis-ci.org/selvathiruarul/process_neo4j_ingest)

## Description
Python process to ingest data into Neo4j database and find answers for following questions

1) How many rid nodes are there with no edges?
2) How many cid nodes have more than one edge to an oid node?
3) Are there any rid nodes with multiple cid nodes? If so, what percent?


# THINGS TO CONSIDER

- Relationship between order/customer and request/customer is considered as ordered and by, since no other attributes are available to differentiate the relation
- Edges will change depending on the uniqueness of relationship
- Input file is loaded from AWS S3 since access to import location server is not available.It can be changed depending on the input location

## Requirements:
    -Neo4j
    -Python3
    -neo4j.v1
## Set Environment variables
    -file_name = 
    -uri = 
    -neo4j_username=

## pyest
    pytest

## To Run:
    python3 ./process_neo_4j_ingest/main.py

## PLAN

![PLAN](./process_neo4j_ingest/resources/plan.jpg)
    
    
## SAMPLE
![SAMPLE](./process_neo4j_ingest/resources/sample.png)
    
## ANSWERS

1) How many rid nodes are there with no edges?

All the (Request)RID nodes are connected with (contact)CID nodes at least once. 

```
OPTIONAL MATCH (request)-[relation:by]->(contact) WHERE relation is null RETURN count(request) as total
```
|TOTAL|
|-----|
| 0   |
|     |

2) How many cid nodes have more than one edge to an oid node?

Number of distinct CID nodes connected to an OID node

```
MATCH (contact)-[r:ordered]->(order) WITH contact, order,count(r) as rel_cnt WHERE rel_cnt > 1 RETURN count(DISTINCT contact) as total

```
|TOTAL|
|-----|
| 795 |
|     |



3) Are there any rid nodes with multiple cid nodes? If so, what percent?

Percentage of RID nodes connected with at least two CID nodes

```
MATCH (contact)<-[k:by]-(request) with count(distinct request) as total MATCH (contact)<-[k:by]-(request) with total,request,count(distinct contact) as cus where cus>1 return round(toFloat(count(cus))/toFloat(total)*100*100)/100 as percentage
```

|PERCENTAGE|
|----------|
|  3.75    |
|          |





Contribute and Grow
-------------------
1. Fork your repo
2. Contribute and raise PR
3. Let other review

|========================|
|       Team 3S          | 
|========================|