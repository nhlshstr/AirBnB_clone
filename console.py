#!/usr/bin/env python3
''' This module contains the entry point for the command interpreter '''
import cmd
import models
from models.base_model import BaseModel

classList = ['BaseModel']

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
                    

    def help_create(self):
        print("Creates a new instance of the class, saves it to file.")
        print("Ex $ create BaseModel")
        print()

    def do_all(self, s):
        ''' Prints all instances of the class name '''
        if s == "BaseModel":
            print(models.storage.all())
            '''
            for keys in storage.__objects.keys():
                print(storage.__objects[keys])
            '''
        else:
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints all instances based of the class name.")
        print("Ex: $ all BaseModel")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
