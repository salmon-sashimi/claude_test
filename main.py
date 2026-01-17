"""
Sample Python script for claude_test project.
"""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def show_info():
    """Print some project info."""
    print("Project: claude_test")
    print("Author: gab")
    print("Status: Testing changes!")


def main():
    print("changes made!")
    print(greet("World"))
    show_info()


if __name__ == "__main__":
    main()
