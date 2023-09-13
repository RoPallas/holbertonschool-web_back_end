#!/usr/bin/env python3
""" Lists documents in a collection """


def list_all(mongo_collection):
    """
    Lists documents in a collection
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find()
