import collections

def count_corpus(tokens):
        if len(tokens)==0 or isinstance(tokens[0], list):
            tokens = [token for line in tokens for token in line] # 展平tokens
        return collections.Counter(tokens)

class Vocab:
    def __init__(self, tokens=None, min_freq=0, reserved_tokens=None):
        if tokens == None:
            tokens = []
        if reserved_tokens == None:
            reserved_tokens = []
        
        counter = count_corpus(tokens)
        
        self._token_freqs = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        
        self.index_to_token = ['<unk>'] + reserved_tokens
        self.token_to_index = {token:index for index, token in enumerate(self.index_to_token)}
        
        for token, freq in self._token_freqs:
            if freq < min_freq:
                break
            self.index_to_token.append(token)
            self.token_to_index[token] = len(self.index_to_token) - 1
    
    def __len__(self):
        return len(self.index_to_token)
    
    def __getitem__(self, tokens):
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_index.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]
     
    @property
    def unk(self):
        return 0
    
    @property
    def token_freqs(self):
        return self._token_freqs