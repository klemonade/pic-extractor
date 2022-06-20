import requests

header = {
    'user-agent': 'Mozilla/5.0'
}


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
                response = requests.get(line[:-1], headers=header)
                img_name = url + str(count) + each
                print(line)
                print(img_name)
                with open(img_name, 'wb') as handler:
                    handler.write(response.content)
                count += 1

main()