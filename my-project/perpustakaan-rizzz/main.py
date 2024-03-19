from welcome import main_header, header_awal
from utilitas import clear
from daftar import daftar
from masuk import masuk
from menu import start
 
def main():
    clear()
    main_header()
    header_awal()
    global user_input
    user_input = input('[Ketik 1, 2, atau 3] ')
    while user_input not in ["1", "2", "3"]:
        user_input = input('[Ketik 1, 2, atau 3] ')

def back2_main():
    input('\nKetik apapun untuk kembali ke menu utama ')
    main()

main()

while True:
    if int(user_input) == 1:
        # lihat_buku()
        # back2_main()
        daftar()
        back2_main()

    elif int(user_input) == 2:
        # cari_buku()
        # back2_main()
        clear()
        id_pengguna = masuk()
        def simpan_id():
            return id_pengguna
        start()
        break
    else:
        clear()
        break




