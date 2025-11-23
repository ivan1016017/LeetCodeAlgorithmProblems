from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from typing import List


class TopicModeling:
    """Class for performing topic modeling using Scikit-Learn's LDA."""
    
    def __init__(self, n_topics: int = 5, max_features: int = 1000, random_state: int = 42):
        """
        Initialize the TopicModeling class.
        
        Args:
            n_topics: Number of topics to extract.
            max_features: Maximum number of features for vectorization.
            random_state: Random seed for reproducibility.
        """
        self.n_topics = n_topics
        self.max_features = max_features
        self.random_state = random_state
        self.vectorizer = CountVectorizer(stop_words='english', max_features=self.max_features)
        self.lda_model = LatentDirichletAllocation(n_components=self.n_topics, random_state=self.random_state)
    
    def preprocess_and_vectorize(self, documents: List[str]):
        """
        Preprocess and vectorize the input documents.
        
        Args:
            documents: List of text documents.
            
        Returns:
            Document-term matrix.
        """
        doc_term_matrix = self.vectorizer.fit_transform(documents)
        return doc_term_matrix
    
    def fit(self, documents: List[str]):
        """
        Fit the LDA model to the input documents.
        
        Args:
            documents: List of text documents.
        """
        doc_term_matrix = self.preprocess_and_vectorize(documents)
        self.lda_model.fit(doc_term_matrix)
    
    def get_topics(self, n_words: int = 10) -> List[List[str]]:
        """
        Extract topics and their top words.
        
        Args:
            n_words: Number of top words to display per topic.
            
        Returns:
            List of topics with their top words.
        """
        topics = []
        feature_names = self.vectorizer.get_feature_names_out()
        print(feature_names, len(feature_names))
        
        for topic_idx, topic in enumerate(self.lda_model.components_):
            print(topic)
            print(topic.argsort()[:-n_words - 1:-1])
            
            top_words = [feature_names[i] for i in topic.argsort()[:-n_words - 1:-1]]
            topics.append(top_words)
        return topics
    
    def print_topics(self, n_words: int = 10):
        """
        Print the topics and their top words.
        
        Args:
            n_words: Number of top words to display per topic.
        """
        topics = self.get_topics(n_words)
        for idx, topic in enumerate(topics):
            print(f"Topic {idx + 1}: {', '.join(topic)}")


# Example usage
if __name__ == "__main__":
    # Sample documents
    documents = [
        "Machine learning algorithms are used for data analysis and prediction",
        "Deep learning neural networks process large amounts of data",
        "Python programming language is popular for machine learning",
        "Natural language processing helps computers understand human language",
        "Computer vision enables machines to interpret visual information",
        "Reinforcement learning agents learn through trial and error",
        "Data science combines statistics and programming for insights",
        "Artificial intelligence systems can solve complex problems",
        "Big data analytics requires distributed computing frameworks",
        "Neural networks mimic biological brain structure and function"
    ]
    
    # Initialize and fit the topic modeling class
    topic_modeling = TopicModeling(n_topics=3)
    topic_modeling.fit(documents)
    
    # Print the topics
    print("\nExtracted Topics:")
    topic_modeling.print_topics(n_words=2)