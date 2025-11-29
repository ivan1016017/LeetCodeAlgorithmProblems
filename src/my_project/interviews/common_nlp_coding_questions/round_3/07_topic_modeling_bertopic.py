from bertopic import BERTopic
from typing import List


class TopicModelingBERT:
    """Class for performing topic modeling using BERTopic."""
    
    def __init__(self, n_topics: int = 3, language: str = "english", min_topic_size: int = 2):
        """
        Initialize the TopicModelingBERT class.
        
        Args:
            n_topics: Number of topics to extract (None for automatic).
            language: Language of the documents.
            min_topic_size: Minimum size of topics.
        """
        self.n_topics = n_topics
        self.topic_model = BERTopic(
            language=language,
            calculate_probabilities=True,
            verbose=True,
            nr_topics=n_topics if n_topics > 0 else "auto",
            min_topic_size=min_topic_size
        )
        self.topics = None
        self.probs = None
    
    def fit(self, documents: List[str]):
        """
        Fit the BERTopic model to the input documents.
        
        Args:
            documents: List of text documents.
        """
        self.topics, self.probs = self.topic_model.fit_transform(documents)
    
    def get_topics(self, n_words: int = 10) -> List[List[str]]:
        """
        Extract topics and their top words.
        
        Args:
            n_words: Number of top words to display per topic.
            
        Returns:
            List of topics with their top words.
        """
        topics = []
        topic_info = self.topic_model.get_topic_info()
        
        for topic_id in topic_info['Topic']:
            if topic_id == -1:  # Skip outlier topic
                continue
            topic_words = self.topic_model.get_topic(topic_id)
            if topic_words:
                top_words = [word for word, _ in topic_words[:n_words]]
                topics.append(top_words)
        
        return topics
    
    def print_topics(self, n_words: int = 10):
        """
        Print the topics and their top words.
        
        Args:
            n_words: Number of top words to display per topic.
        """
        topic_info = self.topic_model.get_topic_info()
        print(f"Total topics found: {len(topic_info)}")
        print(f"Topic distribution:\n{topic_info[['Topic', 'Count']]}\n")
        
        for _, row in topic_info.iterrows():
            topic_id = row['Topic']
            count = row['Count']
            
            topic_words = self.topic_model.get_topic(topic_id)
            if topic_words:
                top_words = [word for word, _ in topic_words[:n_words]]
                label = "Outliers" if topic_id == -1 else f"Topic {topic_id}"
                print(f"{label} ({count} docs): {', '.join(top_words)}")


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
    # Using min_topic_size=2 for small datasets
    topic_modeling = TopicModelingBERT(n_topics=3, min_topic_size=2)
    topic_modeling.fit(documents)
    
    # Print the topics
    print("\nExtracted Topics:")
    topic_modeling.print_topics(n_words=5)