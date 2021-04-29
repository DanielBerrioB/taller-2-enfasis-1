from verification import BasicVerification, CacheVerification, IPVerification, RestructureVerification
from invoker_verification import InvokerVerification
from receive_verification import ReceiveVerification

class Authorizer:
    def verify(self, credentials, safeCredentials, ip):
        # Se recibe la informacion que el cliente o usuario puede traer
        receiveNotification = ReceiveVerification(credentials, safeCredentials, ip)

        # Se crean las instancias de los diferentes comandos que se necesitan para hacer
        # la verificacion y se les pasa una instancia de ReceiveVerification
        basicAuth = BasicVerification(receiveNotification)
        restructureAuth = RestructureVerification(receiveNotification)
        cacheAuth = CacheVerification(receiveNotification)
        ipAuth = IPVerification(receiveNotification)

        # Se crea el invocador de los comandos que va a servir para llamarlos
        invokerVerifications = InvokerVerification()

        # Se agregan los comandos al invocador
        invokerVerifications.addVerification(basicAuth)
        invokerVerifications.addVerification(restructureAuth)
        invokerVerifications.addVerification(ipAuth)
        invokerVerifications.addVerification(cacheAuth)

        # Se ejecutan los comandos de forma secuencial
        return invokerVerifications.doAllVerification()