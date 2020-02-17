from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import userProfile
#
# # test the user registrasi endpoint
# class RegistrationTestCase(APITestCase):
#     def test_registration(self):
#         data={"username":"irvan","password":"oke12345","email":"irvanrizki@gmail.com"}
#         response=self.client.post('/auth/users/',data)
#         self.assertEqual(response.status_code,status.HTTP_201_CREATED)
#
# #test case untuk userProfile model
# class userProfileTestCase(APITestCase):
#     profile_list_url=reverse('all-profiles')
#     def setUp(self):
#         #membuat user baru dengan membuat request post untuk emdpoint djoser
#         self.user=self.client.post('/auth/users/', data = {'username':'irvan', 'password':'oke12345'})
#         #mendapatkan json web token untuk user yang baru di membuat
#         response = self.client.post('/auth/jwt/create',data={'username':'irvan', 'password':'oke12345'})
#         self.token=response.data['access']
#         self.api_authentication()
#
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION='bearer '+self.token)
#
#     #menambil list semua user profile dimana request user sudah di authenticasi
#     def test_userprofile_list_authenticated(self):
#         self.client.force_authenticate(user=None)
#         response=self.client.get(self.profile_list_url)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)
#
#
#     #mengabil list semua user profile dimana request user unauthenticasi
#     def test_userprofile_list_unauthenticated(self):
#         self.client.force_authenticate(user=None)
#         response=self.client.get(self.profile_list_url)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#
#     #mengecek untuk mengambil profile detail autehnticasi users
#     def test_userprofile_detail_retrive(self):
#         response=self.client.get(reverse('profile', kwargs={'pk':1}))
#         print(response.data)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)
#
#
#     #mengisi profile user yang secara automatis di buat menggunakan signals
#     def  test_userprofile_profile(self):
#         profile_data={'description':'saya adalah karakter game terkenal', 'location':'PS3'}
#         response=self.client.put(reverse('profile', kwargs={'pk':1}),data=profile_data)
#         # print(response.data)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)

# test the user registrasi endpoint
class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data={"username":"irvan","password":"oke12345","email":"irvanrizki@gmail.com"}
        response=self.client.post('/auth/users/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class userProfileTestCase(APITestCase):
    profile_list_url=reverse('all-profiles')
    def setUp(self):
        # create a new user making a post request to djoser endpoint
        self.user=self.client.post('/auth/users/',data={'username':'mario','password':'i-keep-jumping'})
        # obtain a json web token for the newly created user
        response=self.client.post('/auth/jwt/create/',data={'username':'mario','password':'i-keep-jumping'})
        self.token=response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    # retrieve a list of all user profiles while the request user is authenticated
    def test_userprofile_list_authenticated(self):
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    # retrieve a list of all user profiles while the request user is unauthenticated
    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    # check to retrieve the profile details of the authenticated user
    def test_userprofile_detail_retrieve(self):
        response=self.client.get(reverse('profile',kwargs={'pk':1}))
        # print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    # populate the user profile that was automatically created using the signals
    def test_userprofile_profile(self):
        profile_data={'description':'I am a very famous game character','location':'nintendo world','is_creator':'true',}
        response=self.client.put(reverse('profile',kwargs={'pk':1}),data=profile_data)
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
