class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{}'.format(self.val)


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def addAtHead(self, val):
        cur = self.head
        new = Node(val)
        new.next = cur
        self.head = new


class HexNumber:
    def __init__(self, number = None):
        if number != number.upper():
            print("Error")
            return None
        Number = LinkedList()
        for el in number:
            Number.addAtHead(el)
        self.num = Number.head


    def add(self, other):
        res = ""
        first = self.num
        second = other.num
        count = 0
        while first is not None and second is not None:
            a = from_hex_to_decimal(first.val)
            b = from_hex_to_decimal(second.val)
            if a + b + count < 16:
                res += from_decimal_to_hex(a+b+count)
                count = 0
            else:
                res += from_decimal_to_hex(a+b+count - 16)
                count = 1

            first = first.next
            second = second.next


        while first is not None:
            a = from_hex_to_decimal(first.val)
            if a + count < 16:
                res += from_decimal_to_hex(a+count)
                count = 0
            else:
                res += from_decimal_to_hex(a+count - 16)
                count = 1
            first = first.next

        while second is not None:
            b = from_hex_to_decimal(second.val)
            if b + count < 16:
                res += from_decimal_to_hex(b+count)
                count = 0
            else:
                res += from_decimal_to_hex(b+count - 16)
                count = 1
            second = second.next

        res += str(count)
        return HexNumber(res[::-1])


def print_hex_num(num):
    a = num.num
    number = ""
    while a is not None:
        number += a.val
        a = a.next
    if number[-1] == '0':
        number = number[:-1:1]
    print(number[::-1])

def from_hex_to_decimal(num):
    return ord(num) - ord('A') + 10 if num >= 'A' and num <= 'F' else ord(num) - ord('0') 

def from_decimal_to_hex(num):
    return chr(ord('A') + num - 10) if num > 9 else chr(ord('0') + num)


def main():
    first = HexNumber("31F")
    second = HexNumber("13")
    sum = first.add(second)
    print_hex_num(first)
    print_hex_num(second)
    print_hex_num(sum)


if __name__ == "__main__":
    main()
