# Modo de usar:

Abrir o aplicativo e digitar a senha para o app conferir na API do pwned se a senha digitada foi comprometida em algum vazamento ou invasão
<br>

# Informações:

Deixei disponível o arquivo em .exe caso queira ter o aplicativo funcionando localmente sem precisar compilar o codig. Tambem pode usar o código a vontade para compilar você mesmo.

## Como compilar:
<b>Antes de fazer isso, se certifique que tambem baixou a pasta assets e seu conteúdo e que tem o ```pyinstaller``` instalado.</b>
<br>
<br>
Para instalar o pyinstaller: ```pip install pyinstaller```
<br>
<br>
Abrir o cmd na pasta onde esta baixado o arquivo ```checarsenhas.py``` e digitar ```pyinstaller --name="Verificador de senhas" --onefile --icon=".\assets\favicon.ico" checarsenhas.py```. E assim você terá o executável dentro da pasta ```dist```
