from tortoise import fields, models, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
class User(models.Model):
    """ Model user """
    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
    first_name = fields.CharField(max_length=100,default="")
    last_name = fields.CharField(max_length=100, null=True,default="")
    date_join = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DatetimeField(null=True)
    is_active = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    avatar = fields.CharField(max_length=100, null=True)
    # social_accounts: fields.ReverseRelation['SocialAccount']
    def full_name(self) -> str:
        return self.first_name + self.last_name
    class PydanticMeta:
        computed = ["full_name"]
        exclude = ('full_name')
User_Pydantic = pydantic_model_creator(User, name="User",exclude=['id','date_join'])
Users_Pydantic = pydantic_model_creator(User,name="UserCreate",exclude_readonly=True,exclude=['id'])
UserIn_Pydantic = pydantic_model_creator(
    User, name="UserIn", exclude_readonly=True)
