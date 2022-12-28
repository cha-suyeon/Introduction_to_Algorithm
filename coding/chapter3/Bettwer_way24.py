from time import sleep
from datetime import datetime

def log(message, when=datetime.now()):
    print(f'{when}: {message}')
    
log('안녕!')
sleep(0.1)
log('다시 안녕!')


def log(message, when=None):
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')
    
log('안녕!')
sleep(0.1)
log('다시 안녕!')

import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('잘못된 데이터')
foo['stuff'] = 5
bar = decode('또 잘못된 데이터')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

assert foo is bar

def decode(data, default=None):
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default
    
foo = decode('잘못된 데이터')
foo['stuff'] = 5
bar = decode('또 잘못된 데이터')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

from typing import Optional

def log_typed(message: str,
              when: Optional[datetime]=None) -> None:
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')