import json
import sys

import websocket
import rel

SERVER_URI = "ws://127.0.0.1:9000/chat"
BEGIN_TOKEN = "<|begin|>"
END_TOKEN = "<|end|>"
ERR_TOKEN = "<|err|>"

def _print(s, end="\n"):
    s = s + end
    sys.stdout.write(s)
    sys.stdout.flush()

def on_message(ws, message):
    resp = json.loads(message)
    token = resp["token"]
    if token == BEGIN_TOKEN:
        _print("Answer: ", end="")
    elif token == END_TOKEN:
        _print("")
    elif token == ERR_TOKEN:
        _print("Something went wrong")
    else:
        _print(token, end="")

def on_error(ws, error):
    _print(f"### error: {error}")

def on_close(ws, close_status_code, close_msg):
    _print(f"### closed: {close_status_code} {close_msg}")

def on_open(ws):
    _print("### opened: Ctrl-C to end")


if __name__ == "__main__":
    websocket.enableTrace(False)
    client = websocket.WebSocketApp(SERVER_URI,
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
    client.run_forever(dispatcher=rel, reconnect=5)
    rel.signal(2, rel.abort)
    question = input("Question: ")
    req = json.dumps({"question": question})
    client.send(req)
    rel.dispatch()
