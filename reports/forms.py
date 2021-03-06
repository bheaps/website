from django import forms
from .models import Report,Participant,Comment
from django.forms.models import inlineformset_factory
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

MAX_PARTICIPANTS = 20

ParticipantFormSet = inlineformset_factory(Report, Participant, extra=MAX_PARTICIPANTS,fields = [ 'name','report'], can_delete=False)

class ReportsForm(forms.ModelForm):
    

    class Meta:
        model = Report
        fields = [ 'title', 'writer', 'text','trip_area', 'elevation_gain','distance_coverred','likes','dislikes','uname']
        widgets = {
             'writer':forms.HiddenInput, 'likes': forms.HiddenInput, 'dislikes': forms.HiddenInput, 'uname':forms.HiddenInput, 'text': CKEditorUploadingWidget(),
        }
        labels = {
            'text':(''),
        }
        help_texts = {
            'trip_area':('OPTIONAL'),
            'elevation_gain':('OPTIONAL'),
            'distance_coverred':('OPTIONAL'),
        }

class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = [ 'name','report']
        widgets = {
            'report': forms.HiddenInput,
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [ 'content','report']
        widgets = {
            'report': forms.HiddenInput,
        }#name comment not content
        labels = {
            'content':('Comment'),
        }

from haystack.forms import SearchForm


class ReportsSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
