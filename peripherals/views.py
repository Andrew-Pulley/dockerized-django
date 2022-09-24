from django.http import JsonResponse


def status_view(request):
    """
    Heartbeat response
    """
    return JsonResponse({'status': 'ok'})
