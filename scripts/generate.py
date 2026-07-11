#!/usr/bin/env python3
"""Generate deck-analyzer output."""
import sys, json, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"name": "deck-analyzer", "generated": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{name}: ready")

if __name__ == "__main__":
    main()
