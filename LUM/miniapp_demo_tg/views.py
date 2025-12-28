import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from .models import Tour, TourDropDownElements,TG_Profile



@csrf_exempt
def save_telegram_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_data = data.get('user')
        profile, created = TG_Profile.objects.update_or_create(
            tg_id=user_data['id'],
            defaults={
                'first_name': user_data.get('first_name', 'user_name'),
                'second_name': user_data.get('last_name', ''),
                'user_icon': user_data.get('photo_url', ''),
            }
        )
        return JsonResponse({'status': 'success'})

class TourList(ListView):
    model = Tour
    ordering = 'tour_name'
    template_name = 'tours_list.html'
    context_object_name = 'tours'
    paginate_by = 3


class TourDetail(DetailView):
    model = Tour
    template_name = 'tour_detail.html'
    context_object_name = 'tour'


class TourDropDownElementsListView(ListView):
    model = TourDropDownElements
    ordering = 'element_created_at'
    context_object_name = 'drop_down_el'
    template_name = 'tours_list.html'