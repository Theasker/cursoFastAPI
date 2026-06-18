from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("Guardando usuario en BBDD")

class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")

def guardar(entidad):
    entidad.guardar()

usuario = Usuario()
sesion = Sesion()
guardar(usuario)
guardar(sesion)

https://www.amazon.es/Anker-Cargador-Port%C3%A1til-Velocidad-Integrado/dp/B0CZ9LH53B?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=J6GXIKO8QFNC&dib=eyJ2IjoiMSJ9.OPlIKfXNHIofvrm-E-OLt0g8dt-IgpSKYQeBVFEqB-r-ffKbWsgRJ-NGnULWxXobITAjaOf_ttMg9g7pyXWJGAUoZHaHgbv0C_BZJOmi9LvXUO6Z_s06TYJhzS68xQvkr8arkVRKFsrrKnqxap2umX25lM8RaRIWfY3dfjC06KnijGtEpa5bKRBSWP3f9Cb2pvrfv_IOrpdRJ8AMxESP4VnCuPxNTYInCIPk3oB4s3uWyJdH5e9iobhLSV8zolsTmuOXKDtHTC8gFi688huCtQKSzXzSeNjvm_ar36-O7fw.2y1xBCVbMLGP06fuquUv5Ix2oXMKjSZszVfShbDNRc8&dib_tag=se&keywords=power%2Bbank%2B20000mah&qid=1781785072&sprefix=power%2Bbank%2B20000mah%2B%2Caps%2C161&sr=8-12&th=1
https://www.amazon.es/UGREEN-Port%C3%A1til-20000mAh-Integrado-Compatible/dp/B0DSPVDYQ9/ref=sr_1_8?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=J6GXIKO8QFNC&dib=eyJ2IjoiMSJ9.OPlIKfXNHIofvrm-E-OLt0g8dt-IgpSKYQeBVFEqB-r-ffKbWsgRJ-NGnULWxXobITAjaOf_ttMg9g7pyXWJGAUoZHaHgbv0C_BZJOmi9LvXUO6Z_s06TYJhzS68xQvkr8arkVRKFsrrKnqxap2umX25lM8RaRIWfY3dfjC06KnijGtEpa5bKRBSWP3f9Cb2pvrfv_IOrpdRJ8AMxESP4VnCuPxNTYInCIPk3oB4s3uWyJdH5e9iobhLSV8zolsTmuOXKDtHTC8gFi688huCtQKSzXzSeNjvm_ar36-O7fw.2y1xBCVbMLGP06fuquUv5Ix2oXMKjSZszVfShbDNRc8&dib_tag=se&keywords=power+bank+20000mah&qid=1781785072&sprefix=power+bank+20000mah+%2Caps%2C161&sr=8-8
https://www.mediamarkt.es/es/product/_powerbank-xiaomi-bhr9738gl-20000-mah-1x-usb-c-1x-usb-a-cable-integrado-225w-gris-oscuro-1612470.html