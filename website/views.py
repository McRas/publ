from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
	records = Record.objects.all()
	# Sprawdzamy czy zalogowany?
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Uwierzytelnienie
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Jesteś zalogowany")
			return redirect('home')
		else:
			messages.success(request, "Wystąpił błąd podczas logowania. Spróbuj ponownie...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})



def logout_user(request):
	logout(request)
	messages.success(request, "Zostałeś wylogowany.")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Uwierzytelnij i zaloguj się
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Zarejestrowałeś się pomyślnie! Powitanie!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Wyszukaj rekordy
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Aby wyświetlić tę stronę, musisz się zalogować...")
		return redirect('home')

	
