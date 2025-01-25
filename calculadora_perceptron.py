import matplotlib.pyplot as plt
import numpy as np

points_coord = ((1, 0, 0), (1, 0, 2), (1, 2, 0), (1, 2, 2))
tax = 0.2
wi = [-1, 1, 1]
t = [0, 0, 1, 1]
max_iterations = 10

def sign(x, epsilon=1e-6):
    return 1 if x > epsilon else 0

all_w = [wi[:]]

for it in range(max_iterations):
    print(f"[{it+1}] Ciclo")
    prev_w = wi[:]
    for p, (x0, x1, x2) in enumerate(points_coord):
        inside_f = (wi[0] * 1) + (wi[1] * x1) + (wi[2] * x2)
        sout = sign(inside_f)
        print(f"\t[P{p+1}] Sout = f(w0x0 + w1x1 + w2x2) = f({wi[0]:.2f}*{1} + {wi[1]:.2f}*{x1} + {wi[2]:.2f}*{x2}) = f({inside_f:.2f}) = {sout}")
        if sout != t[p]:
            for i in range(3):
                new_w = wi[i] + (t[p]-sout) * points_coord[p][i] * tax 
                print(f"\t\tw{i}_new = w{i} + (t - s) * x{i} * tax = {wi[i]:.2f} + ({t[p]} - {sout}) * {points_coord[p][i]} * {tax:.2f} = {new_w:.2f}")
                wi[i] = new_w
    
    all_w.append(wi[:])

    # Verificação de parada: se os pesos não mudaram, parar
    if np.array_equal(prev_w, wi):
        print(f"Convergência atingida na iteração {it+1}")
        break

fig, ax = plt.subplots()

for i, (x0, x1, x2) in enumerate(points_coord):
    if t[i] == 0:
        ax.scatter(x1, x2, color="red", label="Classe 0" if i == 0 else "")
    else:
        ax.scatter(x1, x2, color="blue", label="Classe 1" if i == 2 else "")

x_vals = np.linspace(-1, 3, 100)
for i, (w0, w1, w2) in enumerate(all_w[:-1]):
    if w2 != 0:
        y_vals = -(w0 + w1 * x_vals) / w2
        ax.plot(x_vals, y_vals, label=f"Reta {i}", alpha=0.7)

ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize="small")
ax.grid(True, linestyle="--", alpha=0.6)

plt.title("Pontos e Retas ao Longo das Iterações")
plt.tight_layout()
plt.show()
