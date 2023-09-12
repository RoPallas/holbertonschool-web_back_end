#!/usr/bin/env python3
"""
Returns the list of school for specific topic
"""
from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List:
    """
    Returns the list of school for specific topic
    """
    if mongo_collection is None:
        return None
    return mongo_collection.find({"topics": topic})
