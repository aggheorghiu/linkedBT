from typing import TypeVar, Generic, Optional, Iterator, List
from collections import deque

T = TypeVar('T')  # generic type


class BinaryNode(Generic[T]):
    def __init__(self, data: T, left: Optional['BinaryNode[T]'] = None,
                 right: Optional['BinaryNode[T]'] = None) -> None:
        self.data: T = data
        self.left: Optional['BinaryNode[T]'] = left
        self.right: Optional['BinaryNode[T]'] = right


class LinkedBT:
    def __init__(self, data: T, left: Optional['LinkedBT'] = None,
                 right: Optional['LinkedBT'] = None) -> None:
        self._root = BinaryNode(data,
                                left._root if left else None,
                                right._root if right else None)

    def leaves(self) -> List[T]:
        """
        Get a list of the tree's leaf nodes
        :return: list of leaf nodes
        """

        def find_leaves(node: BinaryNode[T]) -> List[T]:
            if node is None:
                return []
            elif node.left is None and node.right is None:
                return [node.data]
            else:
                return find_leaves(node.left) + find_leaves(node.right)

        return find_leaves(self._root)

    def find_binary_sequence(self, character: T) -> str:
        """
        Find the binary sequence that represents a given character in the tree
        :param character: the character to find
        :return: the binary sequence as a string
        """

        def traverse(node: Optional[BinaryNode[T]], target: T, path: str) -> Optional[str]:
            if node is None:
                return None
            elif node.data == target:
                return path
            else:
                left_path = traverse(node.left, target, path + "0")
                if left_path is not None:
                    return left_path

                right_path = traverse(node.right, target, path + "1")
                if right_path is not None:
                    return right_path

            return None

        return traverse(self._root, character, "")

    def get_character_from_bits(self, bit_sequence: str) -> Optional[T]:
        node = self._root

        for bit in bit_sequence:
            if bit == "0":
                if node.left is not None:
                    node = node.left
                else:
                    return None
            elif bit == "1":
                if node.right is not None:
                    node = node.right
                else:
                    return None
            else:
                return None

        return node.data if node else None

    def is_empty(self) -> bool:
        return self._root is None

    def __len__(self) -> int:
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        return count_nodes(self._root)

    def __str__(self):
        result = []

        def traverse(node):
            if node is not None:
                result.append(str(node.data))
                traverse(node.left)
                traverse(node.right)

        traverse(self._root)
        return " ".join(result)

    def __iter__(self) -> Iterator:
        def traverse(node):
            if node is not None:
                yield from traverse(node.left)
                yield node.data
                yield from traverse(node.right)

        return traverse(self._root)

    def __contains__(self, item) -> bool:
        # this will check if an item is in the tree using pre-order traversal
        def traverse(node):
            if node is None:
                return False
            if node.data == item:
                return True
            return traverse(node.left) or traverse(node.right)

        return traverse(self._root)

    def clear(self):
        self._root = None

    def root(self) -> Optional[T]:
        return self._root.data if self._root else None

    def left(self) -> Optional['BinaryNode[T]']:
        return self._root.left if self._root else None

    def right(self) -> Optional['BinaryNode[T]']:
        return self._root.right if self._root else None

    def preorder(self) -> None:
        def traverse(node):
            if node is not None:
                print(node.data)
                traverse(node.left)
                traverse(node.right)

        traverse(self._root)

    def inorder(self) -> List[T]:
        def traverse(node: Optional[BinaryNode[T]]) -> List[T]:
            result = []
            if node is not None:
                result.extend(traverse(node.left))
                result.append(node.data)
                result.extend(traverse(node.right))
            return result

        return traverse(self._root)

    def postorder(self) -> None:
        def traverse(node):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                print(node.data)

        traverse(self._root)

    def levelorder(self):
        def traverse(node):
            queue = deque([node])

            while queue:
                current_node = queue.popleft()
                print(current_node.data)

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

        traverse(self._root)

    def height(self) -> int:
        def compute_height(node):
            if node is None:
                return 0
            else:
                left_height = compute_height(node.left)
                right_height = compute_height(node.right)

                return max(left_height, right_height) + 1

        return compute_height(self._root)
