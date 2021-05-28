from django.contrib.auth.forms import SetPasswordForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _, ungettext
from django.contrib.auth import password_validation
from django.conf import settings
from django_password_validators.password_history.password_validation import UniquePasswordsValidator
from django_password_validators.password_character_requirements.password_validation import PasswordCharacterValidator


class MySetPasswordForm(SetPasswordForm):
    validators = password_validation.get_password_validators(settings.AUTH_PASSWORD_VALIDATORS_2)

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(validators),
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(
            password2, self.user, self.validators)
        return password2


class MyPasswordChangeForm(MySetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = {
        **MySetPasswordForm.error_messages,
        'password_incorrect': _("Your old password was entered incorrectly. Please enter it again."),
    }
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        password_validation.password_changed(old_password, self.user, self.validators)
        return old_password

def _my_help_text_unique(self):
        return _(f'Your password must differ from your last {self.last_passwords} passwords')
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