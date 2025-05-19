from flask import Flask, render_template, request, session
from classes.actors import Actors

prev_option = ""

def apps_actors():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Actors.current()
            Actors.remove(obj.id)
            if not Actors.previous():
                Actors.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Actors.get_id(0))
            strobj = strobj + ';' + request.form["name"] + ';' + \
            request.form["birthdate"] + ';' + request.form["nationality"]
            obj = Actors.from_string(strobj)
            Actors.insert(obj.id)
            Actors.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Actors.current()
            obj.name = request.form["name"]
            obj.birthdate = request.form["birthdate"]
            obj.nationality = request.form["nationality"]
            Actors.update(obj.id)
        elif option == "first":
            Actors.first()
        elif option == "previous":
            Actors.previous()
        elif option == "next":
            Actors.nextrec()
        elif option == "last":
            Actors.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Actors.current()
        if option == 'insert' or len(Actors.lst) == 0:
            id = 0
            id = Actors.get_id(id)
            name = birthdate = nationality = ""
        else:
            id = obj.id
            name = obj.name
            birthdate = obj.birthdate
            nationality = obj.nationality
        return render_template("actors.html", butshow=butshow, butedit=butedit, 
                        id=id,name=name,birthdate=birthdate,nationality=nationality, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)