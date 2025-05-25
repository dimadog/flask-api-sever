#!/bin/bash
curl 'http://127.0.0.1:5000/data' \
     -X POST \
     -H "Content-Type: application/json" \
     -u admin:secret \
     -d '{ "number" : 123 }'
     
