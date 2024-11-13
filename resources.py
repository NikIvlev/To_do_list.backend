def print_with_indent(value, indent=0):
    indentation = "\t" * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent=indent + 1)

    def __str__(self):
        return self.title


groceries = Entry('Продукты')
category = Entry('Мясное')

category.add_entry(Entry('Курица'))
category.add_entry(Entry('Говядина'))
category.add_entry(Entry('Колбаса'))

groceries.add_entry(category)

groceries.print_entries()