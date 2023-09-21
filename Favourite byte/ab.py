from pwn import xor



hex_encoded_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"


# Dizeyi baytlara çevirin
hex_bytes = bytes.fromhex(hex_encoded_string)

# Secret byte deneyin (0x00'dan 0xFF'e kadar)
for key in range(256):
    decoded_bytes = xor(hex_bytes, key)
    decoded_text = decoded_bytes.decode("utf-8", errors="ignore")
    print(f"Key: {key}, Decoded Text: {decoded_text}")# Dizeyi baytlara çevirin
hex_bytes = bytes.fromhex(hex_encoded_string)

print("kkakkak")