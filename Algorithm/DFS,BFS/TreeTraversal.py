##* DFS (전위순회, 중위순회, 후위순회)

class Tree:
    def __init__(self, i, l, r):  # index left right
        self.index = i
        self.left = l
        self.right = r

    # 재귀적으로 동작함
    # 새로운 노드가 현재 노드의 자식으로 추가되어야 하는 경우 -> 바로추가
    # 그렇지 않다면, 자기 자식중에 새로운 노드를 받을 수 있는 노드를 탐색 => 재귀알고리즘
    def addNode(self, i, l, r):
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요
        '''
        # 루트노드 인경우 or 다른 노드인 경우
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None

            return True
        ## 그렇지 않다면 재귀
        else:
            flag = False

            if self.left != None:
                flag = self.left.addNode(i, l, r)

            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)

            return flag


def preorder(tree):
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    # 순회를 한 결과 방문한 노드들을 순서대로 담고 있는 리스트
    # result에 값을 추가한다 = 현재 노드를 방문한다
    result = []

    # [루트노드 ] + [왼쪽 전위순회] + [오른쪽 전위순회]
    result.append(tree.index)

    if tree.left != None:  # 왼쪽 유효
        result = result + preorder(tree.left)  # 왼쪽 전위순회한 결과
    if tree.right != None:  # 오른쪽 유효
        result = result + preorder(tree.right)

    return result


def inorder(tree):
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    if tree.left != None:
        result = result + inorder(tree.left)

    result.append(tree.index)

    if tree.right != None:
        result = result + inorder(tree.right)

    return result


def postorder(tree):
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    if tree.left != None:
        result = result + postorder(tree.left)

    if tree.right != None:
        result = result + postorder(tree.right)

    result.append(tree.index)

    return result


def main():
    myTree = Tree(None, None, None)

    n = int(input())

    for i in range(n):
        myList = [int(v) for v in input().split()]

        if myList[1] == -1:
            myList[1] = None

        if myList[2] == -1:
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))


if __name__ == "__main__":
    main()
