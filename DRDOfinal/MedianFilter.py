import numpy
import matplotlib.pyplot as plt
from PIL import Image

def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(data),len(data[0])))
    #print(data_final)	
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

def i2a2i(s,i):
	arr=numpy.array(s)
	removed_noise=median_filter(arr,3+i)
	img=Image.fromarray(removed_noise)
	if img.mode != 'RGB':
		img=img.convert('RGB')
	img.save("noisyimg"+str(i)+".jpeg","jpeg")
	img.show()
	return img


def main():
    img0=Image.open("nn.png").convert("L")
    #img.show()
  
    for i in range(2):
    	img = Image.open("nn.png").convert(
        "L")
    	img=i2a2i(img,i)
  
    plt.subplot(121), plt.imshow(img0)
    plt.subplot(122), plt.imshow(img)
    #plt.savefig(plt_file_path)
    plt.show()

main()
