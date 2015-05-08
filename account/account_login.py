from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response


@api_view(['POST'])
def login_for_ken(request, format=None):
    '''
    {
        "username": <username>,
        "password": <password>
    }
    '''
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        users = User.objects.filter(username=username)
        content = {
            'authentication': False,
            'is_admin': False,
            'group_no': None
        }
        if len(users) <= 0:
            return Response(content)
        user = users[0]
        if user.check_password(password):
            accounts = user.account_set.all()
            if len(accounts) > 0:

                account = accounts[0]
                content['authentication'] = True
                content['is_admin'] = account.is_admin
                content['group_no'] = account.group.group_no

        return Response(content)
    else:
        return Response({'detail': 'no ken!, you are wrong!'})

