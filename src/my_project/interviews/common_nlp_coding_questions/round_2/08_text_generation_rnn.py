import torch
import torch.nn as nn
import torch.optim as optim
from typing import Dict, List
import random


class CharRNN(nn.Module):
    """Character-level RNN for text generation."""
    
    def __init__(self, vocab_size: int, hidden_size: int = 128, num_layers: int = 2):
        """
        Initialize the RNN model.
        
        Args:
            vocab_size: Size of character vocabulary
            hidden_size: Size of hidden layers
            num_layers: Number of RNN layers
        """
        super().__init__()  # Cleaner - Python 3+ automatically infers the class
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.rnn = nn.RNN(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)
    
    def forward(self, x, hidden):
        """
        Forward pass.
        
        Args:
            x: Input tensor of shape (batch_size, seq_length)
            hidden: Hidden state
            
        Returns:
            Output and hidden state
        """
        x = self.embedding(x)
        out, hidden = self.rnn(x, hidden)
        out = self.fc(out)
        return out, hidden
    
    def init_hidden(self, batch_size: int):
        """Initialize hidden state."""
        return torch.zeros(self.num_layers, batch_size, self.hidden_size)


class TextGenerator:
    """Text generation using PyTorch RNN."""
    
    def __init__(self, hidden_size: int = 128, num_layers: int = 2, 
                 seq_length: int = 100, learning_rate: float = 0.005):
        """
        Initialize text generator.
        
        Args:
            hidden_size: Size of hidden layers
            num_layers: Number of RNN layers
            seq_length: Length of training sequences
            learning_rate: Learning rate for optimizer
        """
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.seq_length = seq_length
        self.learning_rate = learning_rate
        
        self.char_to_idx: Dict[str, int] = {}
        self.idx_to_char: Dict[int, str] = {}
        self.vocab_size = 0
        self.model = None
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    def build_vocab(self, text: str):
        """
        Build character vocabulary from text.
        
        Args:
            text: Training text corpus
        """
        chars = sorted(list(set(text)))
        self.vocab_size = len(chars)
        self.char_to_idx = {ch: i for i, ch in enumerate(chars)}
        self.idx_to_char = {i: ch for i, ch in enumerate(chars)}
        
        # Initialize model
        self.model = CharRNN(self.vocab_size, self.hidden_size, self.num_layers).to(self.device)
    
    def prepare_data(self, text: str) -> List[tuple]:
        """
        Prepare training data sequences.
        
        Args:
            text: Training text
            
        Returns:
            List of (input, target) sequences
        """
        data = []
        for i in range(0, len(text) - self.seq_length):
            seq = text[i:i + self.seq_length]
            target = text[i + 1:i + self.seq_length + 1]
            
            seq_idx = [self.char_to_idx[ch] for ch in seq]
            target_idx = [self.char_to_idx[ch] for ch in target]
            
            data.append((seq_idx, target_idx))
        
        return data
    
    def train(self, text: str, epochs: int = 100, print_every: int = 10):
        """
        Train the model.
        
        Args:
            text: Training text corpus
            epochs: Number of training epochs
            print_every: Print loss every N epochs
        """
        # Build vocabulary
        self.build_vocab(text)
        
        # Prepare data
        data = self.prepare_data(text)
        
        # Setup training
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
        
        print(f"Training on {len(data)} sequences...")
        print(f"Vocabulary size: {self.vocab_size}")
        print(f"Device: {self.device}\n")
        
        # Training loop
        for epoch in range(epochs):
            # Shuffle data
            random.shuffle(data)
            total_loss = 0
            
            for seq_idx, target_idx in data:
                # Convert to tensors
                inputs = torch.tensor([seq_idx], dtype=torch.long).to(self.device)
                targets = torch.tensor([target_idx], dtype=torch.long).to(self.device)
                
                # Initialize hidden state
                hidden = self.model.init_hidden(1).to(self.device)
                
                # Forward pass
                outputs, hidden = self.model(inputs, hidden)
                loss = criterion(outputs.view(-1, self.vocab_size), targets.view(-1))
                
                # Backward pass
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
            
            # Print progress
            if (epoch + 1) % print_every == 0:
                avg_loss = total_loss / len(data)
                print(f"Epoch [{epoch+1}/{epochs}], Loss: {avg_loss:.4f}")
    
    def generate(self, seed: str = None, length: int = 200, temperature: float = 1.0) -> str:
        """
        Generate text using the trained model.
        
        Args:
            seed: Starting text (optional)
            length: Length of text to generate
            temperature: Sampling temperature (higher = more random)
            
        Returns:
            Generated text
        """
        if self.model is None:
            return "Model not trained yet!"
        
        self.model.eval()
        
        with torch.no_grad():
            # Initialize
            if seed:
                chars = list(seed)
            else:
                # Random starting character
                chars = [random.choice(list(self.char_to_idx.keys()))]
            
            hidden = self.model.init_hidden(1).to(self.device)
            
            # Generate characters
            for _ in range(length):
                # Get last character
                char = chars[-1]
                if char not in self.char_to_idx:
                    char = random.choice(list(self.char_to_idx.keys()))
                
                # Convert to tensor
                input_idx = torch.tensor([[self.char_to_idx[char]]], dtype=torch.long).to(self.device)
                
                # Forward pass
                output, hidden = self.model(input_idx, hidden)
                
                # Apply temperature
                output = output.squeeze() / temperature
                probs = torch.softmax(output, dim=0).cpu().numpy()
                
                # Sample next character
                char_idx = torch.multinomial(torch.tensor(probs), 1).item()
                next_char = self.idx_to_char[char_idx]
                
                chars.append(next_char)
            
            return ''.join(chars)


# Example usage
if __name__ == "__main__":
    # Sample corpus (larger corpus works better)
    corpus = """
    The quick brown fox jumps over the lazy dog. The dog was sleeping under a tree.
    A quick brown fox runs through the forest. The forest is full of tall trees.
    Machine learning is a subset of artificial intelligence. Deep learning uses neural networks.
    Neural networks are inspired by biological neurons. The brain processes information efficiently.
    Natural language processing helps computers understand human language. Text generation is fascinating.
    Recurrent neural networks can process sequential data. They maintain hidden states across time steps.
    Training neural networks requires lots of data and computational power. Modern GPUs accelerate training.
    The weather is beautiful today. Birds are singing in the trees. Nature is wonderful and inspiring.
    """ * 5  # Repeat to have more training data
    
    print("=" * 60)
    print("CHARACTER-LEVEL RNN TEXT GENERATION")
    print("=" * 60)
    
    # Initialize generator
    generator = TextGenerator(hidden_size=128, num_layers=2, seq_length=50, learning_rate=0.01)
    
    # Train model
    generator.train(corpus, epochs=100, print_every=20)
    
    print("\n" + "=" * 60)
    print("GENERATED TEXT")
    print("=" * 60)
    
    # Generate text without seed
    print("\n1. Random generation:")
    print(generator.generate(length=200, temperature=0.8))
    
    # Generate text with seed
    print("\n2. Generation with seed 'The quick':")
    print(generator.generate(seed="The quick", length=200, temperature=0.8))
    
    # Generate text with different temperatures
    print("\n3. Generation with high temperature (more random):")
    print(generator.generate(seed="Machine learning", length=150, temperature=1.5))
    
    print("\n4. Generation with low temperature (more deterministic):")
    print(generator.generate(seed="Machine learning", length=150, temperature=0.5))