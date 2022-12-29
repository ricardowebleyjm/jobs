from django.http import JsonResponse
from .serializers import JobSerializer
from .models import Job



def job_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return JsonResponse({"jobs": serializer.data}, safe=False)    