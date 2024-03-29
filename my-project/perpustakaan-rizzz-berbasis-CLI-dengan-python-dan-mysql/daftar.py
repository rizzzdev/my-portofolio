from utilitas import clear
from database import database
from welcome import main_header, header_daftar
import maskpass as mp
import datetime as dt
from time import sleep

# Load Database
db = database()
cursor = db.cursor()

def daftar():
    clear()
    main_header()
    header_daftar()

    global nama_depan, nama_belakang
    nama_depan    = input("Nama Depan            = ")
    nama_belakang = input('Nama Belakang         = ')

    id_pengguna   = input('ID Pengguna           = ')

    if len(id_pengguna) > 15:
        print('\nID Pengguna yang Anda masukkan lebih dari 15 karakter, silahkan gunakan ID pengguna lain dan daftar ulang!')
        sleep(2)
        clear()
        main_header()
        header_daftar()
        daftar()
    try:
        query = f"insert into daftar_pengguna(id) values('{id_pengguna}')"
        cursor.execute(query)
        db.commit()
    except:
        print('\nID Pengguna yang Anda masukkan telah digunakan pengguna lain, silahkan gunakan ID pengguna lain dan daftar ulang!')
        sleep(2)
        clear()
        main_header()
        header_daftar()
        daftar()
        
    kata_sandi    = mp.askpass(prompt = 'Kata Sandi            = ', mask='*')
    kata_sandi_conf  = mp.askpass(prompt = 'Konfirmasi Kata Sandi = ', mask='*')
    while kata_sandi != kata_sandi_conf:
        print('\nKata Sandi yang Anda masukkan harus sama!\n')
        kata_sandi    = mp.askpass(prompt = 'Kata Sandi            = ', mask='*')
        kata_sandi_conf  = mp.askpass(prompt = 'Konfirmasi Kata Sandi = ', mask='*')

    tanggal_daftar = dt.datetime.today()

    query = f'''
        update daftar_pengguna
        set nama_depan = "{nama_depan.title()}", nama_belakang = "{nama_belakang.title()}", kata_sandi = "{kata_sandi}", tanggal_daftar = "{tanggal_daftar}"
        where id = "{id_pengguna}"
    '''
    cursor.execute(query)
    db.commit()

    print('\nPendaftaran Berhasil\n')


