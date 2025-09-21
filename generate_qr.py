import qrcode
import datetime

def data_setting() -> datetime:
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year

    return (day, month, year)

def qr_setting(data) -> qrcode:
    gen = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)
    gen.add_data(data)
    gen.make(fit=True)

    return gen
    

def generator(data_to_transform) -> None:
    day, month, year = data_setting()

    gen = qr_setting(data_to_transform)
    img = gen.make_image(fill_color="black", back_color="white")
    
    img.save(f'{day}-{month}-{year}_qr_code.png')