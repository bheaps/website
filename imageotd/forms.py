from django import forms
from .models import Imageotd,Comment

import StringIO
from PIL import Image

class ImageotdForm(forms.ModelForm):

    class Meta:
        model = Imageotd
        fields = [ 'title','image', 'date','uname', 'desc','likes','dislikes','likdisdif']
        widgets = {
            'likes': forms.HiddenInput, 'dislikes': forms.HiddenInput, 'uname':forms.HiddenInput, 'likdisdif':forms.HiddenInput,
        }
        labels = {
            'desc':('Photo Description'),
        }

    def clean_image(self):
        
        image_field = self.cleaned_data.get('image')
        image_file = StringIO.StringIO(image_field.read())
        image = Image.open(image_file)
        w, h = image.size
        
        if h>w:
            raise forms.ValidationError("Landscape photos only") 
        elif w>2500:
            raise forms.ValidationError("Your photo is too wide, "+str(w)+" pixels is too wide,please reduce size before uploading")
        elif w<600 or h<400:
            raise forms.ValidationError("Your photo is too small, recommended upload size is 640 x 480 pixels")
        image = image.resize((640, 480), Image.ANTIALIAS) #640 480

        image_file = StringIO.StringIO()
        image.save(image_file, 'JPEG', quality=90)

        image_field.file = image_file

        return image_field
    


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [ 'content','imageotd']
        widgets = {
            'imageotd': forms.HiddenInput,
        }#name comment not content
        labels = {
            'content':('Comment'),
        }
