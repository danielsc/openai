#!/bin/bash
_term() {
    echo "Caught SIGTERM signal!"
    kill -TERM "$child" 2>/dev/null
}
trap _term SIGTERM
echo "starting the script";
python test_sigterm.py &
child=$!
wait "$child"