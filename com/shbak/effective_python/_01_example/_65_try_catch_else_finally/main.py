import json

UNDEFINED = object()

def divide_json(path):
    print('*file open')
    handle = open(path, 'r+')   # OSError can occur
    try:
        print(f'*Data read')
        data = handle.read()
        print(f'*JSON Data read')
        op = json.loads(data)
        print('*Execution')
        value = (op['numerator'] /
                op['denominator'])
    except ZeroDivisionError as e:
        print('*ZeroDivisionError Process')
        return UNDEFINED
    else:
        print('*writer calculation result')
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        print('* close() call')
        handle.close()

def call():
    tmp_path = 'random_data.json'
    with open(tmp_path, 'w') as f:
        f.write('{"numerator": 1, "denominator":10}')

    assert divide_json(tmp_path) == 0.1


if __name__ == '__main__':
    call()
