class Solution(object):
    # 752. Open the Lock
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        # helper function to get childern
        def get_children(lock):
            children = []
            for i in range(4):
                # add 1 to position i
                digit = (int(lock[i]) + 1) % 10
                children.append(lock[:i] + str(digit) + lock[i+1:])
                digit2 = (int(lock[i]) - 1 + 10) % 10 # subtract 1 to position i
                children.append(lock[:i] + str(digit2) + lock[i+1:])
            return children
        
        q = deque()
        visited = set(deadends)
        q.append(["0000", 0])

        while q:
            # pop lock combo and turn count
            lock, turn = q.popleft()
            # if the lock is the target, return turn count
            if lock == target:
                return turn
            for child in get_children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, turn +1])

        return -1


        

        
        
