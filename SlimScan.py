
import qrcode

class Slim:
   @staticmethod
   def SlimCode():
      ssid = "Slim"
      password = "Make@2026"
      security = "WPA"
      FilePath = "SlimNet.png"

      WifiData = f"WIFI:S:{ssid};T:{security};P:{password};;"

      qr = qrcode.QRCode(border = 4,box_size =10)
      qr.add_data(WifiData)
      qr.make(fit=True)
      img = qr.make_image(fill_color = "black",back_color = "white")
      img.save(FilePath)
      print("Done")

if __name__ == '__main__':
   Slim.SlimCode()
