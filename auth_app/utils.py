from .models import Userprofile

def create_userprofile(new_account):
    userprofile = Userprofile.objects.create(user=new_account, username=new_account.username, email=new_account.email)
    return userprofile
