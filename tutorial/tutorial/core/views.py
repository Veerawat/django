from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse

from django.views import View
from django.shortcuts import render
from core.forms import SubscriberForm
from core.models import Profile, Subscriber
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



from core.serializers import SubscriberSerializer, ProfileSerializer


# Create your views here.
def index(request):
    return render(
            request,
            "profile.html",
            {
                "name": "Veerawat Prodpran",
                "nick_name": "Wat",
                "email": "veerawat@odds.team",
                "tel": "0000000000",
            },
        )


class IndexView(View):
    def get(self, request):
        profile = Profile.objects.get(id=1)
        return render(
            request,
            "profile.html",
            {
                "name": profile.name,
                "nick_name": "Wat",
                "email": "veerawat@odds.team",
                "tel": "0000000000",
            },
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get("email"))

        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get("email"))

            email = form.cleaned_data.get("email")
            Subscriber.objects.create(email=email)

        profile = Profile.objects.get(id=1)
        return render(
            request,
            "profile.html",
            {
                "name": "Vee",
                "form": form,
                "nick_name": "Wat",
                "birth_date": "11/08/1993",
                "email": profile.email,
                "tel": "0000000000",
            },
        )


class SubscriberAPIView(APIView):
    def get(self, request):
        subscriber = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfileAPIView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        print("profile: ",profile)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
