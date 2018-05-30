import jieba
import jieba_fast
from collections import Counter
import time


# 装饰器
def get_func_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return inner


@get_func_time
def test_key_words_with_jieba(type='jieba'):
    with open('/Users/zhaowei/Desktop/八爪鱼/yeyonglong_enterprise_name/names2.txt') as f:
        a = f.readline()
    print(a)

    key_words = []
    jieba.enable_parallel(2)
    if type == 'jieba':
        key_words = [x for x in jieba.cut(a) if len(x) > 1]
    elif type == 'jieba_fast':
        key_words = [x for x in jieba_fast.cut(a) if len(x) > 1]
    print(key_words)
    jieba.disable_parallel()

    # 获取高频词
    num = 20
    most_words = Counter(key_words).most_common(num)
    print('高频词汇{}:{}'.format(str(num), most_words))


if __name__ == '__main__':
    test_key_words_with_jieba('jieba_fast')
