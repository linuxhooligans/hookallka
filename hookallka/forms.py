from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from hookallka.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        group = Group.objects.get(name='test_my_group')
        if commit:
            user.save()
            user.groups.add(group)
        return user

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)