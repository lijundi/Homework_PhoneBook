from django import forms


class LinkM(forms.Form):
    imgs = (
        ('#90EE90', "图一"),
        ('#FF6A6A', "图二"),
        ('#836FFF', "图三"),
        ('#FFA500', "图四"),
        ('#98F5FF', "图五"),
        ('#ff6aab', "图六"),
    )
    img = forms.ChoiceField(label="头像", choices=imgs, required=True)
    name = forms.CharField(label="姓名", max_length=30, widget=forms.TextInput, required=True)
    phoneNumber = forms.CharField(label="电话", max_length=15, widget=forms.TextInput, required=True)
    mail = forms.CharField(label="邮箱", max_length=20, widget=forms.TextInput)
    address = forms.CharField(label="住址", max_length=50, widget=forms.TextInput)
    qq = forms.CharField(label="QQ", max_length=15, widget=forms.TextInput)
