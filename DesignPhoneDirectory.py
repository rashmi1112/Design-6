# TC: The contents of hashset and the queue are initialized in the constructor with the TC of O(N). But since they are only initialized in constructor, they won't be considered for the calculation of TC. 
# Therefore, the total TC of the functions are as follows: 
#    1. get() --> O(1) since to get any element, we just poll the first element from the queue ni constant time.
#    2. check() --> O(1) since we are using hashset to check if a particular slot is taken or not. 
#    3. release() --> O(1) since adding a slot into the hashset and the queue requires constant time. 

# SC: O(N) as we use the hashset and queue to store all the valid slots at any given time.

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.hset = set() 
        self.queue = collections.deque()
        for i in range(maxNumbers):
            self.hset.add(i)
            self.queue.append(i)

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.queue: 
            number = self.queue.popleft()
            self.hset.remove(number)
            return number
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        if number in self.hset: 
            return True
        return False

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.hset: 
            return 
        
        self.hset.add(number)
        self.queue.append(number)
