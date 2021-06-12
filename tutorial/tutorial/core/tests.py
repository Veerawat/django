from django.test import TestCase
from core.models import Profile

# Create your tests here.
class TestProfile(TestCase):
    def test_profile_should_have_defined_fields(self):
        profile = Profile.objects.create(
            name="Veerawat Prodpran",
            nick_name="Wat",
            email="veerawat@odds.team",
            tel="0000000000"
        )
        
        assert profile.name == "Veerawat Prodpran"
        assert profile.nick_name == "Wat"
        assert profile.email == "veerawat@odds.team"
        assert profile.tel == "0000000000"


# class TestIndexView(TestCase):
#     def test_index_view_should_be_access(self):
#         Profile.objects.create(
#             name="TTTT"
#         )

#         res = self.client.get("/")

#         assert res == 200

#     def test_post(self):
#         Profile.objects.create(
#             name="TTTT"
#         )

#         data = {
#             "email": "vee@odds.team"
#         }

#         res = self.client.post("/", data=data)

        