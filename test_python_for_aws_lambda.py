from datetime import datetime
from time import sleep


def test_python_for_aws_lambda(event, context):
    """ RunTimeを遅延させたい場合使用 """
    print('Batch Start !!!!!!!!')
    print(datetime.now())
    print('Sleep 5 seconds Start')
    sleep(5)
    print('Sleep 5 seconds Stop')

    """ TrueまたはFalseを選択する """
    is_succeeded = True
    # is_succeeded = False

    if is_succeeded:
        print('Batch Succeeded !!!!!!!!')
        return 0
    else:
        print('Batch Failed !!!!!!!!')
        return 1
