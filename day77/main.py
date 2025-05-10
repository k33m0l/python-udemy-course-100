import numpy
from numpy.random import random
import matplotlib.pyplot as pyplot
from scipy import datasets
from PIL import Image

tensor = numpy.array(
    [
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
        ],
        [
            [7, 86, 6, 98],
            [5, 1, 0, 4],
        ],
        [
            [5, 36, 32, 48],
            [97, 0, 27, 18],
        ]
    ]
)

print("Challange 1:")
print(tensor.ndim)
print(tensor.shape)
print(tensor[2][1][3])
print(tensor[2, 1, :])
print(tensor[:, :, 0])

print("Challange 2:")
a = numpy.arange(10, 30)
print(a)
print(a[-3:])
print(a[3:6])
print(a[12:])
print(a[::2])

print("Challange 3:")
print(a[::-1])

print("Challange 4:")
b = numpy.array([6,0,9,0,0,5,0])
b_non_zero = numpy.nonzero(b)
print(b_non_zero)

print("Challange 5:")
c = random((3,3,3))
print(c)

print("Challange 6:")
d = numpy.linspace(0, 100, num=9)
print(d)

print("Challange 7:")
e = numpy.linspace(start=-3, stop=3, num=9)
pyplot.plot(d, e)

print("Challange 8:")
noise = random((128, 128, 3))
pyplot.imshow(noise)

# pyplot.show()

print("Matrix multiplication:")
matrix1 = numpy.array(
    [
        [1, 3],
        [0, 1],
        [6, 2],
        [9, 7],
    ]
)
matrix2 = numpy.array(
    [
        [4, 1, 3],
        [5, 8, 5],
    ]
)
print(numpy.matmul(matrix1, matrix2))

print("Image op")
img = datasets.face()
# pyplot.imshow(img)
# pyplot.show()

img = Image.open("yummy_macarons.jpg")
img = numpy.array(img)

sRGB_array = img / 255
grey_values = numpy.array([0.2126, 0.7152, 0.0722])
img_gray = sRGB_array @ grey_values # Same as numpy.matmul(sRGB_array, grey_values)
pyplot.imshow(img_gray, cmap="gray")
pyplot.show()

