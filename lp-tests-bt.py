from lp_Linked_BT import LinkedBT

def build_bt() -> LinkedBT:
    node10 = LinkedBT("U")
    node9 = LinkedBT("V")
    node8 = LinkedBT("VU", node9, node10)
    node7 = LinkedBT("W")
    node1 = LinkedBT("X")
    node2 = LinkedBT("Y")
    node3 = LinkedBT("WVU", node7, node8)
    node4 = LinkedBT("YX", node2, node1)
    node5 = LinkedBT("Z")
    node6 = LinkedBT("YXWVU", node4, node3)
    root = LinkedBT("ZYXWVU", node5, node6)

    return root

def main():
    bt = build_bt()

    print(bt.height())  # print the height
    print(bt.leaves())  # print leaf nodes
    print(bt.inorder())

    character = "YX"
    binary_sequence = bt.find_binary_sequence(character)
    print(binary_sequence)

    bit_sequence = "1001"
    character = bt.get_character_from_bits(bit_sequence)
    print(character)

main()

