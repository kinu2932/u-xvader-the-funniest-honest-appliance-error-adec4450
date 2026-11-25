#!/usr/bin/env python3
"""The Funniest Honest Appliance Error -- dishwasher error line (v1 draft).

Writes one line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: same bytes on every run, stdlib only.
"""
import os

ENTRY = "ERROR E7: I washed the dishes. The plates are clean. The smell is still here. It was never the dishes."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
