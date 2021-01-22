import json
with open('output_file_name') as json_read:
    data=json.load(json_read)
with open('bcsample.json', 'w') as json_write:
        for i in range(1000):
                json_write.write(str(data[i]))