import tensorflow as tf

def oblicz(funkcja,a,b,c):
    dx = (b-a)/c
    zm = 0
    for x in range(c):
        x = x*dx + a
        zm += dx*eval(funkcja)
    return zm
 
def main(args):
    funkcja = input("Funkcja: ")
    a = float(input("Początek: "))
    b = float(input("Koniec: "))
    c = int(input("Liczba podprzedziałów: "))
    print("Wynik to: całka = {oblicz}".format(oblicz = oblicz(funkcja,a,b,c)))
    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

nazwa = tf.test.gpu_device_name()
if nazwa != '/device:GPU:0':
	raise SystemError('GPU nie znaleziono')
print('Znaleziono GPU: {}'.format(nazwa))
