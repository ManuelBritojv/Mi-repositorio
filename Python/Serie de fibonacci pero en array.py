from re import A
from xml.etree.ElementTree import Comment


def fibonacci():
    arr = [0,1]
    while len(arr) < 50:
        arr.append(arr[len(arr)-2] + arr[len(arr)-1])
    print(arr)


fibonacci()
