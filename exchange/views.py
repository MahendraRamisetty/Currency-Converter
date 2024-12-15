import requests
from django.shortcuts import render
from .models import ConversionHistory

def currency_converter_view(request):
    converted = None
    rate = None
    amount = None
    source_currency = None
    target_currency = None

    if request.method == 'POST':
        source_currency = request.POST.get('source_currency')
        target_currency = request.POST.get('target_currency')
        amount = float(request.POST.get('amount'))

        # Fetch conversion rate from external API
        api_key = '7f0d02d8c6543b49ac3392c4'  # Replace with your API key
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_currency}/{target_currency}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rate = data['conversion_rate']
            converted = amount * rate

            # Save conversion to the database
            ConversionHistory.objects.create(
                source_currency=source_currency,
                target_currency=target_currency,
                amount=amount,
                converted_amount=converted,
                rate=rate
            )

    # Fetch conversion history
    history = ConversionHistory.objects.all().order_by('-timestamp')

    return render(request, 'index.html', {
        'converted': converted,
        'rate': rate,
        'amount': amount,
        'source_currency': source_currency,
        'target_currency': target_currency,
        'history': history
    })
