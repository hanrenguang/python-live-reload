#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib, time, sys, asyncio, websockets

# maintain the file lists
class FileQueue():
    def __init__(self):
        self.fileInfo = []

    def addFile(self, fileName, md5Val):
        fileInfo = []
        fileInfo.append(fileName)
        fileInfo.append(md5Val)
        try:
            if self.fileInfo.index(fileInfo) >= 0:
                return
        except ValueError:
            self.fileInfo.append(fileInfo)
            return True

# get the MD5 value of file
def getFileMD5(file):
    md5 = hashlib.md5()
    f = open(file, 'rb')
    while True:
        chunk = f.read(1024)
        if not chunk:
            f.close()
            break;
        md5.update(chunk)
    return md5.hexdigest()

# check if the file changed
def checkChange(fileName, newMD5, oldMD5):
    if newMD5 != oldMD5:
        print(fileName, 'was changed!')
        return True
    else:
        return False

# send changed message
async def reload(websocket, path):
    try:
        while  True:
            msg = ''
            for index, f in enumerate(queue.fileInfo):
                newVal = getFileMD5(f[0])
                ret = checkChange(f[0], newVal, f[1])
                if ret:
                    queue.fileInfo[index][1] = newVal
                    msg = 'reload'
            await websocket.send(msg)
            await asyncio.sleep(1)
    except:
        pass


if __name__ == "__main__":
    queue = FileQueue()
    # get file lists
    files = sys.argv[1:] if len(sys.argv) > 1 else False

    if not files:
        print("Please enter the currect filename!")
        sys.exit()
    else:
        for f in files:
            md5V = getFileMD5(f)
            queue.addFile(f, md5V)
    # run websocket server
    try:
        start_server = websockets.serve(reload, '127.0.0.1', 8080)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        sys.exit()
