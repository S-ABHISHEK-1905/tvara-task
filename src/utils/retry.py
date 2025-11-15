import time
# Robustness
def retry(func, attempts=2, delay=1):
    last_error = None

    for i in range(attempts):
        try:
            return func()
        except Exception as e:
            last_error = e
            if i < attempts - 1:
                time.sleep(delay)

    raise last_error