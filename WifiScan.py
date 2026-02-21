
import qrcode
import os
class WifiCode:
   @staticmethod
   def WifiScanLogin():
      ssid = "Slim"
      password = "Make@2026"
      security = "WPA2"

      WifiData = f"WIFI:S:{ssid};T:{security};P:{password};;"
      qr = qrcode.QRCode(border = 10,box_size =10)
      qr.add_data(WifiData)
      qr.make(fit=True)

      FilePath = "WifiQr.png"

      img = qr.make_image(fill_color ="black",back_color = "white")
      img.save(FilePath)
      print("Done")
if __name__ == '__main__':
   WifiCode.WifiScanLogin()
