from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (("m", "Male"), ("f", "Female"))
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField(
        max_length=60, min_length=5
    )  # 5 <= fullname's length <= 60
    height = forms.IntegerField(max_value=250, min_value=70)  # 70 <= height <= 250
    age = forms.IntegerField(max_value=99, min_value=14)  # 14 <= age <= 99

    # implement full_name validation function here
    # full_name should be a title
    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if full_name.istitle():
            return full_name
        raise forms.ValidationError("Error")
