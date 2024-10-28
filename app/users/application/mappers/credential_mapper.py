from app.users.domain.models.credential_model import Credential
from app.users.application.schemas.requests.credential_request import CredentialRequest

class CredentialMapper:
    @staticmethod
    def to_domain(credential: CredentialRequest) -> Credential:
        return Credential(
            id=None,
            uuid=None,
            password=credential.password,
            created_at=None,
            verified_at=None,
            token=None,
            contact=None
        )

    @staticmethod
    def to_dict(credential: Credential) -> dict:
        return {
            'id': credential.id,
            'uuid': credential.uuid,
            'password': credential.password,
            'created_at': credential.created_at,
            'verified_at': credential.verified_at,
            'token': credential.token,
            'contact': credential.contact
        }