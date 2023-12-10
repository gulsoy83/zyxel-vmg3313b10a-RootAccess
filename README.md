# zyxel-vmg3313b10a-RootAccess
This ISP Router comes with heavily restricted firmware. Even with root access. 
Nevertheless, you can get root account enabled by restoring this ttvmg3313root.conf backup file to your router.

![c8c13b44af3dea019dd48cb45ff3a9ed6d98e729](https://github.com/gulsoy83/zyxel-vmg3313b10a-RootAccess/assets/46426033/cf207f08-1d44-48d3-8d27-917d834e0615)

1. Reset your router to default settings from 192.186.1.1 page. (Default user/password is admin/turktelekom.)
2. After this,  go to 192.168.1.1, you can login by these credentials: <br />
  root/enzovmg3313 <br />
  admin/ttvmg3313 <br />
3. You can connect to Wi-Fi with this credentials: <br />
   Wi-Fi Name: VMG3313 / Password: 20222022 <br />

Connect to the router via telnet to disable TR-69. <br />
echo $(ls /bin) <br />
echo $(tr69cli) <br />
echo $(tr69cli display) <br />
Directly disabling is not possible so modify parameters: password, port etc. to negate your ISP's access your device.

---
You can check these links to try appylying same logic to your zyxel isp router to get root account.
The process is simple, obtain .conf file, decrypt it, enable root account by editing decrypted file, encrypt it again and restore it to the modem.

1. https://abrazalaweb.net/2018/11/descomprimir-archivos-de-configuracion-lzw/
2. https://hexed.it/
3. https://github.com/joeatwork/python-lzw
