var ws = new WebSocket("ws://127.0.0.1:8080/");
ws.onmessage = function(event) {
    var data = event.data;
    if (data === "reload") {
        window.location.reload(true);
    }
};
