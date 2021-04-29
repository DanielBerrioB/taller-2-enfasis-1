class InvokerVerification:
    def __init__(self):
        self.verifications = []

    def addVerification(self, verification):
        self.verifications.append(verification)
    
    def doAllVerification(self):
        for verification in self.verifications:
            if (not verification.execute()):
                self.verifications = []
                return False
        self.verifications = []
        return True

