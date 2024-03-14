def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """

    # Get the number of boxes
    n = len(boxes)
    
    # Create a list to keep track of visited boxes, initialized with False
    visited = [False] * n
    
    # Mark the first box as visited (box 0 is unlocked initially)
    visited[0] = True
    
    # Initialize a queue for BFS with the first box
    queue = [0]

    # Perform BFS
    while queue:
        # Get the current box from the queue
        current_box = queue.pop(0)
        
        # Iterate over the keys in the current box
        for key in boxes[current_box]:
            # Check if the key is valid (within the range of boxes) and if the box is not visited
            if 0 <= key < n and not visited[key]:
                # Mark the box corresponding to the key as visited
                visited[key] = True
                # Add the key's box to the queue for further exploration
                queue.append(key)
