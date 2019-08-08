"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        table = collections.defaultdict(list)
        for e in employees:
            table[e.id] = e

        return self.helpImportance(table, id)

    def helpImportance(self, table, id):
        res = 0
        for i in table[id].subordinates:
            res += self.helpImportance(table, i)

        return table[id].importance + res