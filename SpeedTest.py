

import speedtest


def CheckInternetSpeed():
   st = speedtest.Speedtest()
   print("Testing Internet Speed")
   download = st.download()  /1_000_000
   upload = st.upload() / 1_000_000

   st.GetServer()
   ping = st.result.ping
   return {
      "download" :round(download,2),
      "upload" :round(upload,2),
      "ping" : round(ping,2)
   }
speed = CheckInternetSpeed()
print(f"Download:{speed['download']}Mbps\nUpload:{speed['upload']}Mbps\nPing :{speed['ping']}ms")

