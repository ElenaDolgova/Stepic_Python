def closest_mod_5(x):
    return x + (5 - x % 5) * (x % 5 != 0)

print(closest_mod_5(4))

def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(0, 0, 31),s(11, 10),s(11, 10, b=10),s(5, 5, 5, 5, 1),s(21),s(11, 10, 10),s(11, b=20))
# s(b=31, 0)