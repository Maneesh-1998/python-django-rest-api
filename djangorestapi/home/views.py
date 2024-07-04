from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import person
from home.serializer import personserializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework,authtoken.models import token
from home.serializer import loginserializer,personserializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination

class RegisterAPI(APIView):
    def post(self,request):
        _data=request.data
        serializer=Registerserializer(data=_data)
        

        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        serializer.save()

        return Response({'message':'user created'},status=status.HTTP_201_CREATED)
    

class loginAPI(APIView):
    permission_classes=[]
    def post(self,request):
        _data=request.data
        serializer=Loginserializer(data=_data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        user=authenticate(username=serializer.data['username'],password=serializer.data['passsword'])
        if not user:
            return Response({'message':"invalid"},status=status.HTTP_404_NOT_FOUND)
        token,_=token.objects.get_or_create(user=user)

        return Response({'message':'login successfull','token':str(token)},status=status.HTTP_201_CREATED)



class classperson(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        try:
            #objperson=person.objects.filters(team_isnull=False)
            onjperson=person.objects.all()
            page=request.GET.get('page',1)
            page_size=3
            paginator=paginator(objperson,page_size)
            #serializer=personserializer(objperson,many=True)
            serializer=personserializer(paginator.page(page),many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'messgae':"invalide page number"})
    
    def post(self,request):
        return Response("this is a post method from APIView")
    
@api_view(['GET','POST','PUT'])
def index(request):
    if request.method=='GET':
        people_detail={
        'name':'maneesh',
        'age':28,
        'job':'IT Field',
        }    
        return Response(people_detail)
    
    elif request.method=='POST':
        print("this is a POST method")
        return Response("this is a POST method")
    elif request.method=='PUT':
        print("this is a PUT method")
        return Response("this is a PUT method")



@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        objperson=person.objects.filter(team_isnull=False)
        serializer=personserializer(objperson,many=True)
        return Response(serializer.data)  
    elif request.method == 'POST':
        data=request.data
        serializer=personserializer(data=data)
        if serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data=request.data
        obj=person.objects.get(id=data['id'])
        serializer=personserializer(obj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data=request.data
        obj=person.objects.get(id=data['id'])
        serializer=personserializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data=request.data
        obj=person.objects.get(id=data['id'])
        obj.delete
        return Response({'message':'person deleted'})
    

class custompagination(PageNumberPagination):
    page_size=5
    page_size_query_param='page'    


class personViewSets(viewsets.ModelViewSet):
    permission_classes=[]
    serializer_class=personserializer
    queryset=person.objects.all()
    pagination_class=customPagination
    def list(self,request):
        search=request.GET.get("search")
        queryset=self.queryset 
        #paginate the queryset
        paginated_queryset=self.paginate_queryset(queryset)
        
        #serializer the paginated queryset
        serializer=personserializer(paginated_queryset,many=True)

        #rwturn the paginated response
        return self.get_paginated_response({'status':200,'data':serializer.data})