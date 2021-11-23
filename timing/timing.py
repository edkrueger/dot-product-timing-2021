import timeit

def time_function(
    func, args=None, kwargs=None, number=10, repeat=3, agg=min, warmup=False
):
    args = [] if not args else args
    kwargs = {} if not kwargs else kwargs
    return agg(
        timeit.repeat(lambda: func(*args, **kwargs), repeat=repeat, number=number)
    )