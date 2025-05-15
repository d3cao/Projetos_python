xf, yf, xi, yi, vi, r1, r2 = map(int, input().strip().split())

distance = ((xi - xf)**2 + (yi - yf)**2)**0.5
distance_enemy = vi*1.5
final_distance = distance + distance_enemy

if final_distance <= (r1+r2) :
    print(f'Y\n')
else :
    print(f'N\n')