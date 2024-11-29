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
        def get_children(mutation):
            children = []
            
            for i in range(len(mutation)):
                for char in "ACGT":
                    mutated_gene = mutation[:i] + char + mutation[i+1:]
                    children.append(mutated_gene)
            return children
        
        # convert startGene to a set
        visited = set([startGene])
        queue = deque([startGene])
        mutations = 0
        
        # Perform BFS.
        while queue:
            # Iterate over all mutations at the current level
            for i in range(len(queue)):
                # Pop the current state from the queue.
                curr = queue.popleft()
                
                # If the current state is the target, return the number of turns taken.
                if curr == endGene:
                    return mutations
                
                # Generate all possible next states (children) and process them.
                for child in get_children(curr):
                    # If the child is not visited and in bank, add it to the queue and mark it as visited.
                    if child not in visited and child in bank:
                        queue.append(child)
                        visited.add(child)
            
            # Increment mutations after processing all states at the current level.
            mutations += 1
        
        # If the target is not reached after processing all possibilities, return -1.
        return -1