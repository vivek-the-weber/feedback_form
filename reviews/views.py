from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
# Create your views here.


from .forms import ReviewForm
from .models import ReviewModel

class ReviewView(CreateView):
    model = ReviewModel
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
    # def get(self,request):
    #     form = ReviewForm()

    #     return render(request,"reviews/review.html",{
    #     "form" : form
    #     })
    # def post(self,request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("thank-you")
    #     return render(request,"reviews/review.html",{
    #     "form" : form
    #     })

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context
    
class AllReviewsView(ListView):
    template_name = "reviews/all_reviews.html"
    model = ReviewModel
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt = 4)
    #     return data
class DetailReviewView(DetailView):
    template_name = "reviews/detail_review.html"
    model = ReviewModel
    context_object_name = "single_review"









# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")
#     else:
#         form = ReviewForm()
#     return render(request,"reviews/review.html",{
#         "form" : form
#     })
