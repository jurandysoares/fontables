import markdown

_MDOWN_HEADER = '''\
|  |  |  |  |
|--|--|--|--|'''

class Fontables:
    def __init__(self) -> None:
        self._bin_nums: list[str] = [f'{n:05b}' for n in range(1, 32)]

        self._elements_at: dict[int, list[int]] = {}
        for pos in range(4, -1, -1):
            self._elements_at[pos] = [int(n, 2) for n in self._bin_nums if n[pos]=='1' ]

        self._fontables: dict[int, list[list[int]]] = {}
        for pos, elements in self._elements_at.items():
            self._fontables[pos] = [elements[i*4: i*4+4] for i in range(4)]

    @property
    def binary_numbers(self):
        return self._bin_nums[::1]
    
    @property
    def elements(self):
        return self._elements_at.copy()
    
    @property
    def tables(self):
        return self._fontables.copy()
    
    def markdown_table(self, pos: int) -> str:
        assert 0<=pos<5
        lines = [ ('|'+'|'.join([f'{n:>2}' for n in line])+'|') for line in self.tables[pos]]
        lines.insert(0, _MDOWN_HEADER)
        return '\n'.join(lines)
        

if __name__ == '__main__':
    ft = Fontables()
    with open(file='fontables.md', mode='w', encoding='utf-8') as fobj:
        fobj.write("# Fontables: Gustavo Fontoura's tables\n\n")
        for n in range(4, -1, -1):
            fobj.write(ft.markdown_table(n))
            fobj.write('\n\n')
