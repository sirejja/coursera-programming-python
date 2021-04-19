import argparse
import json
import os
import sys
import tempfile

argparser = argparse.ArgumentParser()
argparser.add_argument('--key')
argparser.add_argument('--val')
args = argparser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.isfile(storage_path): 
    if args.val:
        with open(storage_path, "r") as f:
            storage = json.load(f)
            if args.key in storage:
                storage[args.key] = storage[args.key] + [args.val]
            else:
                storage.update({args.key: [args.val]})
        with open(storage_path, "w") as f:
            json.dump(storage, f)
    else:
        try:
            with open(storage_path, "r") as f:
                storage = json.load(f)
                if storage[args.key] == None:
                    print(None)
                if len(storage[args.key]) > 1:
                    print(', '.join(storage.get(args.key)))
                else:
                    print(*storage.get(args.key))
        except:
            print(None)
else:
    d = {}
    with open(storage_path, "w") as f:
        if args.val:
            d = {args.key: [args.val]}
            json.dump(d, f)
        else:
            d = {args.key: None}
            print(None)