from view.input_nilai import data
from view.view_nilai import tampilkan

# update = data.update()
file = [{'nama': 'No Data Found!'}]


class method:

    def tambah(self):
        if file[0]['nama'] == 'No Data Found!':
            del file[0]
        input = data.inputData(self)
        dataAppend = {
            'nama': input[0],
            'nim': input[1],
            'nTugas': input[2],
            'nUTS': input[3],
            'nUAS': input[4],
            'nAkhir': input[5]
        }
        file.append(dataAppend)
        print('Data Telah Terinput')

        #Log
        # print(file)

    def update(self):

        for i in range(0, len(file)):
            nama = data.nama(self)
            if file[i]['nama'] == nama:
                update = data.update()
                print(update[0])
                file[i]['nTugas'] = update[0]
                file[i]['nUTS'] = update[1]
                file[i]['nUAS'] = update[2]
                file[i]['nAkhir'] = update[3]
                # print(file)
                print('Data Telah Terupdate')
            else:
                print("DATA TIDAK DI TEMUKAN!")

    def hapus(self):

        for i in range(0, len(file)):
            nama = data.nama(self)

            if file[i]['nama'] == nama:
                del file[i]['nama']
                del file[i]['nim']
                del file[i]['nTugas']
                del file[i]['nUTS']
                del file[i]['nUAS']
                del file[i]['nAkhir']
                print('Data Telah Dihapus')
                # file[0] = {'nama': 'No Data Found!'}
                # print(file)

    def cari():
        tampilkan.search('self', file)

    def show():
        tampilkan.show('self', file)