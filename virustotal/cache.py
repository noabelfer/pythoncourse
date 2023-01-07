import time
import pickle

def cache(filename='cache.pkl', ttl=3600):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            key = str(args) + str(kwargs)
            cachedict = wrapper.load_cache(filename)
            if key in cachedict:
                result, timestamp = cachedict[key]
                print('tti '+str(time.time() - timestamp)+' '+str(ttl))
                if (time.time() - timestamp) < ttl:
                    return result
            result = func(self, *args, **kwargs)
            cachedict[key] = (result, time.time())
            wrapper.save_cache(filename, cachedict)
            return result
        def save_cache(filename, cachedict):
            print('save ')
            with open(filename, 'wb') as f:
                pickle.dump(cachedict, f)
        def load_cache(filename):
            print('load ')
            try:
                with open(filename, 'rb') as f:
                    return pickle.load(f)
            except FileNotFoundError:
                return {}
        wrapper.save_cache = save_cache
        wrapper.load_cache = load_cache
        return wrapper
    return decorator
