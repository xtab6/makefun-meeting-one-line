import os
import sys

# The single sentence that could have replaced an entire pointless meeting.
LINE = "This meeting is cancelled \u2014 the decision is made, the email is sent, and your hour is yours again."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        return 1
    if not 1 <= len(line) <= 200:
        return 1
    data = line.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match exactly.
    with open(path, "rb") as f:
        if f.read() != data:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
