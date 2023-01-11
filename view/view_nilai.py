from tabulate import tabulate
from view.input_nilai import data
from model import daftar_nilai


class tampilkan:

    def menu():
        print('-' * 80, '\n')
        method = daftar_nilai.method

        stop = True

        print('Program Data Sederhana'.center(80, ' '))

        while (stop):
            print(
                '(1) Tambah Data, (2) Ubah Data, (3) Hapus Data, (4) Tampilkan Data, (5) Cari Data, (6) Exit Program'
            )

            inputUser = str(input('Pilih Menu: '))
            inputs = inputUser.lower()

            if inputs == '1':
                method.tambah('str')

            elif inputs == '2':
                method.update('str')

            elif inputs == '3':
                method.hapus('str')

            elif inputs == '4':
                method.show()

            elif inputs == '5':
                method.cari()

            elif inputs == '6':
                print("Program dihentikan")
                stop = False

            else:
                print('Input Salah!')

    def search(self, datas):
        for i in range(0, len(datas)):
            nama = data.nama(self)

            if datas[i]['nama'] == nama:
                rows = [x.values() for x in datas]
                headers = [
                    'Nama', 'NIM', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS',
                    'Nilai Akhir'
                ]
                print(
                    tabulate(rows,
                             headers=headers,
                             tablefmt='fancy_grid',
                             stralign='center'))

            else:
                print(
                    tabulate('DATA TIDAK DITEMUKAN',
                             tablefmt='fancy_grid',
                             stralign='center'))

    def show(self, datas):

        if datas[0]['nama'] == 'No Data Found!':
            print(tabulate([datas], tablefmt='fancy_grid', stralign='center'))
        else:
            rows = [x.values() for x in datas]
            headers = [
                'Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS',
                'Nilai Akhir'
            ]
            print(
                tabulate(rows,
                         headers=headers,
                         tablefmt='fancy_grid',
                         stralign='center'))