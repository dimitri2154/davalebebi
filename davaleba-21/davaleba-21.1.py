import json
import threading
import os

def parse_json(filename):

    with open(filename, 'r') as f:
        try:
            data = json.load(f)
            print(f"File: {filename}\nData: {data}\n")
        except json.JSONDecodeError as e:
            print(f"Error parsing {filename}: {e}")

def main():

    files = ['file1.json', 'file2.json', 'file3.json']
    data = [
        {"name": "Giorgi", "age": 21},
        {"city": "TBilisi", "country": "Georgia"},
        [1, 2, 3, {"key": "value"}]
    ]

    for file, content in zip(files, data):
        with open(file, 'w') as f:
            json.dump(content, f, indent=4)

    threads = []
    for filename in files:
        thread = threading.Thread(target=parse_json, args=(filename,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for file in files:
        os.remove(file)

if __name__ == "__main__":
    main()