import os
import json
import hashlib

CACHE_FILE = "utils/llm_cache.json"


def _load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def _save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def _make_key(system, user, temperature):
    raw = f"{system}|{user}|{temperature}"
    return hashlib.md5(raw.encode()).hexdigest()


def get_cached(system, user, temperature):
    cache = _load_cache()
    key = _make_key(system, user, temperature)
    return cache.get(key)


def set_cache(system, user, temperature, response):
    cache = _load_cache()
    key = _make_key(system, user, temperature)
    cache[key] = response
    _save_cache(cache)