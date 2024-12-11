class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.row_count = defaultdict(int) # store row count by table name
        self.tables = defaultdict(defaultdict)
        for name in names:
            self.tables[name] = defaultdict(list)
            self.row_count[name] = 1

    def insertRow(self, name: str, row: List[str]) -> None:
        row_id = self.row_count[name]
        self.tables[name][row_id] = row
        self.row_count[name] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.tables[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)