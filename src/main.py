import textnode
from textnode import TextType


def main():
    node = textnode.TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)








if __name__ == "__main__":
    main()