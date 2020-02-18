#!/usr/bin/env python3
''' This module contains the entry point for the command interpreter '''
import cmd
import re
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User

classList = ['BaseModel', 'User', 'City', 'State', 'Place', 'Amenity', 'Review']


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        ''' Disables repetition of previous command '''
        pass

    def do_quit(self, s):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    do_EOF = do_quit
    help_EOF = help_quit

    def do_create(self, s):
        ''' Creates a new instance of the class and saves it '''
        if s not in classList:
            if len(s) == 0:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")
        else:
            new_object = eval("{}()".format(s))
            models.storage.save()
            print(new_object.id)

    def help_create(self):
        print("Creates a new instance of the class, saves it to file.")
        print("Ex $ create BaseModel")
        print()

    def do_show(self, s):
        ''' Prints the string representation of an instance '''
        if len(s) == 0:
            print("** class name missing **")
        else:
            line = s.split()
            if line[0] not in classList:
                print("** class doesn't exist **")
            elif len(line) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(line[0], line[1])
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def help_show(self):
        print("Prints the string representation of an instance")
        print("Ex $ show BaseModel 6dc7ee88-a360-49bb-b998-7140917e65a5")
        print()

    def do_destroy(self, s):
        ''' Deletes an instance and saves the changes to file '''
        if len(s) == 0:
            print("** class name missing **")
        else:
            line = s.split()
            if line[0] not in classList:
                print("** class doesn't exist **")
            elif len(line) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(line[0], line[1])
                if key in models.storage.all().keys():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def help_destroy(self):
        print("Deletes an instance and saves changes to file")
        print("Ex $ destroy BaseModel 6dc7ee88-a360-49bb-b998-7140917e65a5")
        print()

    def do_all(self, s):
        ''' Prints all instances of the class name '''
        list_all = []
        if len(s) == 0:
            for keys in models.storage.all().keys():
                    list_all.append(str(models.storage.all()[keys]))
            print(list_all)
        elif s not in classList:
            print("** class doesn't exist **")
        else:
            for keys in models.storage.all().keys():
                if s == keys.split('.')[0]:
                    list_all.append(str(models.storage.all()[keys]))
            print(list_all)

    def help_all(self):
        print("Prints all instances based of the class name.")
        print("Ex: $ all BaseModel")
        print()

    def do_update(self, s):
        ''' Updates an instance by adding or updating attribute '''
        if len(s) == 0:
            print("** class name missing **")
        else:
            line = re.findall(r"(\".+\"|\S+)", s)
            if line[0] not in classList:
                print("** class doesn't exist **")
            elif len(line) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(line[0], line[1])
                if key not in models.storage.all().keys():
                    print("** no instance found **")
                elif len(line) == 2:
                    print("** attribute name missing **")
                elif len(line) == 3:
                    print("** value missing **")
                else:
                    if line[3][0] == '"' and line[3][-1] == '"':
                        line[3] = line[3][1:-1]
                    setattr(models.storage.all()[key], line[2], line[3])
                    models.storage.save()
    
    def help_update(self):
        print("Updates an instance attribute")
        print("ex $ [id] attribute_name attribute_value")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
