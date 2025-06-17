from django import forms
from task.models import Task ,Task_Details


#Django Form 
class TaskForm(forms.Form):
    title = forms.CharField(max_length=240,label="Task Title :")
    description = forms.CharField(widget=forms.Textarea, label="Task Description :")
    due_date = forms.DateField(widget= forms.SelectDateWidget, label="Due Date :")
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def __init__(self,*args,**kwargs):
        #print(args,kwargs)
        employees = kwargs.pop("employees",[])
        #print(employees)
        super().__init__(*args,**kwargs)
        self.fields['assigned_to'].choices = [(emp.id,emp.name) for emp in employees]





#Class Style for Mixin to Apply form Field 
class styledformixin:
  
    defaultclass = "border-2 border-gray-400 p-3 w-full rounded-lg shadow-sm focus:border-rose-400 focus:ring-rose-400 focus:outline-none"
    def apply_wiget_style(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.defaultclass,
                    'placeholder':f"Enter {field.label.lower()}"

                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':self.defaultclass,
                    'placeholder':f"Enter {field.label.lower()}",
                    'rows':5,

                })
            elif isinstance(field.widget,forms.SelectDateWidget):
                 field.widget.attrs.update({
                    'class':"border-2 border-gray-400 p-2 rounded-lg shadow-sm focus:border-rose-400 focus:ring-rose-400 focus:outline-none",
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                 field.widget.attrs.update({
                    'class':'space-y-2',
                })



                




# DJango Model Form 

class TaskModelForm(styledformixin,forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','assigned_to']
        widgets = {
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
        }
      


        #Using Manual Widget create

        # widgets = {
        #     'title':forms.TextInput(attrs={
        #         'class':"border-2 border-gray-400 p-3 w-full rounded-lg shadow-sm focus:border-rose-400 focus:ring-rose-400 focus:outline-none",
        #         'placeholder':"Enter task Title  "
        #     }),
        #     'description':forms.Textarea(attrs={
        #         'class':"border-2 border-gray-400 w-full p-3 rounded-lg shadow-sm focus:border-rose-400 focus:ring-rose-400 resize-none",
        #         'placeholder':"Enter task Decription here..  ",
        #         'rows':5,
        #     }),
        #     'due_date':forms.SelectDateWidget(attrs={
        #         'class':"border-2 border-gray-400 p-2 rounded-lg shadow-sm focus:outline-none focus:border-rose-400 focus:ring-rose-400"
        #     }),
        #     'assigned_to':forms.CheckboxSelectMultiple(attrs={
        #         'class':"space-y-2",
        #     })
        # }
    #Using Mixing Widget 
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.apply_wiget_style()


# TaskDetail Model Form

class TaskDetailModelForm(styledformixin,forms.ModelForm):
    class Meta:
        model = Task_Details
        fields = ['priority','notes']
    
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.apply_wiget_style()




