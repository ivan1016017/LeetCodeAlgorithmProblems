from typing import Dict, List, Set
import math
from collections import Counter
import re


class TextSimilarity:
    """Class for computing text similarity using various methods."""
    
    def __init__(self):
        self.idf_cache: Dict[str, float] = {}
    
    def preprocess(self, text: str) -> List[str]:
        """
        Preprocess text: lowercase, remove punctuation, tokenize.
        
        Args:
            text: Input text string
            
        Returns:
            List of tokens
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = text.split()
        return tokens
    
    def compute_tf(self, tokens: List[str]) -> Dict[str, float]:
        """
        Compute Term Frequency (TF) for tokens.
        
        Args:
            tokens: List of tokens
            
        Returns:
            Dictionary mapping terms to their TF values
        """
        token_count = Counter(tokens)
        total_tokens = len(tokens)
        
        tf = {token: count / total_tokens for token, count in token_count.items()}
        return tf
    
    def compute_idf(self, documents: List[List[str]]) -> Dict[str, float]:
        """
        Compute Inverse Document Frequency (IDF) for a corpus.
        
        Args:
            documents: List of tokenized documents
            
        Returns:
            Dictionary mapping terms to their IDF values
        """
        num_docs = len(documents)
        doc_freq: Dict[str, int] = Counter()
        
        for doc in documents:
            unique_tokens = set(doc)
            for token in unique_tokens:
                doc_freq[token] += 1
        
        idf = {token: math.log(num_docs / (freq + 1)) + 1 
               for token, freq in doc_freq.items()}
        
        return idf
    
    def compute_tfidf(self, tokens: List[str], idf: Dict[str, float]) -> Dict[str, float]:
        """
        Compute TF-IDF scores.
        
        Args:
            tokens: List of tokens
            idf: IDF dictionary
            
        Returns:
            Dictionary mapping terms to their TF-IDF values
        """
        tf = self.compute_tf(tokens)
        tfidf = {token: tf_val * idf.get(token, 0) 
                 for token, tf_val in tf.items()}
        return tfidf
    
    def cosine_similarity(self, vec1: Dict[str, float], vec2: Dict[str, float]) -> float:
        """
        Compute cosine similarity between two vectors.
        
        Args:
            vec1: First vector as dictionary
            vec2: Second vector as dictionary
            
        Returns:
            Cosine similarity score (0 to 1)
        """
        # Get common terms
        common_terms = set(vec1.keys()) & set(vec2.keys())
        
        if not common_terms:
            return 0.0
        
        # Compute dot product
        dot_product = sum(vec1[term] * vec2[term] for term in common_terms)
        
        # Compute magnitudes
        magnitude1 = math.sqrt(sum(val ** 2 for val in vec1.values()))
        magnitude2 = math.sqrt(sum(val ** 2 for val in vec2.values()))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        
        return dot_product / (magnitude1 * magnitude2)
    
    def jaccard_similarity(self, tokens1: List[str], tokens2: List[str]) -> float:
        """
        Compute Jaccard similarity between two token lists.
        
        Args:
            tokens1: First list of tokens
            tokens2: Second list of tokens
            
        Returns:
            Jaccard similarity score (0 to 1)
        """
        set1 = set(tokens1)
        set2 = set(tokens2)
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        if union == 0:
            return 0.0
        
        return intersection / union
    
    def tfidf_similarity(self, text1: str, text2: str, corpus: List[str] = None) -> float:
        """
        Compute similarity using TF-IDF and cosine similarity.
        
        Args:
            text1: First text document
            text2: Second text document
            corpus: Optional corpus for IDF calculation
            
        Returns:
            Similarity score (0 to 1)
        """
        tokens1 = self.preprocess(text1)
        tokens2 = self.preprocess(text2)
        
        # Build corpus if not provided
        if corpus is None:
            corpus_tokens = [tokens1, tokens2]
        else:
            corpus_tokens = [self.preprocess(doc) for doc in corpus]
            if tokens1 not in corpus_tokens:
                corpus_tokens.append(tokens1)
            if tokens2 not in corpus_tokens:
                corpus_tokens.append(tokens2)
        
        # Compute IDF
        idf = self.compute_idf(corpus_tokens)
        
        # Compute TF-IDF vectors
        tfidf1 = self.compute_tfidf(tokens1, idf)
        tfidf2 = self.compute_tfidf(tokens2, idf)
        
        # Compute cosine similarity
        return self.cosine_similarity(tfidf1, tfidf2)
    
    def simple_similarity(self, text1: str, text2: str, method: str = "cosine") -> float:
        """
        Compute similarity using simple term frequency.
        
        Args:
            text1: First text document
            text2: Second text document
            method: "cosine" or "jaccard"
            
        Returns:
            Similarity score (0 to 1)
        """
        tokens1 = self.preprocess(text1)
        tokens2 = self.preprocess(text2)
        
        if method == "jaccard":
            return self.jaccard_similarity(tokens1, tokens2)
        else:  # cosine
            tf1 = self.compute_tf(tokens1)
            tf2 = self.compute_tf(tokens2)
            return self.cosine_similarity(tf1, tf2)


# Example usage
if __name__ == "__main__":
    sim = TextSimilarity()
    
    # Example 1: Simple cosine similarity
    doc1 = "The quick brown fox jumps over the lazy dog"
    doc2 = "The lazy dog sleeps under the tree"
    
    score = sim.simple_similarity(doc1, doc2, method="cosine")
    print(f"Cosine Similarity: {score:.4f}")
    
    # Example 2: Jaccard similarity
    score = sim.simple_similarity(doc1, doc2, method="jaccard")
    print(f"Jaccard Similarity: {score:.4f}")
    
    # Example 3: TF-IDF similarity
    corpus = [
        "The quick brown fox jumps over the lazy dog",
        "The lazy dog sleeps under the tree",
        "A quick brown dog runs in the park"
    ]
    
    score = sim.tfidf_similarity(doc1, doc2, corpus)
    print(f"TF-IDF Cosine Similarity: {score:.4f}")
    
    # Example 4: Identical documents
    score = sim.tfidf_similarity(doc1, doc1)
    print(f"Identical Document Similarity: {score:.4f}")