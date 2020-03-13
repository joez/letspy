#!/usr/bin/env python3

import subprocess as sp
import json

""" Monitor docker events and act accordingly

Run as a daemon like this:
nohup ./docker-events.py > /dev/null 2>&1 &
"""


def handle(event):
    kind, action = event["Type"], event["Action"]
    if kind == "container" and action == "die":
        name, code = [event["Actor"]["Attributes"][x]
                      for x in ["name", "exitCode"]]
        if code == '129':
            print(f"container {name} exit for reboot")
        elif code == '130':
            print(f"container {name} exit for shutdown")
        else:
            print(f"container {name} exit {code}")
    else:
        pass  # print(str(event))


def main():
    cmd = ["docker", "events", "--format", r"{{json .}}"]
    p = sp.Popen(cmd, stdout=sp.PIPE, universal_newlines=True)
    for line in p.stdout:
        handle(json.loads(line))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
