class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1

        # helper function to get childern
        def get_children(original_string):
            children = []
            for i in range(8):
            	for nucleotide in "ACGT":
                	child = original_string[:i] + nucleotide + original_string[i + 1:]
                	children.append(child)
            return children
        
        q = deque()
        visited = set()
        q.append([startGene, 0])

        while q:
            gene, turn = q.popleft()
            # if the gene is the endGene, return turn count
            if gene == endGene:
                return turn
            for child in get_children(gene):
                if (child not in visited) and (child in bank):
                    visited.add(child)
                    q.append((child, turn +1))

        return -1
