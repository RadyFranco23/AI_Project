"""Veremos como funciona la tokenizacion y el embedding"""
"""Que es tokenizacion: Es el proceso de dividir texto en unidades llamadas tokens (palabras o subpalabras) y asignarles un índice numérico."""
"""Veremos la prueba semanal de entrenar un modelo NPL para clasificar tweets"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchtext import data, datasets
from spacy.lang.en import English
from torchtext.data import BucketIterator


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#Crear tokenizer con spacy

nlp = English()
tokenizer = nlp.tokenizer

def spacy_tokenizer(text):
    return [tok.text.lower() for tok in nlp(text)]

#campos de texto y etiqueta
TEXT = data.Field(
    tokenize=spacy_tokenizer,
    lower=True,
    include_lengths=True,
    batch_first=True
)

LABEL = data.LabelField(dtype=torch.float)

#Cargar dataset

train_data, test_data = datasets.IMDB.splits(TEXT, LABEL)

print(f"Ejemplos de entrenamiento: {len(train_data)}")
print(f"Ejemplos de prueba: {len(test_data)}")

# Crear el vocabulario 

TEXT.build_vocab(
    train_data,
    max_size = 25000
)

LABEL.build_vocab(train_data)

# Crear Iteradores

train_iter, test_iter = BucketIterator.splits(
    (train_data, test_data),
    batch_sizes=(64,64),
    sort_within_batch=True,
    device=device
)

#Creando red Lstm para clasificar sentimientos de comentarios o post

class LSTM(nn.Module):

    def __init__(self,  vocab_size, embed_size, hidden_size, output_dim, pad_idx):
        super().__init__()

        self.hidden_size = hidden_size
        self.num_layers = 1

        self.red = nn.Sequential(
            nn.Embedding(vocab_size,embed_size, padding_idx=pad_idx), # Aqui lo mismo pero tienes que estar relacionado al dataseet
            nn.LSTM(embed_size, hidden_size, batch_first=True) # si queremos podemos usar numeros en ves de las variables
        )

        self.dropout = nn.Dropout(0.5)

        self.redfc = nn.Sequential(
            nn.Linear(hidden_size,output_dim), 
        )


    def forward(self, x, h0=None):
        emb = self.red[0](x)
        emb = self.dropout(emb)

        # obtener batch_size automáticamente
        batch_size = emb.size(0)

        # si no se pasó h0, se inicializa (h0, c0)
        if h0 is None:
            h0 = torch.zeros(self.num_layers, batch_size, self.hidden_size, device=emb.device)
            c0 = torch.zeros(self.num_layers, batch_size, self.hidden_size, device=emb.device)
        else:
            # si viene como solo h0, completamos la tupla
            if isinstance(h0, torch.Tensor):
                c0 = torch.zeros_like(h0)
            else:
                h0, c0 = h0

        # salida del LSTM
        out, (hn, cn) = self.red[1](emb, (h0, c0))

        # tomamos la última salida de la secuencia
        out = out[:, -1, :]  # batch_first=True, así que último paso es [:, -1, :]

        out = self.dropout(out)
        logits = self.redfc(out)

        return logits
    
#Inicializar modelo

vocab_size = len(TEXT.vocab)
embed_size = 100
hidden_size = 128
output_dim = 1
pad_idx = TEXT.vocab.stoi[TEXT.pad_token]   

LSTModel = LSTM(vocab_size, embed_size, hidden_size, output_dim, pad_idx).to(device)

#Fase de entrenamiento

criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(LSTModel.parameters(), lr=0.001)

def binary_accuracy(preds, y):
    rounded = torch.round(torch.sigmoid(preds))
    correct = (rounded == y).float()
    return correct.sum() / len(correct)

N_EPOCHS = 3

for epoch in range(N_EPOCHS):
    LSTModel.train()
    epoch_loss = 0
    epoch_acc = 0
    
    for batch in train_iter:
        optimizer.zero_grad()
        text= batch.text
        predictions = LSTModel(text[0]).squeeze(1)
        loss = criterion(predictions, batch.label)
        acc = binary_accuracy(predictions, batch.label)
        
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item()
        epoch_acc += acc.item()
    
    print(f"Epoch {epoch+1}: Loss={epoch_loss/len(train_iter):.3f}, Acc={epoch_acc/len(train_iter):.3f}")


# Evaluación rápida

LSTModel.eval()
with torch.no_grad():
    acc_total = 0
    for batch in test_iter:
        text = batch.text
        predictions = LSTModel(text[0]).squeeze(1)
        acc = binary_accuracy(predictions, batch.label)
        acc_total += acc.item()
    print(f"Exactitud en test: {acc_total/len(test_iter):.2%}")


#  Predicción con texto nuevo

def predecir_sentimiento(model, texto):
    model.eval()
    tokens = [tok.text.lower() for tok in tokenizer(texto)]
    tensor = torch.LongTensor([TEXT.vocab.stoi[t] for t in tokens]).unsqueeze(0).to(device)
    prediction = torch.sigmoid(model(tensor))
    return "Positivo" if prediction.item() > 0.5 else "Negativo"

print(predecir_sentimiento(LSTModel, "This movie was great, I loved it!"))
print(predecir_sentimiento(LSTModel, "This movie was terrible and boring."))