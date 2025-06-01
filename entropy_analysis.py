import math
import os

def calculate_entropy(filepath):
    try:
        with open(filepath, "rb") as f:
            byteArr = list(f.read())
            fileSize = len(byteArr)
            if fileSize == 0:
                return 0
            freqList = [0] * 256
            for b in byteArr:
                freqList[b] += 1
            entropy = 0.0
            for freq in freqList:
                if freq > 0:
                    prob = freq / fileSize
                    entropy += -prob * math.log2(prob)
            return entropy
    except:
        return -1  # error reading file

def scan_directory(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            entropy = calculate_entropy(filepath)
            if entropy > 7.5:
                print(f"[High Entropy 🔐] {file} → {entropy:.2f}")
            elif entropy != -1:
                print(f"[Normal] {file} → {entropy:.2f}")

# Replace this with the folder you want to scan
scan_directory("add path")
