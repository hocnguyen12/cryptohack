from PIL import Image
import numpy as np

lemur = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")
flag = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")

lemur_p = lemur.load()
flag_p = flag.load()
width, height = lemur.size

arr = np.zeros((width, height, 3), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        x_lem, y_lem, z_lem = lemur_p[x, y]
        x_fl, y_fl, z_fl = flag_p[x, y]
        arr[x, y, 0] = x_lem ^ x_fl
        arr[x, y, 1] = y_lem ^ y_fl
        arr[x, y, 2] = z_lem ^ z_fl

test = Image.fromarray(arr)
test.show()
test.save("crypto{XORly_not!}.png")
print("crypto{XORly_not!}")