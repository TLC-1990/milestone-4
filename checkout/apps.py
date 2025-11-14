"""AppConfig for the checkout app."""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """Configuration for the checkout app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "checkout"
    
    def ready(self):
        """Import signals when the app is ready."""
        import checkout.signals
        
