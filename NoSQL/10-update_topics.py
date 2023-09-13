#!/usr/bin/env python3
"""
Changes topics of a school document
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List):
    """
    Changes topics of a school document
    """
    if mongo_collection is None:
        return None
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
