# implement "leaky bucket" that flow control algorithm

from datetime import timedelta, datetime

from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'bucket(quota={self.quota})'


def fill(bucket, amount):
    now = datetime.now()

    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False  # bucket assignment not reset after start new period
    if bucket.quota - amount < 0:
        return False  # not enough bucket's available capacity
    else:
        bucket.quota -= amount
        return True  # Bucket's capacity is enough, use


def set_bucket():
    bucket = Bucket(60)
    fill(bucket, 100)
    print(colored(f'bucket : {bucket}', 'green'))
    if deduct(bucket, 99):
        print(colored(f'99 capacity used', 'green'))
    else:
        print(colored(f'can\'t process 99 capacity', 'red'))
    print(colored(f'{bucket}', 'green'))

    if deduct(bucket, 3):
        print(colored(f'3 capacity used', 'green'))
    else:
        print(colored(f'can\'t process 3 capacity', 'red'))
    print(colored(f'{bucket}', 'green'))


class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return (f'NewBucket(max_quota={self.max_quota}, '
                f'quota_consumed={self.quota_consumed})')

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


@trace_func
def set_bucket_new():
    """ same usage for set_bucket() method, only Bucket Constructor is changed
    Bucket(60) => NewBucket(60)

    """
    bucket = NewBucket(60)
    fill(bucket, 100)
    print(colored(f'bucket : {bucket}', 'green'))
    if deduct(bucket, 99):
        print(colored(f'99 capacity used', 'green'))
    else:
        print(colored(f'can\'t process 99 capacity', 'red'))
    print(colored(f'{bucket}', 'green'))

    if deduct(bucket, 3):
        print(colored(f'3 capacity used', 'green'))
    else:
        print(colored(f'can\'t process 3 capacity', 'red'))
    print(colored(f'final : {bucket}', 'green'))


if __name__ == '__main__':
    set_bucket()
    set_bucket_new()
