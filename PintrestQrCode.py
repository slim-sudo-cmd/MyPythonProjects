
import qrcode

class OldQrCode:
   @staticmethod
   def QrCodeGenerate():
      url = "https://pin.it/6AXXtyOBH"
      FilePath = "qrcode.png"

      qr = qrcode.QRCode()
      qr.add_data(url)
      img = qr.make_image()
      img.save(FilePath)
      print("Check the file")

if __name__ == '__main__':
   OldQrCode.QrCodeGenerate()
