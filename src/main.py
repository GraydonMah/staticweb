from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.BOLD, "https://www.bood.dev")
    print(node)

if __name__ == "__main__":
    main()
