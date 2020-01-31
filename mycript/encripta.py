from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

fd = open("textoEncriptar.txt","r")

frase = fd.read().encode()

token1 = f.encrypt(frase)
print(token1)

fd1 = open("textoEncriptado.txt","w")

fd1.write(token1)

#token3 = f.decrypt("lalalalala u will never get me!!")

token2 = f.decrypt(token1)
print(token2)
