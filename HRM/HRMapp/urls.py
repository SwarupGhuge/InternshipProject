from django.urls import path
from HRMapp.views import Sample,ShowForm,FormEdit,FormsDelete,FormsUpdate

urlpatterns = [
    path('',Sample,name='sample'),
    path('show/',ShowForm,name='showform'),

    path('edit/<int:id>/',FormEdit,name='formsedit'),
    path('update/<int:id>/',FormsUpdate,name='formsupdate'),
    path('delete/<int:id>/',FormsDelete,name='formsdelete'),

]
