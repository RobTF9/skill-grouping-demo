import sys

def tidy(text: str) -> str:
    return " ".join(text.split())

print(tidy(sys.stdin.read()))
