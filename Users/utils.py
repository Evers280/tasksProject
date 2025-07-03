from django.conf import settings
from allauth.account.utils import user_pk_to_url_str

def custom_password_reset_url_generator(request, user, temp_key):
    """
    Génère l'URL de réinitialisation de mot de passe pour le frontend.
    """
    # Génère l'identifiant utilisateur encodé
    uid = user_pk_to_url_str(user)
    
    # Récupère l'URL de base depuis les settings
    reset_url_base = settings.PASSWORD_RESET_CONFIRM_URL
    return reset_url_base.format(uid=uid, token=temp_key)