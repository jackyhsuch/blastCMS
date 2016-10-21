from django.shortcuts import render, get_object_or_404

from .models import Users
from .forms import NewUserForm

# Create your views here.
def index(request):
    user_list = Users.objects.order_by('id')[:5]
    context = {
        'user_list': user_list,
    }
    return render(request, 'users/index.html', context)


# show each user profile
def show(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    context = {'user': user}

    return render(request, 'users/show.html', context)


# add new user
def new(request):
    context = {}

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            newUser = Users(name=form.cleaned_data['name'],
                            email=form.cleaned_data['email'],
                            contact=form.cleaned_data['contact'],
                            matric_number=form.cleaned_data['matric_number']
                            )
            newUser.save();
            context['success_message'] = 'New user added'

    context['form'] = NewUserForm()

    return render(request, 'users/new.html', context)