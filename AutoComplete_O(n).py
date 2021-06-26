# TC: O(n x m) where n is the avg number of sentences starting from an input string m. These m strings would be stored in the hashmap. Iterating over this hashmap would take O(n), 
#     which is much better than the previous algorithm with TC O(N x M). 
# SC: O(L x N) where L is the average length of the strings in the database and N is the number of strings present in the db.

class TrieNode:
    def __init__(self):
        self.hmap_children = {}
        self.hmap_prefix_sentences = {}

class AutocompleteSystem:
    
    class HeapComparator(tuple): 
        def __lt__(self, other): 
            sentence1, time1 = self
            sentence2, time2 = other
            if time1 == time2: 
                return sentence1 > sentence2
            return time1 < time2
                                
    
    def insert(self, sentence:str, times:int):
        curr = self.root
        for i in sentence: 
            if i not in curr.hmap_children.keys(): 
                curr.hmap_children[i] = TrieNode()
            curr = curr.hmap_children.get(i)
            curr.hmap_prefix_sentences[sentence] = curr.hmap_prefix_sentences.get(sentence, 0) + times

    def search(self, input_str : str) -> dict:
        curr = self.root
        for i in input_str: 
            if i not in curr.hmap_children.keys(): 
                return {}
            curr = curr.hmap_children.get(i)

        return curr.hmap_prefix_sentences
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.sentence = ""
        for i in range(len(sentences)): 
            self.insert(sentences[i], times[i])

    def input(self, c: str) -> List[str]:
        if c == '#': 
            string = str(self.sentence)
            self.insert(string, 1)
            self.sentence = ""
            return []
        
        self.sentence = str(self.sentence + c)
        hmap = self.search(self.sentence)
        heap = []
        for key in hmap.keys():
            if key.startswith(self.sentence):
                heapq.heappush(heap, self.HeapComparator((key, hmap.get(key))))
                if len(heap) > 3: 
                    heapq.heappop(heap)
        
        result = []
        while heap: 
            result.insert(0, heapq.heappop(heap)[0])
        
        return result
