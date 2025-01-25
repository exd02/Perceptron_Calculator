
points_coord = ((1,0,0), (1,2,0), (1,0,2), (1,2,2))
tax = .5
wi = [-1,1,1]
t = [0,0,0,1]
max_iterations = 10

# evitar x<0 não funcionar devido ao funcionamento dos floats
def sign(x, epsilon=1e-6):
    return (1 if x > epsilon else 0)

for it in range(max_iterations):
    print(f"[{it+1}] Iteração")
    p = 0
    for x0,x1,x2 in points_coord:
        inside_f = (wi[0]*1) + (wi[1]*x1) + (wi[2]*x2)
        sout = sign(inside_f)
        print(f"\t[P{p+1}] Sout = f(w0x0 + w1x1 + w2x2) = f({wi[0]:.2f}*{1} + {wi[1]:.2f}*{x1} + {wi[2]:.2f}*{x2}) = f({inside_f:.2f}) = {sout}")
        if sout != t[p]:
            for i in range(3):
                new_w = wi[i] + (t[p]-sout) * points_coord[p][i] * tax 
                print(f"\t\tw{i}_new = w{i} + (t - s) * x{i} * tax = {wi[i]:.2f} + ({t[p]} - {sout}) * {points_coord[p][i]} * {tax:.2f} = {new_w:.2f}")
                wi[i] = new_w
        
        p = p + 1