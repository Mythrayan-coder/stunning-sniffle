from django import forms
from .models import chepak

#class ReviewForm(forms.Form):

#    user_name = forms.CharField(label="Your Name",max_length=100,
#                                error_messages={"required":"Please enter your name.",
#                                            "max_length":"Name is too long"})
#    review_text = forms.CharField(label="your feedback",
#                                  widget=forms.Textarea,max_length=200,)
#    rating = forms.IntegerField(label="Rating (1-5)",
#                                min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(),
        label="Confirm Password"
    )

    class Meta:
        model = chepak
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'email_address': "Your Email ID",
            'password': "Your Password",
        }
        error_messages = {
            'email_address': {
                'required': "Please enter your Email.",
                'max_length': "Email is too long."
            },
        }

    def clean(self):
        cleaned = super().clean()
        pwd = cleaned.get("password")
        cpwd = cleaned.get("confirm_password")
        if pwd and cpwd and pwd != cpwd:
            self.add_error("confirm_password", "Passwords do not match.")

class ChepakLoginForm(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)