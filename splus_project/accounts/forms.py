from django import forms
from django.core import validators


class RegisterForm(forms.Form):

    first_name = forms.CharField(
        label="نام",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام خود را وارد کنید",
                "class": "form-control",
                "autocomplete": "given-name",
            }
        )
    )

    last_name = forms.CharField(
        label="نام خانوادگی",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام خانوادگی خود را وارد کنید",
                "class": "form-control",
                "autocomplete": "family-name",
            }
        )
    )

    phone_number = forms.CharField(
        label="شماره موبایل",
        required=True,
        validators=[
            validators.MinLengthValidator(
                11,
                message="شماره موبایل باید ۱۱ رقم باشد."
            ),
            validators.MaxLengthValidator(
                11,
                message="شماره موبایل باید ۱۱ رقم باشد."
            ),
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "09123456789",
                "class": "form-control",
                "autocomplete": "tel",
                "inputmode": "numeric",
            }
        )
    )

    email = forms.EmailField(
        label="ایمیل",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@gmail.com",
                "class": "form-control",
                "autocomplete": "email",
            }
        )
    )

    password = forms.CharField(
        label="رمز عبور",
        required=True,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "رمز عبور",
                "class": "form-control",
                "autocomplete": "new-password",
            }
        )
    )

    confirm_password = forms.CharField(
        label="تکرار رمز عبور",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "تکرار رمز عبور",
                "class": "form-control",
                "autocomplete": "new-password",
            }
        )
    )

    accept_terms = forms.BooleanField(
        label="قوانین و شرایط سایت را می‌پذیرم.",
        required=True,
    )

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]

        if not phone.startswith("09"):
            raise forms.ValidationError(
                "شماره موبایل باید با 09 شروع شود."
            )

        if not phone.isdigit():
            raise forms.ValidationError(
                "شماره موبایل باید فقط شامل اعداد باشد."
            )

        return phone

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    "رمز عبور و تکرار رمز عبور یکسان نیستند."
                )

        return cleaned_data