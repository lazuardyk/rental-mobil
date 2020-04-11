## Penjelasan Model

Dalam aplikasi ini terdapat 3 model, berikut penjelasannya:

#### User
Model ini adalah model yang berhubungan dengan collection users. Dimana fungsinya adalah untuk keperluan autentikasi dan data user. Di model ini, datanya meliputi: ```nama, alamat, email, no hp, username, password, dan role```. Setiap data terdapat fungsi untuk mengaksesnya maupun mengubahnya.

#### Transaction
Model ini adalah model yang berhubungan dengan collection transactions. Dimana fungsinya adalah untuk mencatat semua transaksi yang berjalan. Di model ini, datanya meliputi: ```id mobil yang dipesan, tanggal peminjaman, durasi, nama pelanggan, alamat pelanggan, nomor hp pelanggan, nomor ktp pelanggan, tanggal lahir pelanggan, dan total harga```. Setiap data terdapat fungsi untuk mengaksesnya maupun mengubahnya.

#### Car
Model ini adalah model yang berhubungan dengan collection cars. Dimana fungsinya adalah untuk mencatat semua mobil yang tersedia untuk dipinjam. Di model ini, datanya meliputi: ```merek mobil, model mobil, warna mobil, nomor polisi, tahun produksi, dan harga per hari nya```. Setiap data terdapat fungsi untuk mengaksesnya maupun mengubahnya.