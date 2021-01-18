import tensorflow as tf

def oblicz(funkcja,a,b,i):
    dx = (b-a)/i
    zm = 0
    for x in range(i):
        x = x * dx + a
        fx1 = eval(funkcja)
        x += dx
        fx2 = eval(funkcja)
        zm += 0.5*dx*(fx1+fx2)
    return zm

def main(args):
    funkcja = input("Funkcja: ")
    a = float(input("Początek: "))
    b = float(input("Koniec: "))
    i = int(input("Liczba podprzedziałów: "))
    print("Całka z podanej funkcji {f} po przedziale od {a} do {b} = {oblicz}".format(f = funkcja, a = a, b = b, oblicz = oblicz(funkcja,a,b,i)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

nazwa = tf.test.gpu_device_name()
if nazwa != '/device:GPU:0':
	raise SystemError('GPU nie znaleziono')
print('Znaleziono GPU: {}'.format(nazwa))
