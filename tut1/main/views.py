from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# import the database components so we can display the item using the id passed through
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id):
    
    # you put html code in the HttpResponse function

    # look for the item in ToDoList with matching id
    ls = ToDoList.objects.get(id=id)
                                        # display the name of the item using ls.name
                                        # we use the dictionary after to pass any variables
                                        # to base.html in the form of:
                                        # "varname" = varvalue
    if ls in response.user.todolist.all():
        {"save": ["save"], "c1":["clicked"]}
        # check if this is a post or get
        if response.method == "POST":
            print(response.POST)
            # differentiating what happens depending on which button you pressed, pass the button name through
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            # adding a new item
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                # validate the input

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/view.html", {"ls":ls})

# create a new view
def home(response):
    return render(response, "main/home.html", {})

# create a form

def create(response):
    # this with give the user, you cna use this to check authenticatoin etc
    # response.user

    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            # now we need to change this to save to a specific user
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

            # adding this will redirect us to a new page once we create a new item
            return HttpResponseRedirect("/%i" %t.id)
    else: 
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})