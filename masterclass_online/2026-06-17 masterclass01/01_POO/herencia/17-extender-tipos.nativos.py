class Lista(list):
    def prepend(self, item):
        self.insert(0, item)

l = Lista([1,2,3,4])
l.append(5)
l.prepend(0)

print(l)