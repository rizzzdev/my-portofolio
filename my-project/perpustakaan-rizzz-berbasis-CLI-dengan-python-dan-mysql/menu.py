from welcome import main_header, header_menu_utama
from utilitas import clear
from lihat_buku import lihat_buku
from cari_buku import cari_buku
# from pinjam_buku import pinjam_buku
 
def main_menu():
    clear()
    main_header()
    header_menu_utama()
    global user_input
    user_input = input('[Ketik 1, 2, atau 3] ')
    while user_input not in ["1", "2", "3", "4"]:
        user_input = input('[Ketik 1, 2, atau 3] ')

def back2_main_menu():
    input('\nKetik apapun untuk kembali ke menu utama ')
    main_menu()

def start():
    main_menu()

    while True:
        if int(user_input) == 1:
            lihat_buku()
            back2_main_menu()

        elif int(user_input) == 2:
            cari_buku()
            back2_main_menu()
        # elif int(user_input) == 3:
        #     pinjam_buku()
        else:
            clear()
            break


