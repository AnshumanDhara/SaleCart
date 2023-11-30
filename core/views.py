import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile
from bs4 import BeautifulSoup


# Create your views here.
def homepage(request):
    if request.method == 'POST':
        result = request.POST['Search']
        
        search_query = result
        amazon_results = scrape_amazon(search_query)
        flipkart_results = scrape_flipkart(search_query)
        
        # Combine and format the results
        products = {
            'amazon': amazon_results,
            'flipkart': flipkart_results,
        }
        
        print(products)
        
        return render(request, 'searchresult.html', {'search_result': result})
    return render(request, 'homepage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        valid_user = auth.authenticate(username = username, password = password)
        if valid_user is not None:
            auth.login(request, valid_user)
            return render(request, 'homepage.html', {'message': "Login Successfull!!"})
        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password!!"})
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST.get('password')
        password_confirm = request.POST.get('password-confirm')
        
        if password is None or password_confirm is None:
            return render(request, 'signup.html', {'message': "Both password fields are required!!"})
        elif password == password_confirm:
            if password.strip() == '':
                return render(request, 'signup.html', {'message': "Password field Empty!!"})
            
            # Account creation
            
            if User.objects.filter(username = username).exists():
                return render(request, 'signup.html', {'message': "Username already taken!!"})
            
            if User.objects.filter(email = email).exists():
                return render(request, 'signup.html', {'message': "Email already exists!!"})
            
            # Create new user
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            
            user_model = User.objects.get(username = username)
            new_profile = Profile.objects.create(user = user_model, id_user = user_model.id)
            new_profile.save()
            
            return render(request, 'homepage.html', {'message': "Account created successfully!!"})
        else:
            return render(request, 'signup.html', {'message': "Passwords do not match!!"})
    else:
        return render(request, 'signup.html')

def cart(request):
    return render(request, 'cart.html')

def category1(request):
    return render(request, 'category1.html')

def category2(request):
    return render(request, 'category2.html')

def scrape_amazon(search_query):
    url = f'https://www.amazon.com/s?k={search_query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = []
    for product in soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2hrdt6w0jdtp122jn0441sgwu4 s-latency-cf-section puis-card-border'):
        title = product.find('span', class_='a-size-medium a-color-base a-text-normal').get_text()
        price = product.find('span', class_='a-price-whole').get_text()
        link = product.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href']
        
        results.append({
            'title': title,
            'price': price,
            'link': link,
        })
    
    return results

def scrape_flipkart(search_query):
    url = f'https://www.flipkart.com/search?q={search_query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = []
    for product in soup.find_all('div', class_='_1AtVbE'):
        title = product.find('a', class_='IRpwTa').get_text()
        price = product.find('div', class_='a-price-whole').get_text()
        link = 'https://www.flipkart.com' + product.find('a', class_='IRpwTa')['href']
        
        results.append({
            'title': title,
            'price': price,
            'link': link,
        })
    
    return results


def searchresult(request):
    
    search_query = request.GET.get('query')  # Get the user's search query
    amazon_results = scrape_amazon(search_query)
    flipkart_results = scrape_flipkart(search_query)
    
    # Combine and format the results
    products = {
        'amazon': amazon_results,
        'flipkart': flipkart_results,
    }
    
    print(products)
    
    return render(request, 'searchresult.html')


def Fhomepage(request):
    return render(request, 'Fhomepage.html')

def Flogin(request):
    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-password']
        valid_user = auth.authenticate(username = username, password = password)
        if valid_user is not None:
            auth.login(request, valid_user)
            print("Login Successfull!!")
            return render(request, 'Fhomepage.html', {'message': "Login Successfull!!"})
        else:
            print("Login Unsuccessful!!")
            return render(request, 'Flogin.html', {'message': "Invalid Username or Password!!"})
    else:
        return render(request, 'Flogin.html')

def Fresetpassword(request):
    return render(request, 'Fresetpassword.html')

def Fsearch_category(request):
    return render(request, 'Fsearch_category.html')

def Fsearch_name(request):
    return render(request, 'Fsearch_name.html')

def Fsignup(request):
    return render(request, 'Fsignup.html')

def Fuserprofile(request):
    return render(request, 'Fuserprofile.html')

def Fcart(request):
    return render(request, 'Fcart.html')
