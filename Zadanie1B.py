import tensorflow as tf

def oblicz_simpson(funkcja, a, b, n):
  s1 = 0
  s2 = 0  
  d = (b-a)/n
  res = funkcja(a) + funkcja(b)
  
  for i in range(0, n, 2):
    x = a+i*d
    s1 += funkcja(x)

  for i in range(1, n-1, 2):
    x = a + i * d
    s2 += funkcja(x)
  return d*(total + 4*s1 + 2*s2)/3

zm = oblicz_simpson(lambda x: x*x, 0.0, 3.0, 50)
print(zm)

nazwa = tf.test.gpu_device_name()
if nazwa != '/device:GPU:0':
	raise SystemError('Nie znaleziono urządzenia GPU')
print('Znaleziono urządzenie GPU: {}'.format(nazwa))
