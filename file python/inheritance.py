class Calculator:


    def __init__(self, nilai = 0) -> None:
        self.nilai = nilai

    def tambah_angka(self, angka1,angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:
            print('Kalkulator melebihih batas angka {}'.format(self.nilai))
        return self.nilai


class CalculatorKali(Calculator):
    def kali_angka(self,angka1,angka2):
        self.nilai = angka1 * angka2
        print("hasil dari {} * {} adalah = {}".format(angka1,angka2, angka1*angka2))

    def tambah_angka(self, angka1, angka2):
        return super().tambah_angka(angka1, angka2)


b = CalculatorKali()

class CalculatorTambah():
    def tambah_angka(self, angka1,angka2):
        if angka1 + angka2 <= 9:
            super().tambah_angka(angka1,angka2)
        else:
            self.nilai = angka1 +angka2
        return self.nilai

#jalankan fungsi
b.tambah_angka(12,10)
b.kali_angka(12,10)