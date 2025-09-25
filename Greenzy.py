import pandas as pd
import csv
import os
import time
import sys
from tabulate import tabulate
from datetime import datetime

font = '''
  ▄████  ██▀███  ▓█████ ▓█████  ███▄    █ ▒███████▒▓██   ██▓
 ██▒ ▀█▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀  ██ ▀█   █ ▒ ▒ ▒ ▄▀░ ▒██  ██▒
▒██░▄▄▄░▓██ ░▄█ ▒▒███   ▒███   ▓██  ▀█ ██▒░ ▒ ▄▀▒░   ▒██ ██░
░▓█  ██▓▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄ ▓██▒  ▐▌██▒  ▄▀▒   ░  ░ ▐██▓░
░▒▓███▀▒░██▓ ▒██▒░▒████▒░▒████▒▒██░   ▓██░▒███████▒  ░ ██▒▓░
 ░▒   ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒   ██▒▒▒ 
  ░   ░   ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒ ▓██ ░▒░ 
░ ░   ░   ░░   ░    ░      ░      ░   ░ ░ ░ ░ ░ ░ ░ ▒ ▒ ░░  
      ░    ░        ░  ░   ░  ░         ░   ░ ░     ░ ░     
                                          ░         ░ ░     
'''

def Awal(): 
    os.system('cls')
    print(font)
    tanya = str(input('Apakah anda memiliki akun? [y/n] : ')).lower()
    if tanya == 'y': 
        login()
    elif tanya == 'n':
        register()
        login()
    else:
        print('❕❕❕Jawaban Anda tidak valid❕❕❕')
        time.sleep(1)
        Awal()

def Animation():
    print('\n🔄 Verifikasi akun', end='')
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)
    print('\n')
    
def Animation1():
    print('\n🔄 Tunggu sebentar', end='')
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)
    print('\n')

def register():
    os.system('cls')
    print('\n' + '=' * 20 + ' REGISTRASI AKUN ' + '=' * 20 + '\n')
    Email = input('Masukkan email anda: ')
    while '@gmail.com' not in Email.split('@gmail.com')[-1]:
        input('❌ Format email tidak valid. Tekan enter untuk coba lagi❕❕❕')
        while '@gmail.com' not in Email:
            print('⚠️ Email harus berformat @gmail.com ⚠️')
            time.sleep(1.5)
            register()
        register()
    Username = input('Masukkan username anda: ')
    while Username == '':
        print('❌ Username tidak boleh kosong❕❕❕')
        time.sleep(1)
        register()
    Password = input('Masukkan password anda: ')
    while Password == '':
        print('❌ Password tidak boleh kosong❕❕❕')
        time.sleep(1)
        register()
    Animation1()
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	  MANAJEMEN AKUN             ^^^ ||')
    print('||--------- Silahkan pilih posisi Anda  ---------||')
    print('||                1. Penjual                     ||')
    print('||                2. Pembeli                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    tanya = input('Silahkan pilih posisi Anda: ').strip()
    Animation1()
    try :
        os.system('cls')
        if tanya == '1':
            tanya = 'Penjual'
            print('\n✅ Registrasi anda telah berhasil❕❕❕')
            data = 'E:/Algo1/Project algo 1/UsersPenjual.csv'
            file_exists = os.path.isfile(data)
            with open(data, mode='a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(['Email', 'Username', 'Password', 'Posisi'])
                writer.writerow([Email, Username, Password, tanya])
            input('Tekan enter untuk melanjutkan...')
            login()
        elif tanya == '2':
            tanya = 'Pembeli'
            Alamat = input('Masukkan alamat rumah anda: ')
            while Alamat == '':
                print('❌ Alamat tidak boleh kosong❕❕❕')
                Alamat = input('Masukkan alamat rumah anda: ')
            PIN = int(input('Masukkan PIN transaksi anda: '))
            while len(PIN) != 6:
                print('❌ PIN harus terdiri dari 6 digit angka❕❕❕')
                PIN = int(input('Masukkan PIN transaksi anda: '))
            data = 'E:/Algo1/Project algo 1/UsersPembeli.csv'
            file_exists = os.path.isfile(data)
            with open(data, mode='a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(['Email', 'Username', 'Password', 'Alamat', 'PIN', 'Posisi'])
                writer.writerow([Email, Username, Password, Alamat, PIN, tanya])
            print('\n✅ Registrasi anda telah berhasil❕❕❕')
            input('Tekan enter untuk melanjutkan...')
            login()
        else:
            print('❌ Pilihan tidak ada❕❕❕')
            time.sleep(1)
            register()
    except ValueError:
        print('❌ Pilihan tidak ada❕❕❕')
        time.sleep(1)
        register()

def login():
    while True:
        os.system('cls')
        print(font)
        print('\n' + '=' * 20 + ' LOGIN AKUN ' + '=' * 20 + '\n')
        User = input('Masukkan email atau username anda: ')
        Password = input('Masukkan password anda: ')
        Animation()
        data = pd.read_csv('E:/Algo1/Project algo 1/UsersPenjual.csv')
        data['Password'] = data['Password'].astype(str)
        data['Username'] = data['Username'].astype(str)
        user = data[((data['Username'] == User) | (data['Email'] == User)) & (data['Password'] == Password)]
        if not user.empty:
            print('\n✅ Login berhasil❕❕❕')
            time.sleep(1)
            Penjual(User)
            break
        data1 = pd.read_csv('E:/Algo1/Project algo 1/UsersPembeli.csv')
        data1['Password'] = data1['Password'].astype(str)
        data1['Username'] = data1['Username'].astype(str)
        user = data1[((data1['Username'] == User) | (data1['Email'] == User)) & (data1['Password'] == Password)]
        if not user.empty:
            print('\n✅ Login berhasil❕❕❕')
            time.sleep(1)
            Pembeli(User)
            break
        else:
            print('\n❌ Username atau password salah ❌')
            print('❕❕❕Coba lagi❕❕❕')
            time.sleep(1)
            Awal()

def Penjual(User):
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||---------Apa yang ingin anda inginkan?---------||')
    print('||                1. Profil                      ||')
    print('||                2. Manajemen barang            ||')
    print('||                3. Transaksi                   ||')
    print('||                4. Voucher                     ||')
    print('||                5. Logout                      ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        tanya = int(input('Pilih menu: '))
        if tanya == 1:
            ProfilPenjual(User)
        elif tanya == 2:
            ManajemenBarang(User)
        elif tanya == 3:
            Transaksi(User)
        elif tanya == 4:
            Voucher(User)
        elif tanya == 5:
            os.system('cls')
            print(font)
            print('Terima kasih telah menggunakan aplikasi kami❕❕❕')
            time.sleep(2.1)
            os.system('cls')
            sys.exit()
        else:
            print('❕❕❕Pilihan Anda tidak valid❕❕❕')
            time.sleep(1)
            Penjual(User)
    except ValueError:
        print('❕❕❕Pilihan Anda tidak valid❕❕❕')
        print('   ⚠️ INPUT MENGGUNAKAN ANGKA ⚠️')
        Penjual(User)

def ProfilPenjual(User):
    os.system('cls')
    file = 'E:/Algo1/Project algo 1/UsersPenjual.csv'
    UserInput = User
    print(font)
    print('\n' + '=' * 20 + ' PROFIL AKUN ' + '=' * 20 + '\n')
    if os.path.isfile(file):
        try:
            data = pd.read_csv(file)
            UserData = data[(data['Username'] == UserInput) | (data['Email'] == UserInput)]
            if not UserData.empty:
                print(tabulate(UserData, headers='keys', tablefmt='grid', showindex=False))
                input('Tekan enter untuk kembali...')
                Penjual(User)
            else:
                print('⚠️ Pengguna tidak ditemukan. Pastikan email atau username benar❕❕❕')
                time.sleep(1)
                Penjual(User)
        except Exception as e:
            print(f"⚠️ Terjadi kesalahan saat membaca data: {e}")
            time.sleep(1)
            Penjual(User)
    else:
        print('⚠️ Data tidak ditemukan.')
        time.sleep(1)
        Penjual(User)

FileBarang = 'E:/Algo1/Project algo 1/ManajemenBarang.csv'

def TambahBarang():
    data = pd.read_csv(FileBarang)
    ID = int(input('Masukkan ID Barang: '))
    Nama = input('Masukkan nama barang: ').capitalize()
    Harga = float(input('Masukkan harga barang: '))
    Stok = int(input('Masukkan stok barang (dalam kg): '))
    if Nama in data['Nama Barang'].values:
        data.loc[data['Nama Barang'] == Nama, 'Stok'] += Stok
    else:
        data = pd.concat([data, pd.DataFrame({'ID' : [ID], 'Nama Barang': [Nama], 'Harga': [Harga], 'Stok': [Stok]})], ignore_index=True)
    data.to_csv(FileBarang, index=False)
    print(f"'{Nama}' telah ditambahkan dengan harga Rp.{Harga} dan stok {Stok} kg.")

def EditHarga():
    data = pd.read_csv(FileBarang)
    Nama = input('Masukkan nama barang yang ingin anda ubah harganya: ').capitalize()
    if Nama in data['Nama Barang'].values:
        HargaBaru = float(input(f'Masukkan harga baru {Nama}: '))
        data.loc[data['Nama Barang'] == Nama, 'Harga'] = HargaBaru
        data.to_csv(FileBarang, index=False)
        print(f"Harga '{Nama}' berhasil diperbarui menjadi Rp.{HargaBaru}")
    else:
        print(f"'{Nama}' tidak ditemukan❕❕❕")

def EditStok():
    data = pd.read_csv(FileBarang)
    Nama = input('Masukkan nama barang yang ingin Anda ubah stoknya: ').capitalize()
    if Nama in data['Nama Barang'].values:
        StokBaru = int(input(f'Masukkan stok baru untuk {Nama}: '))
        if StokBaru == 0:
            data = data[data['Nama Barang'] != Nama]
            print(f"'{Nama}' telah dihapus dari daftar karena stoknya habis.")
        else:
            data.loc[data['Nama Barang'] == Nama, 'Stok'] = StokBaru
            print(f"Stok '{Nama}' berhasil diperbarui menjadi {StokBaru} kg.")
        data.to_csv(FileBarang, index=False)
    else:
        print(f"'{Nama}' tidak ditemukan❕❕❕")
        time.sleep(1)
        EditStok()

def ManajemenBarang(User):
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	  MANAJEMEN BARANG           ^^^ ||')
    print('||---------Apa yang ingin anda inginkan?---------||')
    print('||                1. Tampilkan barang            ||')
    print('||                2. Tambah barang               ||')
    print('||                3. Edit harga                  ||')
    print('||                4. Edit stok                   ||')
    print('||                5. Kembali                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    tanya = (input('Pilih menu: '))
    data = pd.read_csv('E:/Algo1/Project algo 1/ManajemenBarang.csv')
    data.index = range(1,len(data)+1)
    Tabel = (tabulate(data, headers='keys', tablefmt='grid'))
    try:
        if tanya == '1':
            os.system('cls')
            print('\n' + '=' * 20 + ' DAFTAR BARANG ' + '=' * 20 + '\n')
            print(Tabel)
            input('\nTekan enter untuk kembali...')
            ManajemenBarang(User)
        elif tanya == '2':
            os.system('cls')
            print('\n' + '=' * 20 + ' TAMBAH BARANG ANDA ' + '=' * 20 + '\n')
            print(Tabel)
            TambahBarang()
            input('\nTekan enter untuk kembali...')
            ManajemenBarang(User)
        elif tanya == '3':
            os.system('cls')
            print('\n' + '=' * 20 + ' EDIT HARGA BARANG ANDA ' + '=' * 20 + '\n')
            print(Tabel)
            EditHarga()
            input('\nTekan enter untuk kembali...')
            ManajemenBarang(User)
        elif tanya == '4':
            os.system('cls')
            print('\n' + '=' * 20 + ' EDIT STOK BARANG ANDA ' + '=' * 20 + '\n')
            print(Tabel)
            EditStok()
            input('\nTekan enter untuk kembali...')
            ManajemenBarang(User)
        elif tanya == '5':
            Penjual(User)
        else:
            print('❕❕❕Jawaban Anda tidak valid❕❕❕')
            time.sleep(1)
            ManajemenBarang(User)
    except ValueError:
        print('❕❕❕Jawaban Anda tidak valid❕❕❕')
        print('   ⚠️ INPUT MENGGUNAKAN ANGKA ⚠️')
        time.sleep(1)
        ManajemenBarang(User)

def RiwayatPenjualan():
    file_keranjang = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    riwayat_penjualan = 'E:/Algo1/Project algo 1/RiwayatPenjualan.csv'
    data_keranjang = filedata(file_keranjang)
    if not data_keranjang.empty:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_keranjang['Tanggal'] = now
        if not os.path.isfile(riwayat_penjualan):
            data_keranjang.to_csv(riwayat_penjualan, index=False, mode='w')
        else:
            data_keranjang.to_csv(riwayat_penjualan, index=False, mode='a', header=False)

def Transaksi(User):
    os.system('cls')
    file_penjualan = 'E:/Algo1/Project algo 1/RiwayatPenjualan.csv'
    if os.path.isfile(file_penjualan):
        data_penjualan = filedata(file_penjualan)
        if not data_penjualan.empty:
            print('\n' + '=' * 20 + ' RIWAYAT PENJUALAN ' + '=' * 20 + '\n')
            print(tabulate(data_penjualan, headers='keys', tablefmt='grid', showindex=False))
        else:
            print('⚠️ Belum ada riwayat penjualan.')
    else:
        print('⚠️ File riwayat penjualan tidak ditemukan.')
    input('\nTekan enter untuk kembali...')
    Penjual(User)
    
VoucherPenjual = 'E:/Algo1/Project algo 1/UsersVoucher.csv'

def FileVoucher():
    if os.path.exists('E:/Algo1/Project algo 1/UsersVoucher.csv'):
        return pd.read_csv(VoucherPenjual).set_index('Kode').to_dict()['Stok']
    return {}

def DataVoucher(vouchers):
    if vouchers:
        print('\nDaftar voucher dan Stoknya:')
        print(tabulate(vouchers.items(), headers=['Kode', 'Stok'], tablefmt='grid'))
    else:
        print('\nTidak ada voucher yang tersedia.')

def SimpanVoucher(vouchers):
    data = pd.DataFrame(list(vouchers.items()), columns=['Kode', 'Stok'])
    data.to_csv(VoucherPenjual, index=False)

def TambahVoucher(vouchers, Kode, Stok):
    if Kode in vouchers:
        vouchers[Kode] += Stok
        print(f"Stok voucher '{Kode}' ditambahkan sebanyak {Stok}. Total Stok sekarang: {vouchers[Kode]}.")
    else:
        vouchers[Kode] = Stok
        print(f"Kode voucher '{Kode}' telah ditambahkan dengan stok {Stok} voucher.")
    return vouchers

def HapusVoucher(vouchers, Kode, Stok):
    if Kode in vouchers:
        if vouchers[Kode] >= Stok:
            vouchers[Kode] -= Stok
            print(f"Stok voucher '{Kode}' dikurangi sebanyak {Stok}. Sisa Stok: {vouchers[Kode]}.")
            if vouchers[Kode] == 0:
                del vouchers[Kode]
                print(f"Voucher '{Kode}' habis dan dihapus dari daftar❕❕❕")
        else:
            print('❕❕❕Gagal menghapus Stok❕❕❕')
            print(f"⚠️ Stok yang diminta ({Stok}) melebihi Stok yang tersedia ({vouchers[Kode]}) ⚠️")
    else:
        print(f"⚠️ Voucher '{Kode}' tidak ditemukan ⚠️")
    return vouchers

def Voucher(User):
    vouchers = FileVoucher()
    while True:
        os.system('cls')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	     	   VOUCHER TOKO              ^^^ ||')
        print('||---------Apa yang ingin anda inginkan?---------||')
        print('||                1. Tampilkan voucher           ||')
        print('||                2. Tambah voucher              ||')
        print('||                3. Hapus voucher               ||')
        print('||                4. Kembali                     ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        try:
            tanya = int(input('Pilih menu: '))
            if tanya == 1:
                os.system('cls')
                print('\n' + '=' * 20 + ' DAFTAR VOUCHER ' + '=' * 20 + '\n')
                DataVoucher(vouchers)
                input('\nTekan enter untuk kembali...')
                Voucher(User)
            elif tanya == 2:
                os.system('cls')
                print('\n' + '=' * 20 + ' TAMBAH VOUCHER ANDA ' + '=' * 20 + '\n')
                Kode = input('Masukkan kode voucher: ').upper()
                try:
                    Stok = int(input('Masukkan stok voucher: '))
                    vouchers = TambahVoucher(vouchers, Kode, Stok)
                    SimpanVoucher(vouchers)
                except ValueError:
                    print('Input stok harus berupa angka.')
                input('\nTekan enter untuk kembali...')
            elif tanya == 3:
                os.system('cls')
                print('\n' + '=' * 20 + ' HAPUS VOUCHER ANDA ' + '=' * 20 + '\n')
                DataVoucher(vouchers)
                Kode = input('\nMasukkan kode voucher yang ingin dihapus: ').upper()
                try:
                    Stok = int(input('Masukkan stok voucher yang ingin dihapus: '))
                    vouchers = HapusVoucher(vouchers, Kode, Stok)
                    SimpanVoucher(vouchers)
                except ValueError:
                    print('Input stok harus berupa angka.')
                    time.sleep(1)
                    Voucher(User)
            elif tanya == 4:
                Penjual(User)
            else:
                print('❕❕❕Pilihan Anda tidak valid❕❕❕')
                time.sleep(1)
                Voucher(User)
        except ValueError:
            print('❕❕❕Pilihan Anda tidak valid❕❕❕')
            print('   ⚠️ INPUT MENGGUNAKAN ANGKA ⚠️')
            time.sleep(1)
            Voucher(User)

def Pembeli(User):
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||---------Apa yang ingin anda inginkan?---------||')
    print('||                1. Profil                      ||')
    print('||                2. Katalog                     ||')
    print('||                3. Transaksi                   ||')
    print('||                4. Logout                      ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        tanya = int(input('Pilih menu: '))
        if tanya == 1:
            ProfilPembeli(User)
        elif tanya == 2:
            Katalog(User)
        elif tanya == 3:
            RiwayatPembelian(User)
        elif tanya == 4:
            os.system('cls')
            print(font)
            print('Terima kasih telah menggunakan aplikasi kami❕❕❕')
            ClearPembelian()
            time.sleep(2.1)
            os.system('cls')
            sys.exit()
        else:
            print('❕❕❕Pilihan Anda tidak valid❕❕❕')
            time.sleep(1)
            Pembeli(User)
    except ValueError:
        print('❕❕❕Pilihan Anda tidak valid❕❕❕')
        print('   ⚠️ INPUT MENGGUNAKAN ANGKA ⚠️')
        time.sleep(1)
        Pembeli(User)
        
def ClearPembelian():
    riwayat_pembelian = 'E:/Algo1/Project algo 1/RiwayatPembelian.csv'
    if os.path.exists(riwayat_pembelian):
        with open(riwayat_pembelian, 'w') as file:
            file.write('Nama Barang,Jumlah,Total\n')
        print('✅ Riwayat pembelian dibersihkan❕❕❕')
        
def ProfilPembeli(User):
    os.system('cls')
    file = 'E:/Algo1/Project algo 1/UsersPembeli.csv'
    UserInput = User
    print(font)
    print('\n' + '=' * 20 + ' PROFIL AKUN ' + '=' * 20 + '\n')
    if os.path.isfile(file):
        try:
            data = pd.read_csv(file)
            UserData = data[(data['Username'] == UserInput) | (data['Email'] == UserInput)]
            if not UserData.empty:
                print(tabulate(UserData, headers='keys', tablefmt='grid', showindex=False))
                input('Tekan enter untuk kembali...')
                Pembeli(User)
            else:
                print('⚠️ Pengguna tidak ditemukan. Pastikan email atau username benar.')
                time.sleep(1)
                Pembeli(User)
        except Exception as e:
            print(f'⚠️ Terjadi kesalahan saat membaca data: {e}')
            time.sleep(1)
            Pembeli(User)
    else:
        print('⚠️ Data tidak ditemukan.')
        time.sleep(1)
        Pembeli(User)

def filedata(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        return pd.DataFrame()

def save(data, filepath):
    data.to_csv(filepath, index=False)
    
def TambahKeranjang(ID_Barang):
    data_barang = filedata('E:/Algo1/Project algo 1/ManajemenBarang.csv')
    keranjang_path = f'E:/Algo1/Project algo 1/UserKeranjang.csv'
    data_keranjang = filedata(keranjang_path)

    stok = data_barang.loc[data_barang['ID'].astype(str) == ID_Barang, 'Stok'].values[0]
    nama_barang = data_barang.loc[data_barang['ID'].astype(str) == ID_Barang, 'Nama Barang'].values[0]
    harga_barang = data_barang.loc[data_barang['ID'].astype(str) == ID_Barang, 'Harga'].values[0]

    jumlah = int(input('Masukkan jumlah barang: '))
    if jumlah <= stok:
        total = harga_barang * jumlah
        new_entry = {'Nama Barang': nama_barang, 'Jumlah': jumlah, 'Total': total}
        data_keranjang = pd.concat([data_keranjang, pd.DataFrame([new_entry])], ignore_index=True)
        data_barang.loc[data_barang['ID'].astype(str) == ID_Barang, 'Stok'] -= jumlah
        save(data_barang, 'E:/Algo1/Project algo 1/ManajemenBarang.csv')
        save(data_keranjang, keranjang_path)
        print(f"'{nama_barang}' telah ditambahkan ke keranjang.")
    else:
        print(f"Stok tidak mencukupi. Sisa stok: {stok}.")
        
def Katalog(User):
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^                 KATALOG                ^^^ ||')
    print('||---------Apa yang ingin anda inginkan?---------||')
    print('||                1. Pencarian                   ||')
    print('||                2. Tampilkan barang            ||')
    print('||                3. Keranjang                   ||')
    print('||                4. Kembali                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        pilih = int(input('Pilih menu: '))
        if pilih == 1:
            CariBarang(User)
        elif pilih == 2:
            SemuaBarang(User)
        elif pilih == 3:
            Keranjang(User)
        elif pilih == 4:
            Pembeli(User)
        else:
            print('❕❕❕Pilihan Anda tidak valid❕❕❕')
            time.sleep(1)
            Katalog(User)
    except ValueError:
        print('❕❕❕Pilihan Anda tidak valid❕❕❕')
        print('   ⚠️ INPUT MENGGUNAKAN ANGKA ⚠️')
        time.sleep(1)
        Katalog(User)
        
def CariBarang(User):
    os.system('cls')
    print('\n' + '=' * 20 + ' PENCARIAN BARANG ' + '=' * 20 + '\n')
    barang = input('Masukkan nama barang yang ingin dicari: ')
    data = filedata('E:/Algo1/Project algo 1/ManajemenBarang.csv')
    result = data[data['Nama Barang'].str.contains(barang, case=False, na=False)]
    if not result.empty:
        print(tabulate(result, headers='keys', tablefmt='grid', showindex=False))
        tanya = ('Apakah ada barang yang akan anda beli? (y/n): ')
        jawab = input(tanya)
        if jawab == 'y':
            ID_Barang = input('Masukkan ID barang: ')
            if ID_Barang in result['ID'].astype(str).values:
                TambahKeranjang(ID_Barang)
            else:
                print('⚠️ ID barang tidak ditemukan❕❕❕')
                time.sleep(1)
                CariBarang(User)
        elif jawab == 'n':
            Katalog(User)
        else:
            print('❕❕❕Pilihan tidak valid❕❕❕')
            time.sleep(1)
            CariBarang(User)
    else:
        print('❕❕❕Barang tidak ditemukan❕❕❕')
    input('Tekan enter untuk kembali...')
    Katalog(User)

def SemuaBarang(User):
    print('\n' + '=' * 20 + ' DAFTAR BARANG ' + '=' * 20 + '\n')
    data = filedata('E:/Algo1/Project algo 1/ManajemenBarang.csv')
    if not data.empty:
        print(tabulate(data, headers='keys', tablefmt='grid', showindex=False))
        while True:
            pilih = input('\nApakah Anda ingin membeli barang? (y/n): ').lower()
            if pilih == 'y':
                ID_Barang = input('Masukkan ID barang: ')
                if ID_Barang in data['ID'].astype(str).values:
                    TambahKeranjang(ID_Barang)
                else:
                    print('❕❕❕ID barang tidak ditemukan❕❕❕')
            elif pilih == 'n':
                Katalog(User)
                break
            else:
                print('❕❕❕Pilihan tidak valid❕❕❕')
                time.sleep(1)
                SemuaBarang(User)
    else:
        print('⚠️ Data barang kosong ⚠️')
        time.sleep(1)
        Katalog(User)
    input('Tekan enter untuk kembali...')
    Katalog(User)

def Keranjang(User):
    os.system('cls')
    keranjang_path = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    data_keranjang = filedata(keranjang_path)
    if data_keranjang.empty:
        print('\n' + '=' * 20 + ' KERANJANG KOSONG ' + '=' * 20 + '\n')
        input('Tekan enter untuk kembali...')
        Katalog(User)
    else:
        print(tabulate(data_keranjang, headers='keys', tablefmt='grid', showindex=False))
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^               PILIH MENU               ^^^ ||')
        print('||---------Apa yang ingin anda inginkan?---------||')
        print('||                1. Checkout                    ||')
        print('||                2. Hapus item                  ||')
        print('||                3. Kembali                     ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        try:
            pilih = int(input('Pilih menu: '))
            if pilih == 1:
                VerifPIN(User)
            elif pilih == 2:
                HapusItem(User)
            elif pilih == 3:
                Katalog(User)
            else:
                print('Pilihan tidak valid!')
                time.sleep(1)
                Keranjang(User)
        except ValueError:
            print('❕❕❕Pilihan Anda tidak valid❕❕❕')
            print('   ⚠️ INPUT MENGGUNAKAN ANGKA ⚠️')
            time.sleep(1)
            Keranjang(User)

def HapusItem(User):
    file_keranjang = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    data_keranjang = filedata(file_keranjang)
    data_barang = filedata('E:/Algo1/Project algo 1/ManajemenBarang.csv')
    barang = input('Masukkan nama barang yang ingin dihapus: ').capitalize()
    if barang in data_keranjang['Nama Barang'].values:
        try:
            jumlah = int(input('Masukkan jumlah barang yang ingin dihapus: '))
            keranjang_row = data_keranjang[data_keranjang['Nama Barang'] == barang].iloc[0]
            if jumlah <= keranjang_row['Jumlah']:
                data_keranjang.loc[data_keranjang['Nama Barang'] == barang, 'Jumlah'] -= jumlah
                if data_keranjang.loc[data_keranjang['Nama Barang'] == barang, 'Jumlah'].values[0] == 0:
                    data_keranjang = data_keranjang[data_keranjang['Nama Barang'] != barang]
                stok_kembali = jumlah
                data_barang.loc[data_barang['Nama Barang'] == barang, 'Stok'] += stok_kembali
                save(data_barang, 'E:/Algo1/Project algo 1/ManajemenBarang.csv')
                save(data_keranjang, file_keranjang)
                print(f'{jumlah} {barang} telah dihapus dari keranjang.')
                time.sleep(1)
                Keranjang(User)
            else:
                print('⚠️ Jumlah yang dimasukkan melebihi jumlah di keranjang ⚠️')
                time.sleep(1)
                HapusItem(User)
        except ValueError:
            print('❕❕❕Jumlah tidak valid❕❕❕')
            time.sleep(1)
            HapusItem(User)
    else:
        print('⚠️ Barang tidak ditemukan di keranjang ⚠️')
        time.sleep(1)
        HapusItem(User)

def ResetKeranjang():
    keranjang_path = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    save(pd.DataFrame(columns=['Nama Barang', 'Jumlah', 'Total']), keranjang_path)

def Verifikasi(Pembayaran, Username):
    try:
        with open(Pembayaran, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == Username:
                    return row['PIN']
        print('❌User ID tidak ditemukan❕❕❕')
        time.sleep(1)
        Pembeli(Username)
    except FileNotFoundError:
        print('⚠️ File tidak ditemukan ⚠️')
    return None

def VerifPIN(User):
    os.system('cls')
    Pembayaran = 'E:/Algo1/Project algo 1/UsersPembeli.csv'
    print('\n' + '=' * 20 + ' ⚠️ VERIFIKASI DULU ⚠️ ' + '=' * 20 + '\n')
    Username = input('Masukkan Username anda: ')
    PINuser = Verifikasi(Pembayaran, Username)
    if PINuser:
        for attempt in range(3):
            InputPIN = input('Masukkan PIN transaksi Anda: ')
            if InputPIN == PINuser:
                print('\nPIN berhasil diverifikasi✅')
                metode = PilihPembayaran(User)
                print(f'Metode pembayaran yang dipilih: {metode}')
                print('Pembayaran dimulai...')
                break
            else:
                print('PIN salah. Coba lagi.')
                time.sleep(1)
                VerifPIN(User)
        else:
            print('⚠️ Terlalu banyak percobaan gagal. Transaksi dibatalkan❕❕❕')
            time.sleep(1)
            Keranjang(User)
    else:
        print('⚠️ Tidak dapat memproses transaksi karena PIN tidak ditemukan ⚠️')
        time.sleep(1)
        Katalog(User)
        
def PilihPembayaran(User):
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   VOUCHER TOKO              ^^^ ||')
    print('||---------Apa yang ingin anda inginkan?---------||')
    print('||                1. Tunai                       ||')
    print('||                2. VA Billing                  ||')
    print('||                3. Kembali                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    while True:
        try:
            pilih = int(input('Pilih menu: '))
            if pilih == 1:
                Tunai(User)
            elif pilih == 2:
                VA(User)
            elif pilih == 3:
                Katalog(User)
            else:
                print('❕❕❕Pilihan Anda tidak valid❕❕❕')
                time.sleep(1)
                PilihPembayaran(User)
        except ValueError:
            print('❕❕❕Pilihan Anda tidak valid❕❕❕')
            print('   ⚠️ INPUT MENGGUNAKAN ANGKA ⚠️')
            time.sleep(1)
            PilihPembayaran(User)

def CekVoucher():
    file_voucher = 'E:/Algo1/Project algo 1/UsersVoucher.csv'
    if os.path.exists(file_voucher):
        kode_voucher = input('Masukkan kode voucher (atau tekan Enter untuk lanjut): ').strip().upper()
        if not kode_voucher:
            return 1.0
        data_voucher = pd.read_csv(file_voucher)
        if kode_voucher in data_voucher['Kode'].values:
            index = data_voucher[data_voucher['Kode'] == kode_voucher].index[0]
            if data_voucher.loc[index, 'Stok'] > 0:
                data_voucher.loc[index, 'Stok'] -= 1
                print('   ✅Voucher valid❕❕❕')
                print('✅Diskon 10% diterapkan❕❕❕')
                if data_voucher.loc[index, 'Stok'] == 0:
                    data_voucher = data_voucher.drop(index)
                data_voucher.to_csv(file_voucher, index=False)
                return 0.9
            else:
                print('❌Kode voucher sudah habis stoknya❕❕❕')
        else:
            print('❌Kode voucher tidak valid❕❕❕')
    else:
        print('⚠️ File voucher tidak ditemukan ⚠️')
    return 1.0

def Tunai(User):
    os.system('cls')
    file_keranjang = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    data_keranjang = filedata(file_keranjang)
    if data_keranjang.empty:
        print('\n⚠️ Keranjang kosong, tidak ada pembayaran yang perlu dilakukan ⚠️')
        input('Tekan enter untuk kembali...')
        Pembeli(User)
        return
    print(tabulate(data_keranjang, headers='keys', tablefmt='grid', showindex=False))
    total = data_keranjang['Total'].sum()
    diskon = CekVoucher()
    total *= diskon
    print(f'Total yang harus dibayar: Rp{total:.2f}')
    try:
        bayar = int(input(f'Masukkan jumlah uang dengan tepat: '))
        if bayar >= total:
            kembalian = bayar - total
            if kembalian > 0:
                input(f'Pembayaran berhasil. Kembalian Anda: Rp{kembalian:.2f}')
            else:
                input('✅Pembayaran berhasil❕❕❕')
            Cetak(User)
            SimpanRiwayatPembelian()
            RiwayatPenjualan()
            ResetKeranjang()
        else:
            print('❌Uang tidak cukup. Silakan coba lagi❕❕❕')
            time.sleep(1)
            Tunai(User)
    except ValueError:
        print('⚠️ Input tidak valid. Masukkan angka❕❕❕')
        time.sleep(1)
        Tunai(User)
    input('\nTekan enter untuk kembali...')
    Pembeli(User)

def VA(User):
    os.system('cls')
    file_keranjang = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    data_keranjang = filedata(file_keranjang)
    if data_keranjang.empty:
        print('\n⚠️ Keranjang kosong, tidak ada pembayaran yang perlu dilakukan ⚠️')
        input('Tekan enter untuk kembali...')
        Pembeli(User)
        return
    print(tabulate(data_keranjang, headers='keys', tablefmt='grid', showindex=False))
    total = data_keranjang['Total'].sum()
    diskon = CekVoucher()
    total *= diskon
    print(f'Total yang harus dibayar: Rp.{total:.2f}')
    try:
        bayar = int(input(f'Masukkan jumlah uang dengan tepat (Rp.{total:.2f}): '))
        if bayar == total:
            input('✅Pembayaran berhasil❕❕❕')
            Cetak(User)
            SimpanRiwayatPembelian()
            RiwayatPenjualan()
            ResetKeranjang()
        elif bayar < total:
            print('❌Uang tidak cukup. Silakan coba lagi❕❕❕')
            time.sleep(1)
            VA(User)
        else:
            print('             ❌Pembayaran gagal❕❕❕')
            print('⚠️ Anda harus membayar dengan jumlah uang yang pas❕❕❕')
            time.sleep(1.5)
            VA(User)
    except ValueError:
        print('❌ Input tidak valid. Harap masukkan angka❕❕❕')
        time.sleep(1)
        VA(User)
    input('\nTekan enter untuk kembali...')
    Pembeli(User)

def Cetak(User):
    os.system('cls')
    file_keranjang = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    data_keranjang = filedata(file_keranjang)
    Username = User
    if not data_keranjang.empty:
        total = data_keranjang['Total'].sum()
        print('\n=========   GREENZY   =========')
        print(f'Nama Pengguna: {Username}')
        print(f'Total Harga (Tanpa diskon): Rp{total}')
        print('\nBarang yang dibeli:')
        print(tabulate(data_keranjang, headers='keys', tablefmt='grid', showindex=False))
        print('\n========= TERIMA KASIH =========')

def SimpanRiwayatPembelian():
    file_keranjang = 'E:/Algo1/Project algo 1/UserKeranjang.csv'
    data_keranjang = filedata(file_keranjang)
    if not data_keranjang.empty:
        riwayat_path = 'E:/Algo1/Project algo 1/RiwayatPembelian.csv'
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_keranjang['Tanggal'] = now
        if not os.path.isfile(riwayat_path):
            data_keranjang.to_csv(riwayat_path, index=False, mode='w')
        else:
            data_keranjang.to_csv(riwayat_path, index=False, mode='a', header=False)

def RiwayatPembelian(User):
    os.system('cls')
    data_pembelian = 'E:/Algo1/Project algo 1/RiwayatPembelian.csv'
    if os.path.isfile(data_pembelian):
        pembelian = filedata(data_pembelian)
        if not pembelian.empty:
            print('\n' + '=' * 20 + ' RIWAYAT PEMBELIAN ' + '=' * 20 + '\n')
            print(tabulate(pembelian, headers='keys', tablefmt='grid', showindex=False))
        else:
            print('⚠️ Belum ada riwayat pembelian ⚠️')
    else:
        print('⚠️ File riwayat pembelian tidak ditemukan ⚠️')
    input('\nTekan enter untuk kembali...')
    Pembeli(User)

Awal()      