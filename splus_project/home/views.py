from django.shortcuts import render

def index(request):
        
    products = [
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1051",
         "price": "۱۱.۲۹۰.۰۰۰",
         "quantity": 0},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس زنانه",
         "code": "PH-1052",
         "price": "۱۲.۶۹۰.۰۰۰",
         "quantity": 3},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "کاسیو پلاس مردانه",
         "code": "PH-1053",
         "price": "۱۰.۱۹۰.۰۰۰",
         "quantity": 10},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1054",
         "price": "۱۵.۰۰۰.۰۰۰",
         "quantity": 1},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه و زنانه",
         "code": "PH-1055",
         "price": "۹.۸۰۷.۰۰۰",
         "quantity": 0},
    ]
    
    return render(request, 'home/home.html',
        {
            "products": products
        })

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')
