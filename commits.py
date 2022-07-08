import subprocess

with open("commits.txt", "r") as f:
    a = f.read().splitlines()

for i in range(len(a) - 1):
    subprocess.run(
        [
            f"asv continuous --interleave-processes -a processes=2 --split --show-stderr {a[i]} {a[i+1]}"
        ],
        shell=True,
    )
