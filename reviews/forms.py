from django import forms

from .models import ReviewModel
# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name:",max_length=100,error_messages={
#         "required": "Your name must not be empty",
#         "max_length" : "Please enter small name"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea,max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = "__all__"
        # exclude = ["owner_comment"] 
        labels = {
            "username": "Your Name:",
            "review_text":"Your Feedback:",
            "rating":"Rating",
        }
        error_messages = {
            "username": {
                "required": "Your name must not be empty",
                "max_length" : "Please enter small name"
            }
        }
