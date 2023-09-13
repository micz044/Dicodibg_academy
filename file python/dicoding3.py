def kuadrat(x):
    return x*x
a = 10
k = kuadrat(a)
print('nilai kuadrat dari {} adalah {}'.format(a, k))


def kali(angka1, angka2):
    # Kalikan kedua parameter
    hasil = angka1 * angka2
    print('Dicetak dari dalam fungsi: {}'.format(hasil))
    return hasil
 
# Panggil fungsi kali
keluaran = kali(10, 20);
print('Dicetak sebagai kembalian: {}'.format(keluaran))