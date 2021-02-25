from django.shortcuts import render
import requests

# Create your views here.

def home(request):
	if request.method=="POST":
		try:
			city= request.POST.get('city')
			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2 = "&q=" + city
			a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
			wa = a1 + a2 + a3 

			res= requests.get(wa)	
			data= res.json()
			temp= data['main']['temp']			
			desc= data['weather'][0]['description']
			degree_sign= u'\N{DEGREE SIGN}'

			icon= "http://api.openweathermap.org/img/w/" + data['weather'][0]['icon'] + ".png"
			msg= "Temperature =  " + str(temp)+ str(degree_sign) + " Condition = " + str(desc) 
			return render(request,'home.html',{'msg':msg,'icon':icon})
			

		except Exception as e:
			return render(request,'home.html',{'msg':'city not found'})

	else:
		return render(request,'home.html')
			



