
import qrcode

class Gorilla:
   @staticmethod
   def GorillaCode():
      Url = "https://pin.it/7xNgKyal9"
      FilePath = "GorillaFuck.png"

      qr = qrcode.QRCode()
      qr.add_data(Url)
      img = qr.make_image()
      img.save(FilePath)
      print("Done")

if __name__ == '__main__':
   Gorilla.GorillaCode()
