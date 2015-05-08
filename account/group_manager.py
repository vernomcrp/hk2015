from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from account.models import GroupAccount
from rest_framework import status


@api_view(['POST'])
def register_new_account(request, format=None):
    '''
    {
        "username": <username>,
        "password: <password>,
        "email: <email>,
        "group": <group_no>,
    }
    '''
    if request.method == 'POST':
        print 'd0'
        username = request.data['username']
        password = request.data['password']
        email = request.data.get('email')
        group_no = request.data.get('group_no', None)
        print 'd1'
        user = User.objects.create(username=username, email=email)
        if user:
            user.set_password(password)
            print 'Password has set.'
        else:
            return Response({'detail': 'Cannot create user'}, status=status.HTTP_400_BAD_REQUEST)

        if group_no:
            groups = GroupAccount.objects.filter(group_no=group_no)
            if groups:
                group = groups[0]
                user.group = group
                user.save()
            else:
                return Response({'detail': 'Cannot find target group'}, status=status.HTTP_400_BAD_REQUEST)