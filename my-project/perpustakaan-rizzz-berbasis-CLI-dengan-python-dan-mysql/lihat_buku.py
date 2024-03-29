from utilitas import clear
from welcome import main_header
import random as r
from database import database_buku

data_buku = database_buku()

# Menampilkan 10 buku acak
def algo_buku_acak():
    print("\nBerikut ini adalah 10 buku yang terdapat di Perpustakaan Rizz:")
    print("-"*125)
    print(f"| ID{' '*15}| Judul Buku{' ' * 49}| Pencipta{' '*17}| Status{' '*9}|")
    print("-"*125)
    
    for i in [r.randint(0, len(data_buku)- 1) for x in range(10)]:
        print(f"| {data_buku[i][0]}  | {data_buku[i][1]}{' ' * (59 - len(data_buku[i][1]))}| {data_buku[i][2]}{' ' * (25 - len(data_buku[i][2]))}| {data_buku[i][3]}{' ' * (15 - len(data_buku[i][3]))}|")
    print("-"*125)

# Menampilkan seluruh buku
def algo_buku_full():
    print("\nBerikut ini adalah daftar semua buku yang terdapat di Perpustakaan Rizz:\n")
    print("-"*125)
    print(f"| ID{' '*15}| Judul Buku{' ' * 49}| Pencipta{' '*17}| Status{' '*9}|")
    print("-"*125)

    for i in range(len(data_buku)):
        print(f"| {data_buku[i][0]}  | {data_buku[i][1]}{' ' * (59 - len(data_buku[i][1]))}| {data_buku[i][2]}{' ' * (25 - len(data_buku[i][2]))}| {data_buku[i][3]}{' ' * (15 - len(data_buku[i][3]))}|")
    print("-"*125) 


def lihat_buku():
    clear()
    main_header()
    algo_buku_acak()
    input_lihat_buku = input('Ingin melihat daftar semua buku? [y/n] ')
    while input_lihat_buku not in ["y", "n"]:
        input_lihat_buku = input('Ingin melihat daftar semua buku? [y/n] ')
    if input_lihat_buku == 'y':
        clear()
        main_header()
        algo_buku_full()