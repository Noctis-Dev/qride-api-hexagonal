from abc import ABC, abstractmethod

class MercadoPagoClientInterface(ABC):
    @abstractmethod
    def create_preference(self, preference_data: dict) -> dict:
        pass

    @abstractmethod
    def get_payment(self, payment_id: str) -> dict:
        pass