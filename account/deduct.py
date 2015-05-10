from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from .utiba_deduct import utiba_deduct

@api_view(['POST'])
def do_deduct(request, format=None):

    if request.method == 'POST':
        amount = request.data['amount']
        mobile = request.data['mobile']
        result_code = utiba_deduct(mobile, amount)
        content = {
            'result': result_code
        }
        return Response(content)
    else:
        return Response({'detail': 'no ken!, you are wrong!'})

