from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serial import AlbumSerial
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, LoginForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


# List all albums or create new
# /music/all
class AlbumList(APIView):

    # retrieve all albums
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerial(albums, many=True)
        return Response(serializer.data)

    # create new album
    def post(self, request):
        pass


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/signup.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalised) data
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                # log in user and redirect to homepage
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form':form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'music/login.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form })

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form' : form })