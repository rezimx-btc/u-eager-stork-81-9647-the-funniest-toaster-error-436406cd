"""The Funniest Toaster Error Message — make.fun entry.

Prints the entry: the single error message a kitchen toaster shows
its owner when something goes wrong. Stdlib only.
"""

LINE = "ERROR: toast ejected at 94 mph. The bagel has left the building. Please check the ceiling."

# The brief caps the entry at 120 characters; fail loudly if it ever grows.
assert len(LINE) <= 120, f"entry is {len(LINE)} characters, over the 120 limit"


def main():
    print(LINE)


if __name__ == "__main__":
    main()
