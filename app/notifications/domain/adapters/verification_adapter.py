from abc import ABC, abstractmethod

class VerificationAdapter(ABC):
    @abstractmethod
    def send_verification_code(self, mensaje_data: dict):
        pass
