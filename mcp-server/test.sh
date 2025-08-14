#!/bin/bash

#curl --noproxy '*'  "http://localhost:8080/sse" \
#  -H "Content-Type: application/json"



curl --noproxy '*' -X POST "http://localhost:8080/mcp/message?sessionId=6d2fbf4a-e764-41c2-b321-8a1c9afb2501" \
   -H "Content-Type: application/json" \
   -d '{
         "jsonrpc": "2.0",
         "id": 1,
         "method": "initialize",
         "params": {
           "protocolVersion": "2025-03-26",
           "capabilities": {
             "roots": {
               "listChanged": true
             },
             "sampling": {}
           },
           "clientInfo": {
             "name": "ExampleClient",
             "version": "1.0.0"
           }
         }
       }'
