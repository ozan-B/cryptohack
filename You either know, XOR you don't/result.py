from pwn import xor

mesaj = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

kısmi_anahtar = "myXORkey"
tam_anahtar = (kısmi_anahtar * (len(mesaj) // len(kısmi_anahtar) + 1))[:len(mesaj)]


result = xor(mesaj, tam_anahtar)

print(result.decode())
