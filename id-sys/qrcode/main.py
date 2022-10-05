import qrcode

def qrgen(msg):
    qr = qrcode.make(msg)
    qr.save("qrcode.jpg")

#Teste#################################################################
if __name__ == "__main__":
    texto = "Google  <www.google.com>"
    qrgen(texto)