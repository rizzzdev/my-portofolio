import mysql.connector as mysql

# Database MySQL
def database():
    db = mysql.connect(
        user     = 'root',
        password = '1234',
        host     = 'localhost',
        port     = 3306,
        database = 'perpustakaan_rizzz'
    )
    return db

# Convert Database MySQL menjadi list
def database_buku():
    db = database()
    cursor = db.cursor()
    data_buku = []
    cursor.execute('select * from daftar_buku')
    for x in cursor:
        data_buku.append(x)
    return data_buku



