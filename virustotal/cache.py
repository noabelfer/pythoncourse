import time
import pickle

def cache(filename='cache.pkl', ttl=3600):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            key = str(args) + str(kwargs)
            cachedict = wrapper.load_cache(self,filename)
            if key in cachedict:
                result, timestamp = cachedict[key]
                if (time.time() - timestamp) < ttl:
                    return result
            result = func(self, *args, **kwargs)
            cachedict[key] = (result, time.time())
            wrapper.save_cache(self,filename, cachedict)
            return result
        def save_cache(self,filename, cachedict):
            print('save ')
            self.lock.acquire()
            with open(filename, 'wb') as f:
                pickle.dump(cachedict, f)
                self.lock.release()
        def load_cache(self,filename):
            print('load ')
            self.lock.acquire()
            try:
                with open(filename, 'rb') as f:
                    ret = pickle.load(f)
                    self.lock.release()
                    return ret
            except FileNotFoundError:
                self.lock.release()
                return {}
        wrapper.save_cache = save_cache
        wrapper.load_cache = load_cache
        return wrapper
    return decorator
