#!/usr/bin/env python3
"""
Caching request module
"""

import requests
import redis
import time
from functools import wraps
from typing import Callable

# Dictionary to store cached responses
cache = {}

# Decorator to implement caching with a given expiration time
def cache_response(expiration_time=10):
    def decorator(func):
        def wrapper(url):
            # Check if the URL is in the cache and not expired
            if url in cache and time.time() - cache[url]["timestamp"] < expiration_time:
                print(f"Using cached content for {url}")
                cache[url]["count"] += 1
                return cache[url]["content"]
            else:
                content = func(url)
                # Update cache with new content and timestamp
                cache[url] = {
                    "content": content,
                    "timestamp": time.time(),
                    "count": 1
                }
                return content
        return wrapper
    return decorator

# Function to get page content from a given URL
@cache_response()
def get_page(url):
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com"
    content = get_page(url)
    print(content)
    print(f"Number of times accessed: {cache[url]['count']}")
    time.sleep(5)  # Simulating a delay to test caching expiration
    content = get_page(url)
    print(content)
    print(f"Number of times accessed: {cache[url]['count']}")

