#!/usr/bin/env python3
"""
Provides stats about Nginx
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    print("{} logs".format(logs_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(
            method, logs_collection.count_documents({"method": method})))
    print("{} status check".format(
        logs_collection.count_documents({"method": "GET", "path": "/status"})))
