# encoding: utf-8
from tuple import *
from numpy import *

file_name = 'three_tuple.txt'
target = open('matrix.txt', "a", 512000000)
# open函数第三个参数是bufsize，据说可以提高大文件读写速度，原理昨天没查到
product_count = 66370
# 这个数据其实并没有用到
user_count = 128794
# 缓存50M

def arrayToString(arrayOne):
    # 将数组转换为字符串
    array_string = ''
    for numOne in arrayOne:
        array_string += (str(int(numOne))+' ')
    return array_string[:-1]


def transferThreeTuple(three_tuple):
    global target
    productPos = 0
    # 记录矩阵到第几行了
    array_one = zeros(user_count)
    for listOne in three_tuple:
        if listOne[0] != productPos:
            # 如果当前得到的行数跟productPos不同，说明矩阵已经换行，此时进行一次迭代
            string_one = arrayToString(array_one)
            yield string_one+'\n'
            if productPos % 1000 == 0:
                # 每迭代一千次，关闭并重开文件以控制资源占用，此时数据会写入文件
                target.close()
                target = open('matrix.txt', "a", 51200000)
                print productPos
                # 数据太大，print用来知道它有没有死掉
            for num in array_one:
                # 清空数据中数据(此处应当可以改进，增加一个list用来存储需要清空的位置，直接遍历清空有些浪费资源)
                num = 0
            productPos+=1
        # 无论是否迭代，都将三元组内容写入
        array_one[listOne[1]] = listOne[2]

three_tuple = []
get_tuple(file_name, three_tuple)
for product in transferThreeTuple(three_tuple):
    target.write(product)
target.close()