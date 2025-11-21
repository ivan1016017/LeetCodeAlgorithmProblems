from typing import Dict 
from collections import Counter
import re

class WordFrequencyCounter:

    def count_word_frequency_counter(self, text: str) -> Dict[str, int]:
        """
        Count the frequency of each word in a text document.
        
        Args:
            text: Input text document
            
        Returns:
            Dictionary with word frequencies
        """

        words = re.findall(r'\b\w+\b', text)

        print(words)

        word_freq = Counter(text)   

        

        return word_freq


    def count_word_frequency_counter_with_stop_words(self, text: str) -> Dict[str, int]:
        """
        Count the frequency of each word in a text document.
        
        Args:
            text: Input text document
            
        Returns:
            Dictionary with word frequencies
        """

        words = re.split(r'[,.]|\s', text)

        print(words)

        word_freq = Counter(words)

        return word_freq


# Example usage
if __name__ == "__main__":
    counter = WordFrequencyCounter()
    
    text = """
    Natural language processing (NLP) is a subfield of linguistics, 
    computer science, and artificial intelligence concerned with the 
    interactions between computers and human language.
    """

    print(counter.count_word_frequency_counter(text=text))
    print(counter.count_word_frequency_counter_with_stop_words(text=text))