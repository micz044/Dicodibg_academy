class calculator:

    def f(self):
        return "Hello World"
    

    @classmethod
    def tambah_angka(cls,angka1,angka2):
        return '{} + {} = {}'.format(angka1,angka2, angka1+angka2)
    
    @staticmethod
    def kali_angka(angka1,angka2):
        return '{} * {} = {}'.format(angka1,angka2, angka1*angka2)

k = calculator()

print(calculator.tambah_angka(10,20))
print(k.tambah_angka(13,10))

print(calculator.kali_angka(10,20))
print(k.kali_angka(13,10))