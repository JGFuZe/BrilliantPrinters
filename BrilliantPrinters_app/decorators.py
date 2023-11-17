from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):

    #Create a decorator that will pass in a function from views
    def decorator(view_func):

        # Create a wrapper function
        def wrapper_func(request, *args, **kwargs):
            print('role: ', allowed_roles)
            
            #Group variable to hold a list of groups
            group = None

            #If user groups exist
            if (request.user.groups.exists()):

                # Store all groups types in group variable
                group = request.user.groups.all()[0].name

            # Check if any of the groups in the group list match a group in allowed_roles
            if (group in allowed_roles):
                # Then return the function for execution
                return view_func(request, *args, **kwargs)
            
            else:
                return HttpResponse('Sorry you are not authorized to view this page!')
            
        #
        return wrapper_func
    
    #
    return decorator