import os
import zipfile

def zipMydir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def zipMyfile(file, ziph):
	ziph.write(file)

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Pedido.zip', 'w', zipfile.ZIP_DEFLATED)
    zipMydir('CON_BORDE', zipf)
    zipMydir('SIN_BORDE', zipf)
    zipf.close()