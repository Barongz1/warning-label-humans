"""Warning Label for Humans: One Line, Big Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a single-line safety warning label that should come printed on every human being, 160 characters or fewer.
"""
import os

LINE = "WARNING: May suddenly fall asleep during important meetings. Do not operate heavy machinery or small children after lunch."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
