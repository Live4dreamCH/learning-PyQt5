import os

filePath = r'D:\music'
fileMap = {}
order = 1

x = os.listdir(filePath)
for filename in x:
    if os.path.splitext(filename)[1] in ['.ape', '.mp3', '.flac', '.ncm', '.mp4']:
        size = os.path.getsize(os.path.join(filePath, filename))
        fileMap[filename] = size

filelist = sorted(fileMap.items(), key=lambda d: d[0], reverse=False)
for filename, size in filelist:
    print(order, filename, size)
    order += 1
