import random
import matplotlib.pyplot as plt

def estimar_pi(n_pontos):
    dentro = 0
    x_dentro, y_dentro = [], []
    x_fora, y_fora = [], []

    for _ in range(n_pontos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            dentro += 1
            x_dentro.append(x)
            y_dentro.append(y)
        else:
            x_fora.append(x)
            y_fora.append(y)

    pi_estimado = 4 * dentro / n_pontos

    # Visualização
    plt.figure(figsize=(6, 6))
    plt.scatter(x_dentro, y_dentro, s=1, color='blue', label='Dentro do círculo')
    plt.scatter(x_fora, y_fora, s=1, color='red', label='Fora do círculo')
    plt.title(f'Estimativa de π ≈ {pi_estimado:.5f}')
    plt.legend()
    plt.axis('equal')
    plt.show()

    return pi_estimado

if __name__ == "__main__":
    n = int(input("Quantos pontos deseja gerar? "))
    pi = estimar_pi(n)
    print(f"Estimativa de π com {n} pontos: {pi}")
