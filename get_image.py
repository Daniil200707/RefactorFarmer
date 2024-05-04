import numpy as np

INPUT_DIM = 1
OUT_DIM = 11
H_DIM = 10

x = np.random.randn(INPUT_DIM)

W1 = np.random.randn(INPUT_DIM, H_DIM)

b1 = np.random.randn(H_DIM)

W2 = np.random.randn(H_DIM, OUT_DIM)

b2 = np.random.randn(OUT_DIM)

def relu(t):
    return np.maximum(t, 0)

def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)

def predict(x):
    t1 = x @ W1 + b1
    h1 = relu(t1)
    t2 = h1 @ W2 + b2
    z = softmax(t2)
    return z

probs = predict(x)
pred_class = np.argmax(probs)
class_names = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('Predicted class:', f'{class_names[pred_class]}% sun')
