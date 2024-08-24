from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Profile
from .forms import UserRegistrationForm, ProfileEditForm, UserEditForm


class SignUpView2(View):

    def get(self, request):
        user_form = UserRegistrationForm()
        context = {
            "user_form": user_form
        }

        return render(request, "account/register.html", context)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.data.get('username'):
            pass

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            context = {
                'new_user': new_user
            }
            return render(request, 'account/register_done.html', context)

def profile_view(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(User, username=request.user)
        user = request.user
        profile=Profile.objects.get(user=user)
        context = {
            'user': user,
            'profile': profile
        }
        return render(request, 'pages/profile.html', context)
    else:
        return HttpResponseForbidden("saytda ro'yxatdan o'tishingiz kerak")

class EditUserView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'account/profile_edit.html',
                      {"user_form": user_form, 'profile_form': profile_form})
    def post(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile')