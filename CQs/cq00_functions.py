"""CQ00"""

__author__ = "730767392"


def mimic(message: str) -> str:
    """Repeat my input"""
    return message


def main() -> None:
    """Return mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    """Run main function in trailhead"""
    main()
