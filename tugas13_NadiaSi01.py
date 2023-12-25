class Hewan:
    def init(self, nama, makanan, habitat, reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.reproduksi = reproduksi

class Badak(Hewan):
    def init(self, nama, habitat):
        super().init(nama, "tumbuhan", habitat, "viviparous")

    def menyerang(self):
        return f"{self.nama} sedang menyerang dengan tanduknya!"

class Ikan(Hewan):
    def init(self, nama, habitat):
        super().init(nama, "plankton", habitat, "oviparous")

    def berenang(self):
        return f"{self.nama} sedang berenang di air."

class Ular(Hewan):
    def init(self, nama, habitat):
        super().init(nama, "hewan kecil", habitat, "oviparous")

    def merayap(self):
        return f"{self.nama}sedang merayap tanah"
    

 #contoh penggunaan
    Badak_sumatra =Badak("Badak Sumatra","Hutan")
    print(Badak sumatra meyerang()) 

    Ikan_koi =Ikan("Ikan Koi","kolam")
    print(Ikan_koi.berenang()) 

    ular_sanca = ("Ular Sanca","Hutan") 
    print(ular_sanca.merayap())