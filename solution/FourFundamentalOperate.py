from tree.BinaryTree import *


def strip_parentheses(expression):
    """去掉首尾多余的括号"""
    if expression.startswith('(') and expression.endswith(')'):
        ex = expression[1:-1]

        flag = 0
        for s in ex:
            if s == '(':
                flag -= 1
            elif s == ')':
                flag += 1

            if flag > 0:  # 说明首尾的括号不是多余的
                break
        else:
            expression = ex

    return expression


def build_tree(expression):
    """寻找当前字符串的主节点
    有操作符就把操作符作为主节点，没有操作符就把数据作为主节点"""
    expression = strip_parentheses(expression)
    p = BNode(None)
    flag = 0  # 用于屏蔽括号
    index = 0  # 记录操作符的位置
    for i, s in enumerate(expression):
        if s == '(':
            flag -= 1
        elif s == ')':
            flag += 1

        if flag < 0:
            continue
        elif flag > 0:
            raise ValueError('Please check out the input formulate!')

        if i == 0:  # 如果第一位是操作符，例如，'-'号，我们把它理解为负号，不会把它当做操作符
            continue

        if s in ['*', '/']:
            index = i
        elif s in ['+', '-']:  # 运算优先级最低的作为主节点
            index = i
            break

    p.data = expression[index] if index > 0 else expression  # 如果没获取到操作符，说明整个字符串是数值
    p.left = build_tree(expression[:index]) if index > 0 and expression[:index] else None
    p.right = build_tree(expression[index + 1:]) if index > 0 and expression[index + 1:] else None

    return p


def operate(bn: BNode):
    """后序遍历计算"""
    global stack

    if bn:
        operate(bn.left)
        operate(bn.right)
        if bn.data in ['+', '-', '*', '/']:
            a = stack.pop(-1)
            b = stack.pop(-1)

            if bn.data == '+':
                result = a + b
            elif bn.data == '-':
                result = a - b
            elif bn.data == '*':
                result = a * b
            else:
                result = a / b

            stack.append(result)
        else:
            stack.append(float(bn.data))


def calculate(expression: str):
    """四则运算主程序"""
    global stack

    stack = []
    expression = expression.replace(' ', '')  # 去掉多余的空格
    root = build_tree(expression)  # 获取二叉树的根节点

    bt = BinaryTree()
    print(bt.postorder(root))
    # bt.draw(root)

    operate(root)  # 四则运算操作

    return stack[0]


if __name__ == '__main__':
    print(calculate('-1+2*(3.2+4)*5+6'))
