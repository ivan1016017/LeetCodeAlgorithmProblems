import torch
import torch.nn as nn
import torch.optim as optim
import random

class CharRNN(nn.Module):
    def __init__(self, vocab_size, hidden_size=128, num_layers=1):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.rnn = nn.RNN(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)
        self.num_layers = num_layers
        self.hidden_size = hidden_size

    def forward(self, x, hidden):
        x = self.embedding(x)
        out, hidden = self.rnn(x, hidden)
        out = self.fc(out)
        return out, hidden

    def init_hidden(self, batch_size):
        return torch.zeros(self.num_layers, batch_size, self.hidden_size)

def build_vocab(text):
    chars = sorted(set(text))
    char2idx = {ch: i for i, ch in enumerate(chars)}
    idx2char = {i: ch for i, ch in enumerate(chars)}
    return char2idx, idx2char

def prepare_data(text, char2idx, seq_length):
    data = []
    for i in range(len(text) - seq_length):
        seq = text[i:i+seq_length]
        target = text[i+1:i+seq_length+1]
        seq_idx = [char2idx[ch] for ch in seq]
        target_idx = [char2idx[ch] for ch in target]
        data.append((seq_idx, target_idx))
    return data

def train(text, seq_length=40, epochs=50, lr=0.005):
    char2idx, idx2char = build_vocab(text)
    vocab_size = len(char2idx)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = CharRNN(vocab_size).to(device)
    data = prepare_data(text, char2idx, seq_length)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    for epoch in range(epochs):
        total_loss = 0
        random.shuffle(data)
        for seq_idx, target_idx in data:
            inputs = torch.tensor([seq_idx], dtype=torch.long).to(device)
            targets = torch.tensor([target_idx], dtype=torch.long).to(device)
            hidden = model.init_hidden(1).to(device)
            outputs, _ = model(inputs, hidden)
            loss = criterion(outputs.view(-1, vocab_size), targets.view(-1))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if (epoch+1) % 10 == 0:
            print(f"Epoch {epoch+1}, Loss: {total_loss/len(data):.4f}")
    return model, char2idx, idx2char, device

def generate(model, char2idx, idx2char, seed, length=200, temperature=1.0, device='cpu'):
    model.eval()
    chars = list(seed)
    hidden = model.init_hidden(1).to(device)
    for _ in range(length):
        input_idx = torch.tensor([[char2idx.get(chars[-1], 0)]], dtype=torch.long).to(device)
        output, hidden = model(input_idx, hidden)
        output = output[0, -1] / temperature
        probs = torch.softmax(output, dim=0).detach().cpu().numpy()
        next_idx = random.choices(range(len(probs)), weights=probs)[0]
        chars.append(idx2char[next_idx])
    return ''.join(chars)

if __name__ == "__main__":
    corpus = (
        "The quick brown fox jumps over the lazy dog. "
        "Machine learning is fun. "
        "PyTorch makes building neural networks easy. "
        "Text generation with RNNs is simple."
    ) * 5
    model, char2idx, idx2char, device = train(corpus, seq_length=40, epochs=50)
    print("\nGenerated text:\n")
    print(generate(model, char2idx, idx2char, seed="The quick", length=200, temperature=0.8, device=device))