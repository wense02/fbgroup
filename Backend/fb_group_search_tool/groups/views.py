from django.shortcuts import render
from django.http import JsonResponse
import requests
from . models import FacebookGroup
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response


class FacebookGroupView(APIView):
    def get(self, request):
        output = [{"name": output.name,
                  "description": output.description,
                  "member_count": output.member_count,
                  "is_private": output.is_private}
                  for output in FacebookGroup.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = FacebookGroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save
            return Response(serializer.data)


def search_groups(request):
    # Handle GET request to search groups
    if request.method == 'GET':
        # Extract town name and radius from request
        town_name = request.GET.get('town_name')
        radius = request.GET.get('radius')

        # Perform search using Facebook Graph API (replace with actual API call)
        # Example: 
        # groups = requests.get(f'https://graph.facebook.com/v12.0/search?type=group&q={town_name}&fields=name,description,member_count,is_private&access_token=YOUR_ACCESS_TOKEN').json()

        # Mock data for demonstration
        groups = [
            {'name': 'Group 1', 'description': 'Description 1', 'member_count': 1500, 'is_private': True},
            {'name': 'Group 2', 'description': 'Description 2', 'member_count': 2000, 'is_private': True},
            {'name': 'Group 3', 'description': 'Description 2', 'member_count': 2500, 'is_private': True},
            {'name': 'Group 4', 'description': 'Description 2', 'member_count': 3000, 'is_private': True},
            {'name': 'Group 5', 'description': 'Description 2', 'member_count': 3500, 'is_private': True},
            # Add more groups as needed
        ]

        # Filter groups based on criteria (e.g., member count, private status)
        filtered_groups = [group for group in groups if group['member_count'] > 1000 and group['is_private']]

        # Return JSON response with filtered groups
        return JsonResponse({'groups': filtered_groups})

    # Handle other types of requests (e.g., POST)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})


def search_groups(request):
    if request.method == 'GET':
        # Extract town name and radius from request
        town_name = request.GET.get('town_name')
        radius = request.GET.get('radius')

        # Get all groups within the specified town
        groups = FacebookGroup.objects.all()

        # Filter groups based on criteria (e.g., member count, private status)
        filtered_groups = [groups for groups in groups if groups.member_count > 1000 and groups.is_private]

        # Prepare response data
        response_data = []
        for group in filtered_groups:
             if 'member_count' in groups:
                response_data.append({
                     'name': groups.get('name', ''),
                     'description': groups.get('description', ''),
                      'member_count': groups['member_count']  # Ensure 'member_count' exists before accessing it
                })


        # Return JSON response with filtered groups
        return JsonResponse({'groups': response_data})

    else:
        # Handle other types of requests (e.g., POST)
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint'})