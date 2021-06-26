# TC: O(N x M) where N is the size of the hashmap which maps every sentence in input with its frequency and N is the input sentences in the i/p list. 
#     For every input sentence in the input list, we iterate over the whole hashmap. 
# SC: O(N) where N is the size of the hashmap. The size of the heap is also considered, but it will be constant at any given time, as we store only 3 sentences in it. 

class AutocompleteSystem:
    class _heapcomparator(tuple): 
        def __lt__(self, other): 
            time1, sentence1 = self
            time2, sentence2 = other
            if time1 == time2: 
                return sentence1 > sentence2
            return time1 < time2

    def __init__(self, sentences: List[str], times: List[int]):
        self.hmap = {}
        self.sentence = ""
        # print(len(sentences))
        for i in range(len(sentences)): 
            self.hmap[sentences[i]] = self.hmap.get(sentences[i],0) + times[i]            
        
    def input(self, c: str) -> List[str]:
#         If the input string is #, we need to strore the string in db i.e hashmap and return an empty array with initializing initial sentence to a new string
        if c == '#': 
            string = str(self.sentence)
            self.hmap[string] = self.hmap.get(string,0) + 1
            self.sentence = ""
            return []
#         if input string is not #, we need to append to current sentence
        self.sentence += c
#     Return the top 3 hot sentences with prefix as the current sentence.
        string = str(self.sentence)
    
        heap = []
        
        for keys in self.hmap.keys(): 
            if keys.startswith(self.sentence):
                heapq.heappush(heap, self._heapcomparator((self.hmap.get(keys), keys)))
            if len(heap) > 3: 
                heapq.heappop(heap)
        result = []
        
        i = 2
        while heap: 
            result.insert(0, heapq.heappop(heap)[1])
            i -= 1
        return result
