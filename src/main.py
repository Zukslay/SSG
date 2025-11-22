import textnode
from textnode import TextType


def main():
    node = textnode.TextNode("some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)








if __name__ == "__main__":
    main()