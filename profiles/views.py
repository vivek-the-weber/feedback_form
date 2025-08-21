from django.shortcuts import render
from django.views.generic import View,ListView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .forms import ProfileForm
from .models import ProfileModel

class CreateProfileView(CreateView):
    template_name = "profiles/create_profiles.html"
    model = ProfileModel
    fields = "__all__"
    success_url = "/profiles"
# class CreateProfileView(View):
#     def get(self,request):
#         form = ProfileForm()
#         return render(request,"profiles/create_profiles.html",{
#             "form":form,
#         })
    
#     def post(self,request):
#         submitted_form = ProfileForm(request.POST,request.FILES)
#         if submitted_form.is_valid():
#             profile = ProfileModel(profile_image = request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#         else:
#             return render(request,"profiles/create_profiles.html",{
#             "form":submitted_form,
#             })
class ProfilesListView(ListView):
    model = ProfileModel
    template_name = "profiles/user_profiles.html"
    context_object_name =  "all_profiles"
    