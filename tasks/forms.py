from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
                'rows': 3,
                'placeholder': 'Enter task description'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'status': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'priority': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Make all fields required
        for field in self.fields:
            self.fields[field].required = True
        
        # Add labels
        self.fields['title'].label = 'Task Title'
        self.fields['description'].label = 'Task Description'
        self.fields['due_date'].label = 'Due Date'
        self.fields['status'].label = 'Task Status'
        self.fields['priority'].label = 'Task Priority'
        self.fields['assigned_to'].label = 'Assign To'