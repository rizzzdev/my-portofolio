from utilitas import clear, encode_string
from welcome import main_header
import random as r
from database import database_buku

data_buku = database_buku()

# Mencari buku berdasarkan judul atau nama penulis dari keyword yang diinputkan
def algo_cari_buku(judul):
    judul_buku = []
    penulis_buku = []
    id_buku = []
    for i in range(len(data_buku)):
        judul_buku.append(encode_string(data_buku[i][1]).lower())
        penulis_buku.append(encode_string(data_buku[i][2]).lower())
        id_buku.append(encode_string(data_buku[i][0]).lower())
    index_buku = []
    for i in range(len(judul_buku)):
        if (encode_string(judul) in judul_buku[i]) or (encode_string(judul) in penulis_buku[i]) or (encode_string(judul) in id_buku[i]):
            index_buku.append(i)
    if index_buku == []:
        print("-"*108)
        print(f"| ID{' '*15}| Judul Buku{' ' * 49}| Pencipta{' '*17}|")
        print("-"*108)
        print(f'| hasil tidak ditemukan{" "* 84}|')
        print("-"*108)
    else:
        print("-"*125)
        print(f"| ID{' '*15}| Judul Buku{' ' * 49}| Pencipta{' '*17}| Status{' '*9}|")
        print("-"*125)
        for i in index_buku:
            print(f"| {data_buku[i][0]}  | {data_buku[i][1]}{' ' * (59 - len(data_buku[i][1]))}| {data_buku[i][2]}{' ' * (25 - len(data_buku[i][2]))}| {data_buku[i][3]}{' ' * (15 - len(data_buku[i][3]))}|")
        print("-"*125)

def cari_buku():
    clear()
    main_header()
    print('\nSilahkan ketik kata kunci untuk mencari buku yang Anda inginkan!\nPencarian yang dilakukan berdasarkan id buku, judul buku atau nama penulis\n')
    input_cari_buku = input('kata kunci = ')
    print('\n')
    algo_cari_buku(input_cari_buku)
    print('\n')