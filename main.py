import requests
import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()

def convert_int_to_str(value, target):
    val_10 = 0
    inwhile = value
    while inwhile / 10 > 0:
        val_10 += 1
        inwhile /= 100
    return ('0' * (target-val_10)) +  str(value)

def main(): 
    count = 0
    url = 'image\\'
    name = 'database.txt'
    file = open(name, "r")
    filetype = ['.png', '.jpg', '.jpeg']

    

    for line in file:
        for each in filetype:
            if each in line:
                
                # response = requests.get(line, stream=True).content
                # print(response)
                # img_name = url + convert_int_to_str(count, 5) + each
                img_name = url + str(count) + each
                print(line)
                print(img_name)
                # with open(img_name, 'wb') as handler:
                #     handler.write(response)
                urllib.request.urlretrieve(line, img_name)
                count += 1
        if count > 5:
            break


    # for line in file:
    #     for each in filetype:
    #         if each in line:
                
    #             response = requests.get(line, stream=True).content
    #             # print(response)
    #             # img_name = url + convert_int_to_str(count, 5) + each
    #             img_name = url + str(count) + each
    #             print(line)
    #             print(img_name)
    #             # with open(img_name, 'wb') as handler:
    #             #     handler.write(response)
    #             img = open(img_name, "wb")
    #             img.write(response)
    #             img.close()
    #             count += 1
    #     if count > 5:
    #         break

    # for line in file:
    #     for each in filetype:
    #         if each in line:
    #             print(line)
    #             response = requests.get(line, stream=True).content
    #             img_name = url + convert_int_to_str(count, 5) + each
    #             # with open(img_name, 'wb') as handler:
    #             #     handler.write(response)
    #             img = open(img_name, "wb")
    #             img.write(response)
    #             img.close()
    #             count += 1


main()