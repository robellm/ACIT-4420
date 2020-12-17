import numpy as np

file = open("C:/Users/robel/OneDrive/Skrivebord/Oslomet/ACIT4420/oslomet.bmp", "rb")
header = np.fromfile(file, dtype=np.uint8, count=54)
width = header[18] + header[19] * 256 + header[20] * (256 ** 2) + header[21] * (256 ** 3)
print("width: " + str(width))
height = header[22] + header[23] * 256 + header[24] * (256 ** 2) + header[25] * (256 ** 3)
print("height: " + str(height))

data = np.fromfile(file, dtype=np.uint8)
pixels3d = data.reshape(630, 1200, 3)
file.close()

print(len(data))
print(pixels3d.shape)
print(pixels3d[0, 0])

p2 = pixels3d.copy()
for row in range(height):
    for column in range(width):
        if p2[row, column, 0] > 150 and p2[row, column, 1] > 150 and p2[row, column, 2] > 150:
            p2[row, column, 0] = 255
            p2[row, column, 1] = 255
            p2[row, column, 2] = 255
            
file2 = open("oslomet_snow.bmp", "wb")
header.astype("int8").tofile(file2)
p2.astype("int8").tofile(file2)
file2.close()


p3 = pixels3d.copy()
for row in range(height):
    for column in range(width):
        if p3[row, column, 2] > 130 and p3[row, column, 1] > 130 and p3[row, column, 0] < 110:
            temp = p3[row, column, 1]
            if p3[row, column, 2] < 205:
                p3[row, column, 1] = p3[row, column, 2] + 50
            else: p3[row, column, 1] = 255
            if temp > 50:
                p3[row, column, 2] = temp - 50
            else: p3[row, column, 2] = 0

file3 = open("oslomet_yellow.bmp", "wb")
header.astype("int8").tofile(file3)
p3.astype("int8").tofile(file3)
file3.close()

p4 = pixels3d[:430, 200:1000]
header2 = header.copy()
header2[18] = 800 % 256
header2[19] = 800 / 256
header2[22] = 400 % 256
header2[23] = 400 / 256
file4 = open("oslomet_small.bmp", "wb")
header2.astype("int8").tofile(file4)
p4.astype("int8").tofile(file4)
file4.close()
