
from rest_framework_jwt.utils import jwt_payload_handler

def jwt_user_payload_handler(user):
    payload = jwt_payload_handler(user)
    payload['user_type'] = user.user_type
    # Ajoutez vos champs personnalisés à la payload ici
    return payload

# Path: comptes/serializers.p
# Compare this snippet from comptes/models.py:  
# from django.db import models      

                        