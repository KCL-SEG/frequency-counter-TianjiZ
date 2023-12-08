"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        # Convert item to string and use the get method to simplify the counting logic
        key = str(item)
        frequencies[key] = frequencies.get(key, 0) + 1
    return frequencies
