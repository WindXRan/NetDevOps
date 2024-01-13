# sort,sorted()

## 1. 引言

Python中的` sort()`和`sorted()`函数主要用于按升序或降序对数据进行排序。在本文中比较用于列表时，两个函数在编程和语法上的差异。

## 2. Sort()函数基本用法

用于列表排序的sort函数(方法)的语法如下：

> list.sort(reverse=False, key=None)
用法如下：

- 参数reverse：默认为False。如果reverse=True，则数据将按降序排列。
- 参数key： 默认为None。我们可以指定一个用户定义的函数来自定义排序。

### 2.1 样例一之基本排序

我们首先尝试使用上述默认参数来看个事例，样例代码如下：

```Python
# Original List
typ_data = ['$', '45', '3j+5', 'Hello']
print(f'Original Data: {typ_data}')

# Sorting the list
typ_data.sort()
# Printing sorted list
print(f'Sorted Data: {typ_data}')

----------
Original Data: ['$', '45', '3j+5', 'Hello']
Sorted Data: ['$', '3j+5', '45', 'Hello']
```

可以知道上述结果按照字符串首字符的ASCII码进行升序排序。

### 2.2 样例二之用户自定义排序函数

有时间我们需要按照用户自定义的函数来对列表进行排序，相应的代码示例如下：

```cpp
# List containing dictionary data
data = [
    {'fruit': 'strawberry', 'price': 100},
    {'fruit': 'banana', 'price': 91},
    {'fruit': 'mango', 'price': 132},
    {'fruit': 'cherry', 'price': 82},
]

print(f'Original Data: {data}')

# Function for sorting by key 'price'

# Sorting data using the user-defined sorting function
data.sort(key=lambda item:item['price'])
print('-'*20)
# Printing the data
print(f'Sorted Data: {data}')
```

运行结果如下：

```cpp
Original Data: [{'fruit': 'strawberry', 'price': 100}, {'fruit': 'banana', 'price': 91}, {'fruit': 'mango', 'price': 132}, {'fruit': 'cherry', 'price': 82}]
--------------------
Sorted Data: [{'fruit': 'cherry', 'price': 82}, {'fruit': 'banana', 'price': 91}, {'fruit': 'strawberry', 'price': 100}, {'fruit': 'mango', 'price': 132}]
```

上述代码中，我们通过编写一个名为`sort_dict_by_price`的函数，它接受我们的字典本身作为输入，并返回键“price”的值。将此函数已传递给函数`sort`的参数`key`，该参数将根据价格按升序对数据进行排序。

## 3. Sorted()函数基本用法

用于列表排序的sorted函数的语法如下：

> sorted(iterable, key=None, reverse=False)

用法如下：

- 参数iterable： 必需。输入任何可迭代数据
- 参数key： 默认为“None”。指定排序条件。
- 参数reverse： 默认为False。当设置为True时，数据将按降序排列。

### 3.1 基本排序

Python中的`sorted()`函数用于对可迭代数据进行排序。默认情况下，此函数按升序对数据进行排序。

我们当然也可以使用`sorted`()函数来对各种类型的数据进行排序，样例代码如下：

```cpp
list_data = [43, 21, 2, 34]
print(f'Sorted List: {sorted(list_data)}')

# Seperator
print('-'*20)

tuple_data = (('x', 3), ('w', 1), ('1', 4))
print(f'Sorted Tuple: {sorted(tuple_data)}')

# Seperator
print('-'*20)

dict_data = {9: 'G', 1: 'V', 4: 'E'}
print(f'Sorted Dictionary Keys: {sorted(dict_data)}')
print(f'Sorted Dictionary Values: {sorted(dict_data.values())}')
print(f'Sorted Dictionary Items: {sorted(dict_data.items())}')
```

结果如下：

```cpp
Sorted List: [2, 21, 34, 43]
--------------------
Sorted Tuple: [('1', 4), ('w', 1), ('x', 3)]
--------------------
Sorted Dictionary Keys: [1, 4, 9]
Sorted Dictionary Values: ['E', 'G', 'V']
Sorted Dictionary Items: [(1, 'V'), (4, 'E'), (9, 'G')]
```

### 3.2 用户自定义排序函数

我们同样也可以通过将自定义排序函数传递给函数`sorted()`来实现相应的排序功能，举例如下：

```cpp
# Tuple data
tuple_data = ( 
    ('Mango', 25),
    ('Walnut', 65),
    ('Cherry', 10),
    ('Apple', 68),
)

print(f'Original: {tuple_data}')
# Separator
print('-'*20)
# Sorting based on sorting criteria in descending order
sorting = sorted(tuple_data, key=lambda item: item[1], reverse=True)
print(f'Sorted: {sorting}')
```

结果如下：

```cpp
Original: (('Mango', 25), ('Walnut', 65), ('Cherry', 10), ('Apple', 68))
--------------------
Sorted: [('Apple', 68), ('Walnut', 65), ('Mango', 25), ('Cherry', 10)]
```

上述代码中，由于在传递自定义函数时使用了参数`key`，因此元组是根据第二项进行排序的；同样由于我们将参数`reverse`设置为True，此时输出的数据是按降序排序输出的。

## 4. 总结

综上所述，`sort()`和`sorted()`函数是Python中用于对数据进行排序的重要方法。

通常情况下，对于简单的排序任务，可以使用`sorted()`函数更简洁地完成任务。对于需要修改原始列表并进行就地排序的情况，可以使用`sort()`函数。

简而言之，这两个函数都用于对数据进行排序，但函数`sort()`只对Python列表进行排序，而`sorted()`函数用于对可迭代数据进行排序。

| sort()                                                       | sorted()                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Used to sort the Python `List`.                              | Used to sort any iterable data such as `List`, `Tuple`,`Dictionary` and more. |
| Takes two parameters: `key` and `reverse`                    | Takes three parameters: `iterable`,`key` and `reverse`.      |
| It is a List function(`list.sort()`) and can only work with Lists. | It is a function to sort any data which can be iterated.     |
| `sort()` modifiles the original list.                        | `sorted()` dosen't modify the original data instead it returns the new modified data. |

