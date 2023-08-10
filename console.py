#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''
        Contains the entry point of the command interpreter.
    '''

    prompt = ("(hbnb) ")

    def do_quit(self, args):
        '''
            Quit command to exit the program.
        '''
        return True

    def do_EOF(self, args):
        '''
            Exits after receiving the EOF signal.
        '''
        return True

    def emptyline(self):
        '''
            Prevents printing anything when an empty line is passed.
        '''
        pass

if __name__ == "__main__":
    '''
        Entry point for the loop.
    '''
    HBNBCommand().cmdloop()
