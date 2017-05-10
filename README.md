# Python Live Reload
基于`Python3.5`写的页面热更新server，操作系统：`windows10`  

## 使用方式
下载`example`文件夹，以`example`内的文件举例：  
首先打开`cmd`，定位到`example`所在文件夹，需要监听变化的文件依次添加在`liveReloadServer.py`之后，这里监听`index.html`文件，执行以下命令：  
```bash
$ python liveReloadServer.py index.html
```
然后在浏览器打开`index.html`文件，修改文件内容，即可观察到页面自动刷新。  

## 注意
1.在需要刷新的页面中加入如下脚本：  
```javascript
<script>
    var ws = new WebSocket("ws://127.0.0.1:8080/");
    ws.onmessage = function(event) {
        var data = event.data;
        if(data === "reload") {
            window.location.reload(true);
        }
    };
</script>
```

2.若Python提示没有`websockets`模块，则需要下载：  
```bash
$ pip install websockets
```
