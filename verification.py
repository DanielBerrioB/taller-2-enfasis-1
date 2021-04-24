class Verification:
    def execute(self):
        pass

class BasicVerification(Verification):
    def __init__(self, receiveNotification):
        self.verification = receiveNotification

    def execute(self):
        self.verification.basicAuth()

class RestructureVerification(Verification):
    def __init__(self, receiveNotification):
        self.verification = receiveNotification

    def execute(self):
        self.verification.restructureAuth()

class IPVerification(Verification):
    def __init__(self, receiveNotification):
        self.verification = receiveNotification

    def execute(self):
        self.verification.ipAuth()

class CacheVerification(Verification):
    def __init__(self, receiveNotification):
        self.verification = receiveNotification

    def execute(self):
        self.verification.cacheAuth()