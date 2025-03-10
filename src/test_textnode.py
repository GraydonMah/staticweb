import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
#        print("test_eq")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
#        print("test_neq")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_None_URL(self):
#        print("test URL=None")
        node = TextNode("None URL", TextType.BOLD) 
#        print(node.url)
        node_url = node.url
        self.assertEqual(node_url,None)

if __name__ == "__main__":
    unittest.main()
