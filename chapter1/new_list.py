
# 自定义列表类型，继承自list
class Mylist(list):
    def __sub__(self, other):
        new_list = []
        for item in self:
            if item not in other:
                new_list.append(item)
        return new_list


if __name__ == '__main__':
    a = Mylist([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = Mylist([1, 2, 10])
    c = a - b
    print(c)
# [3, 4, 5, 6, 7, 8, 9]
