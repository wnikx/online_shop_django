from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import LoginForm
from django.contrib.auth.decorators import login_required
