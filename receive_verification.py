class ReceiveVerification():
    def __init__(self, credentials, safeCredentials, ip):
        self.isThereAnyError = False
        self.credentials = credentials
        self.safeCredentials = safeCredentials
        self.ip = ip
        self.cache = []

    def basicAuth(self):
        if (not self.credentials):
            self.isThereAnyError = True
            print('YOUR CREDENTIALS ARE EMPTY')
            return
        
        print(f'BASIC AUTH')

    def restructureAuth(self):
        if (self.isThereAnyError):
            print('YOU CANNOT CONTINUE WITH THE RESTRUCTURE AUTH THERE ARE AN ERROR')
            return

        if (not self.safeCredentials):
            print('YOUR CREDENTIALS ARE EMPTY')
            return

        print(f'RESTRUCTURE AUTH {self.safeCredentials}')

    def ipAuth(self):
        if (self.isThereAnyError):
            print('YOU CANNOT CONTINUE WITH THE IP AUTH THERE ARE AN ERROR')
            return

        if (not self.ip):
            print('THE IP WAS NOT PROVIDED')
            return

        print(f'IP AUTH: ${self.ip}')

    def cacheAuth(self):
        if (self.isThereAnyError):
            print('YOU CANNOT CONTINUE WITH THE CACHE AUTH THERE ARE AN ERROR')
            return
        
        print('CACHE AUTH')
