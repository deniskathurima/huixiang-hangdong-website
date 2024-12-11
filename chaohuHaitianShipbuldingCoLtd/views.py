from django.shortcuts import render


def home(request):
    return render(request, 'Hindex.html')


def about1(request):
    return render(request, 'about1.html')


def contact1(request):
    return render(request, 'contact1.html')


def shipBuilding(request):
    return render(request, 'shipBuilding.html')


def seaHorse(request):
    return render(request, 'seaHorse.html')


def greenLine1(request):
    return render(request, 'greenLine1.html')


def finFin(request):
    return render(request, 'finFin.html')


def darEsSalaam(request):
    return render(request, 'darEsSalaam.html')


def barrackBarge(request):
    return render(request, 'barrackBarge.html')


def mDahor(request):
    return render(request, '10MDahor.html')


def mPatrolBoat(request):
    return render(request, '10MPatrolBoat.html')


def dregering(request):
    return render(request, 'dredging.html')


def fishing(request):
    return render(request, 'fishing.html')
