#!/usr/bin/env python3
"""
Inserts a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document in a collection
    """
    if mongo_collection is None:
        return None
    new_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_id
