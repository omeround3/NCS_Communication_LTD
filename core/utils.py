from django.contrib.auth.forms import SetPasswordForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _, ungettext
from django.contrib.auth import password_validation
from django.conf import settings
from django_password_validators.password_history.password_validation import UniquePasswordsValidator
from django_password_validators.password_character_requirements.password_validation import PasswordCharacterValidator

def _my_help_text_unique(self):
    return _(f'Your password must always differ from your last {self.last_passwords} passwords.')

UniquePasswordsValidator.get_help_text = _my_help_text_unique

def _my_help_text_chars(self):
    validation_req = []
    if self.min_length_alpha:
        validation_req.append(
            ungettext(
                "%(min_length)s letter",
                "%(min_length)s letters",
                self.min_length_alpha
            ) % {'min_length': self.min_length_alpha}
        )
    if self.min_length_digit:
        validation_req.append(
            ungettext(
                "%(min_length)s digit",
                "%(min_length)s digits",
                self.min_length_digit
            ) % {'min_length': self.min_length_digit}
        )
    if self.min_length_lower:
        validation_req.append(
            ungettext(
                "%(min_length)s lower letter",
                "%(min_length)s lower letters",
                self.min_length_lower
            ) % {'min_length': self.min_length_lower}
        )
    if self.min_length_upper:
        validation_req.append(
            ungettext(
                "%(min_length)s upper letter",
                "%(min_length)s upper letters",
                self.min_length_upper
            ) % {'min_length': self.min_length_upper}
        )
    if self.special_characters:
        validation_req.append(
            ungettext(
                "%(min_length_special)s special char",
                "%(min_length_special)s special chars",
                self.min_length_special
            ) % {'min_length_special': str(self.min_length_special), 'special_characters': self.special_characters}
        )
    return _("Your password must contain") + ' ' + ', '.join(validation_req) + '.'
PasswordCharacterValidator.get_help_text = _my_help_text_chars