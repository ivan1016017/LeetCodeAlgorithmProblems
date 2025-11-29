from typing import Dict, List
import math
from collections import Counter
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class TextSimilarity:
    """Class for computing text similarity using TF-IDF and cosine similarity."""
    
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
        Uses scikit-learn's formula: log((1 + n) / (1 + df)) + 1
        
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
        
        # Use scikit-learn's IDF formula for consistency
        idf = {token: math.log((1 + num_docs) / (1 + freq)) + 1 
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
    
    def cosine_similarity_manual(self, vec1: Dict[str, float], vec2: Dict[str, float]) -> float:
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
    
    def tfidf_similarity_manual(self, text1: str, text2: str, corpus: List[str] = None) -> float:
        """
        Compute similarity using manual TF-IDF and cosine similarity.
        
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
        return self.cosine_similarity_manual(tfidf1, tfidf2)
    
    def tfidf_similarity_sklearn(self, text1: str, text2: str, corpus: List[str] = None) -> float:
        """
        Compute similarity using scikit-learn TF-IDF and cosine similarity.
        
        Args:
            text1: First text document
            text2: Second text document
            corpus: Optional corpus for IDF calculation
            
        Returns:
            Similarity score (0 to 1)
        """
        # Build corpus if not provided
        if corpus is None:
            documents = [text1, text2]
        else:
            documents = corpus + [text1, text2]
        
        # Create TF-IDF vectorizer with L2 normalization (default)
        vectorizer = TfidfVectorizer(norm='l2')
        tfidf_matrix = vectorizer.fit_transform(documents)
        print(tfidf_matrix)
        
        # Get the TF-IDF vectors for text1 and text2
        vec1 = tfidf_matrix[-2]
        vec2 = tfidf_matrix[-1]
        
        # Compute cosine similarity
        similarity = cosine_similarity(vec1, vec2)[0][0]
        return similarity


# Example usage
if __name__ == "__main__":
    sim = TextSimilarity()
    
    doc1 = "The quick brown fox jumps over the lazy dog"
    doc2 = "The lazy dog sleeps under the tree"
    
    # Manual TF-IDF implementation
    score_manual = sim.tfidf_similarity_manual(doc1, doc2)
    print(f"Manual TF-IDF Cosine Similarity: {score_manual:.4f}")
    
    # Scikit-learn TF-IDF implementation
    score_sklearn = sim.tfidf_similarity_sklearn(doc1, doc2)
    print(f"Scikit-learn TF-IDF Cosine Similarity: {score_sklearn:.4f}")
    
    print(f"\nDifference: {abs(score_manual - score_sklearn):.4f}")