import qrcode
from PIL import Image

# Nhập đường dẫn từ người dùng
url = input("Nhập nội dung cần tạo qr: ")

# Tạo mã QR từ đường dẫn
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Tạo hình ảnh QR
img = qr.make_image(fill_color='black', back_color='white')

# Lưu hình ảnh QR vào tệp PNG
img.save('qr_code.png', 'PNG')

# Hiển thị hình ảnh QR
img.show()
