from random import choice
import string
import redis


keyNum = 200
keyLength = 20


# linked redis database
def get_redis():
    r = redis.Redis(host="localhost", port=6379,db=0)
    return r


def push_to_redis(key_list):
    for key in key_list:
        get_redis().lpush('key', key)


def get_data_from_redis():
    key_list = get_redis().lrange('key', 0, -1)
    for key in key_list:
        print(key)


# wrapper ???
def print_key(func):
    def _print_key(length, num):
        for i in func(length, num):
            print(i)
    return _print_key


# get nums key
def get_all_key(length, num, result=None):
    if result is None:
        result = set()
    while len(result) < num:
        if get_key(length) in result:
            continue
        else:
            result.add(get_key(length))
    return result


# get one key
def get_key(length):
    base_char = string.ascii_letters + string.digits
    key_list = [choice(base_char) for _ in range(length)]
    return ''.join(key_list)


push_to_redis(get_all_key(keyLength, keyNum))
get_data_from_redis()
