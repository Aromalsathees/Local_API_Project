from django.shortcuts import render
from django.http import JsonResponse

# Hardcoded JSON data
PLACES_DATA = {
    "Japan": {
        # "image" : "https://as2.ftcdn.net/v2/jpg/01/22/01/51/1000_F_122015145_k2jNV8ed5pAlYi9fRjQAzjtZ8DVAYhF9.jpg",
        "temples": [
             {"name": "Kyoto Temple", "image": "https://h5p.org/sites/default/files/h5p/content/1209180/images/file-6113d5f8845dc.jpg", "description": "Historic temple in Kyoto", "rating": 4.7 ,},
            {"name": "Senso-ji Temple", "description": "Ancient temple in Tokyo", "rating": 4.6}
        ],
        "bars": [
            {"name": "Bar Kyu", "description": "Cozy bar in Tokyo", "rating": 4.3}
        ],
        "entertainment": [
            {"name": "Tokyo Tower", "description": "Iconic landmark in Tokyo", "rating": 4.5}
        ],
        "collegs": [
            {"name":"Ebanezzar college" ,"description":"university of science"},
              {"name":"Antman college" ,"description":"Applied science"}
        ]
    },
    "America": {
        "temples": [],
        "bars": [
            {"name": "Bar Central", "description": "Popular bar in New York", "rating": 4.4},
                        {"name": "Bar Central", "description": "Popular bar in New York", "rating": 4.4},
                                    {"name": "Bar Central", "description": "Popular bar in New York", "rating": 4.4},
                                                {"name": "Bar Central", "description": "Popular bar in New York", "rating": 4.4},
                                                            {"name": "Bar Central", "description": "Popular bar in New York", "rating": 4.4}
        ],
        "entertainment": [
            {"name": "Statue of Liberty", "description": "Symbol of freedom in New York", "rating": 4.8},
            {"name": "Grand Canyon", "description": "Massive canyon in Arizona", "rating": 4.9},
             {"name": "Statue of Liberty", "description": "Symbol of freedom in New York", "rating": 4.8},
            {"name": "Grand Canyon", "description": "Massive canyon in Arizona", "rating": 4.9}
        ]
    }
}



def index(request):
    return render(request, 'index.html')

def places_view(request):
    country = request.GET.get('country')
    country = str(country).capitalize()
    if country in PLACES_DATA:
        return JsonResponse(PLACES_DATA[country])
    else:
        #  return JsonResponse({}, status=404)
          return JsonResponse({'error':'not found'}, status=404)
       