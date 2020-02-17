#!/usr/bin/env python3
''' This module contains the entry point for the command interpreter '''
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
