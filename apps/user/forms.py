from allauth.account.forms import LoginForm, ChangePasswordForm, ResetPasswordForm, ResetPasswordKeyForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Field, Div
from django import forms
from django.urls import reverse_lazy


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = self.fields[fieldname].label
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save'), css_class='kt-login__actions'
                )
            )
        )

    def custom_signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = self.fields[fieldname].label
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('login', placeholder='Mobile No', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('password', placeholder='Password', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    HTML('<label class="checkbox"><input type="checkbox" checked="checked" name="remember">'
                         '<span></span> &nbsp;Remember Me</label>'),
                    css_class='form-group text-left col-md-6 mb-5'),
                Column(
                    HTML('<a href="{}" class="kt-link kt-login__link-forgot">Forgot Password ?</a>'.format(
                        reverse_lazy('account_reset_password'))), css_class='text-right col-md-6 mb-5'
                ),
            ),
            Row(
                Column(
                    Submit('submit', 'Submit'), css_class='kt-login__actions'
                )
            )
        )


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = self.fields[fieldname].label

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save'), css_class='kt-login__actions mb-5'
                ),
            )
        )


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # for fieldname in self.fields:
        # self.fields[fieldname].help_text = None
        # self.fields[fieldname].widget.attrs['placeholder'] = self.fields[fieldname].label

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('password1', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('password2', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save'), css_class='kt-login__actions'
                ),
            )
        )


class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = ''

        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('oldpassword', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('password1', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('password2', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save'), css_class='kt-login__actions'
                ),
            )
        )
