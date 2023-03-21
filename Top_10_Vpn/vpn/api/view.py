from rest_framework.response import Response
from rest_framework.decorators import api_view
from vpn.models import Top_ten,VpnList,All_avilable_filter,Form,Specification
from .serializers import Top_Ten_Serializer,VpnList_Serializer,All_available_filter_Serializer,Form_Serializer,Specification_Serializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def Instruction(request):
    instruction =(
        ('','instructions'),
        ('/specification',"specification_of_all_vpn"),
        ('/vpn','Vpn_List'),
        ('/vpn/id','Vpn_with_id'),
        ('/vpn/id/logo','logo_of_vpn_of_id'),
        ('/All_available_filter','All_availble_filter'),
        ('/All_available_filter/id','A filter with id'),
        ('/Top_ten','Top_ten_of_all_filters'),
        ('/Top_ten/id','Top_ten_of_a_filter_with_id'),
        ('/form/','form details')
    )
    return Response(instruction)


@api_view(["GET"])
def Specification_without_id(request):
    specification_data_set = Specification.objects.all()
    serializer = Specification_Serializer(specification_data_set,many = True)
    return Response(serializer.data)



@api_view(["GET"])
def Vpn_without_id(request):
    Vpn_list_data_set = VpnList.objects.all()
    serializer = VpnList_Serializer(Vpn_list_data_set,many = True)
    return Response(serializer.data)


@api_view(["GET"])
def Vpn_with_id(request,pk):
    try:
        top_10_data_object = VpnList.objects.get(title=pk)
        serializer = VpnList_Serializer(top_10_data_object,many = False)
        return Response(serializer.data)
    except:
        return Response("No object present with that specific id")


@api_view(['GET'])
def get_logo_url(request,pk):
    try:
        vpn_logo = VpnList.objects.get(id =pk)
        logo_url = vpn_logo.logo.url
        return Response({'logo_url': logo_url})
    except:
        return Response("No object present with that specific id")  
        



@api_view(["GET"])
def All_avilable_filter_without_id(request):
    All_avilable_filter_data_set = All_avilable_filter.objects.all()
    serializer =All_available_filter_Serializer(All_avilable_filter_data_set,many = True)
    return Response(serializer.data)


@api_view(["GET"])
def All_avilable_filter_with_id(request,pk):
    try:
        All_avilable_filter_data_object =All_avilable_filter.objects.get(id=pk)
        serializer = All_available_filter_Serializer(All_avilable_filter_data_object,many = False)
        return Response(serializer.data)
    except:
        return Response("No object present with that specific id")        


@api_view(["GET"])
def Top_10_without_id(request):
    top_10_data_set = Top_ten.objects.all()
    serializer = Top_Ten_Serializer(top_10_data_set,many = True)
    return Response(serializer.data)


@api_view(["GET"])
def Top_10_with_id(request,pk):
    try:
        top_10_data_object = Top_ten.objects.get(type__name=pk)
        serializer = Top_Ten_Serializer(top_10_data_object,many = False)
        return Response(serializer.data)
    except:
        return Response("No object present with that specific id")


@api_view(['GET','POST','PUT'])
def Form_without_id(request):
        if request.method == 'POST':
            try:
                
                json_input = request.body
                stream = io.BytesIO(json_input)
                parsed_data = JSONParser().parse(stream)
                serializer = Form_Serializer(data=parsed_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response("successfully saved")
                else:
                    return Response(serializer.errors)
            except Exception:
                return Response("Error occurs")

        Form_set = Form.objects.all()
        serializer = Form_Serializer(Form_set, many=True)
        return Response(serializer.data)
    



    