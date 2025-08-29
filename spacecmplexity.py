import gzip
import os

from collections import Counter

import time
start = time.time()


with open("large_sample_log.txt", "r") as f:
    logs = f.readlines()

print(f"Original log entries: {len(logs)}")

# Step 2: Trimming (keep only last 5000 logs)
trimmed_logs = logs[-5000:]

# Step 3: Deduplication (remove duplicate lines)
unique_logs = list(set(trimmed_logs))
print(f"After deduplication: {len(unique_logs)} entries")

# Step 4: Summarization (count types of logs)
summary = Counter(line.split()[1] for line in unique_logs)  # second word is log level
print("\nLog Summary:")
for log_type, count in summary.items():
    print(f"{log_type}: {count}")

# Step 5: Save processed file
with open("processed_logs.txt", "w") as f:
    f.writelines(unique_logs)

# Step 6: Compression using gzip
with gzip.open("processed_logs.txt.gz", "wt") as f:
    f.writelines(unique_logs)

print("\nProcessing complete!")


def file_size(path):
    return os.path.getsize(path) / 1024  

print(f"Original file size: {file_size('large_sample_log.txt'):.2f} KB")
print(f"Processed file size: {file_size('processed_logs.txt'):.2f} KB")
print(f"Compressed file size: {file_size('processed_logs.txt.gz'):.2f} KB")



end = time.time()
print(f"\nProcessing time: {end - start:.2f} seconds")