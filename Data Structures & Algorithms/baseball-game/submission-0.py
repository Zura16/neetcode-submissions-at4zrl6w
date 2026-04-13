class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # My Solution: T-O(n) S-O(n)
        record = []
        for a in operations:
            if a == "+":
                record.append(record[-1] + record[-2])
            elif a == "D":
                record.append(2 * record[-1])
            elif a == "C":
                record.pop()
            else:
                record.append(int(a))
            
        return sum(record)
