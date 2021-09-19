from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from pages.models import Customers, Trans_hist


# Create your views here.
def index(request):
    return render(request, 'index.html')


def newuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        amount = request.POST.get('amount')
        
        if Customers.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('newuser')
        else:
            newuser = Customers(username=username, email=email, gender=gender, amount=amount, date=datetime.now())
            newuser.save()
            messages.success(request, 'You have successfully added as our customer!')
            return redirect('newuser')
    else:
        return render(request, 'newUser.html')

def customer(request):
    customers = Customers.objects.all()
    return render(request, 'allcustomer.html', {'customers': customers})


def transfer(request, pk):
    info = Customers.objects.filter(username=pk)
    users = Customers.objects.all()
    return render(request, 'transfer.html', {'info': info, 'users': users})


    
def transactions(request):
    users = Customers.objects.all()
    

    if request.method == "POST":
        sender = request.POST.get('FROM')
        reciever = request.POST.get('TO')
        send_amount = request.POST.get('amount')

        debit = Customers.objects.get(username__contains=sender)
        credit = Customers.objects.get(username__contains=reciever)

        sender_id= str(debit.id)
        reciever_id = str(credit.id)

        if sender != reciever and int(debit.amount) > int(send_amount):
            trans_history = Trans_hist(sender=sender, sender_id=sender_id, reciever=reciever,  reciever_id=reciever_id, amount=send_amount, date=datetime.now())
            trans_history.save()
           
        
        if (int(debit.amount) <= int(send_amount)) or (sender == reciever):
            messages.warning(request, "Insufficient Balance in Account! OR You Didn't Choose The Correct Bank Account.")
            return render(request, 'transaction.html', {'users': users})
        else:
            debit.amount = int(debit.amount) - int(send_amount)
            debit.save(update_fields=['amount'])
            messages.success(request, "You have transfered money successfully!")
            
            credit.amount = int(credit.amount) + int(send_amount)
            credit.save(update_fields=['amount'])
            return redirect('transactions')             
        
    else:
        return render(request, 'transaction.html', {'users': users})


def history(request):
    all_hist = Trans_hist.objects.all()
    return render(request, 'history.html', {'all_hist': all_hist})
