import qrcode
img=qrcode.make('https://github.com')
#img.save('qrcode.png')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('xinxingzhao')
qr.make(fit=True)

img = qr.make_image()
img.save('qrcode.png','png')
