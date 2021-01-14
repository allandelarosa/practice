class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "n"
        
        q = deque([root])
        level_order = ""
        
        while q:
            for node in q:
                if not node:
                    level_order += "n,"
                else:
                    level_order += "%d," %(node.val)
                    
            n = len(q)
            while n > 0:
                n -= 1
                curr = q.popleft()
                
                if not curr:
                    continue
                    
                q.append(curr.left)
                q.append(curr.right)
                
        return level_order.strip(',')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        
        if data[0] == 'n':
            return None
        
        root = TreeNode(int(data[0]))
        i = 1
        q = deque([root])
        
        while i < len(data):
            curr = q.popleft()
            if data[i] != 'n':
                curr.left = TreeNode(int(data[i]))
                q.append(curr.left)
                
            i += 1
            if i == len(data):
                break
                
            if data[i] != 'n':
                curr.right = TreeNode(int(data[i]))
                q.append(curr.right)
                
            i += 1
            
        return root
            
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))