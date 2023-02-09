from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(requests):
    return HttpResponse("<h1>Hello World</h1>")

def contact(requests):
    a = """
        
    <style>
    body {background-color: lightblue;}
    h1 {colour: black;}
    p {color: red;}
    </style> 


    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>

    <h3> <a href = "https://github.com/HiggsBoson8"> Github: https://github.com/HiggsBoson8  </a> </h3>

    <table border = "2">

        <tr> 
            <th> Name </th> 
            <td> Abay </td> 
        </tr> 

        <tr>
        <th> Number </th>
        <td> +77087617661 </td>
        </tr>

    </table>

    <img src= "https://vse-ekskursii-sochi.ru/storage/tour-images/June2021/w7fhvlH27Q72Ebx8SCe5.jpg" width = "800" height = "500" vspace = "5" hspace = "5">

    <img src= "https://kartinkin.net/pics/uploads/posts/2022-07/1658630675_67-kartinkin-net-p-prirodnie-dostoprimechatelnosti-abkhazii-p-68.jpg">
    """

    return HttpResponse(a)


