class Stack: 
    def __init__(self):
        self.pri = []
    def is_empty(self):
        return self.pri == []
    def push(self, data):
        self.pri.append(data)
    def pop(self):
        return self.pri.pop()
rag= Stack()
barathi = input(' ') 
for char in barathi:
    rag.push(char)
rev_text = ''
while not rag.is_empty():
    rev_text = rev_text + rag.pop()
if barathi== rev_text:
    print('YES')
else:
    print('NO')
