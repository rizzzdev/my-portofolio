from utilitas import clear
from database import database
from welcome import main_header, header_masuk
import maskpass as mp
from time import sleep

db = database()
cursor = db.cursor()

def masuk():
    # clear()
    main_header()
    header_masuk()

    id_pengguna   = input("ID Pengguna    = ")

    cek_db = []

    query = f'''

        select * from daftar_pengguna where id = "{id_pengguna}"

    '''
    cursor.execute(query)
    for x in cursor:
        cek_db.append(x)
    
    if cek_db == []:
        print('Kata Sandi     = \n')
        print('ID Pengguna yang Anda masukkan salah, silahkan masuk kembali dalam!')
        sleep(3)
        masuk()
    else:
        kata_sandi    = mp.askpass(prompt ='Kata Sandi     = ', mask='*')

        if kata_sandi != cek_db[0][3]:
            print('\nKata Sandi yang Anda masukkan salah, silahkan masuk kembali dalam!')
            sleep(3)
            masuk()
        else:
            print('\nBerhasil masuk, tunggu sebentar!\n')
            sleep(3)
    return id_pengguna

